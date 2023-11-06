"""This module contains the methods needed to establish the UDP, TCP and TLS connections.
SSL contexts can be created by using the methods contained in this module and a custom
socket receive method (recvall) is being defined, in order to have more capacity
of the messages that are received
    """
import socket
import ssl
# import fcntl
import struct
import uuid
import os

import netifaces
from iso15118.secc import secc_config
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates

from iso15118.evcc import evcc_config
from iso15118.secc import secc_config


def create_evcc_ssl_context(v2grootpath):
    """Creates the SSL contect for the EVCC (client). EVCC will verify
    the SECC counterpart based on the V2G Root certificate.

    Args:
        v2grootpath (String): Path to the V2G Root certificate stored by the EVCC

    Returns:
        SSLContext: The SSL Context containing the TLS version, the verification mode
        and the TLS Suite that will be used. EVCC will receive the SECC leaf Certificate
        chain with its corresponding private key and verify if it has the same V2G Root certificate
    """
    
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations(v2grootpath)
    context.set_ciphers("ECDHE-ECDSA-AES128-SHA256")
    return context

# pylint: disable=no-member
def create_secc_sll_context(server_cert, server_key):
    """Creates the SSL contect for the SECC (server). SECC will send its leaf certificate
    chain and its corresponding private key and will be verified by the EVCC. Verification
    is based on the V2G Root certificate

    Args:
        server_cert (String): Path to the Secc leaf certificate stored by the SECC
        server_key (String): Path to the Secc leaf private key stored by the SECC

    Returns:
        SSLContext: The SSL Context containing the TLS version, the verification mode
        and the TLS Suite that will be used. SECC will send the SECC leaf Certificate
        chain and its corresponding private key and  EVCC will verify if its V2G Root
        certificate is the same
    """
    print(server_cert)
    print(server_key)
    # Load SECC Certificate
    with open(server_cert, 'rb') as pkcs12_file:
        pkcs12_data = pkcs12_file.read()
    pkcs12_password_bytes = "123456".encode('utf8')

    # Returns a tuple where 0:privatekey, 1:certificate, 2:certificate_chain
    cpocertchain = load_key_and_certificates(pkcs12_data, pkcs12_password_bytes)

    cposub1 = cpocertchain[2][0].public_bytes(serialization.Encoding.PEM)
    cposub2 = cpocertchain[2][1].public_bytes(serialization.Encoding.PEM)
    cpocert = cpocertchain[1].public_bytes(serialization.Encoding.PEM)
    cpocertpem_path = secc_config.SECC_CERTCHAIN_PEM_PATH
    f = open(cpocertpem_path , "wb")
    f.write(cpocert)
    f.write(cposub2)
    f.write(cposub1)

    f.close()
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(cpocertpem_path, server_key, password='123456')
    context.verify_mode = ssl.VerifyMode.CERT_NONE
    context.set_ciphers("ECDH-ECDSA-AES128-SHA256:" "ECDHE-ECDSA-AES128-SHA256")
    return context


def recvall(sock):
    """Receive method for a specific socket. Will store the whole
    bytes message that a socket receives.

    Args:
        sock Socket: The socket that receives the data

    Returns:
        bytes: Data received from socket
    """
    BUFF_SIZE = 4096  # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if not data:
            break
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data


def get_ip(interface):
    """Based on the interface provided generates its corresponding IP Adress

    Args:
        interface (string): Name of the interface

    Returns:
        ipadress: _description_
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(interface[:15], 'utf-8'))
    )[20:24])


def get_mac_in_hex():
    mac_int = uuid.getnode()

    # Convert the 48-bit integer to a 6-byte binary string
    mac_bytes = mac_int.to_bytes(6, byteorder='big')

    # Convert the 6-byte binary string to a hexadecimal string
    mac_hex = ''.join('{:02x}'.format(x) for x in mac_bytes)
    return mac_hex



        

# Specify the interface name (e.g. "eth0" or "wlan0")
def get_broadcast_adress(interface):
    

    # Get the interface's IPv4 address and netmask
    interface_addrs = netifaces.ifaddresses(interface)
    ipv4_addr = interface_addrs[netifaces.AF_INET][0]["addr"]
    ipv4_netmask = interface_addrs[netifaces.AF_INET][0]["netmask"]

    # Calculate the broadcast address
    ipv4_broadcast = socket.inet_ntoa(
        struct.pack(
            ">I",
            struct.unpack(">I", socket.inet_aton(ipv4_addr))[0]
            | (struct.unpack(">I", socket.inet_aton(ipv4_netmask))[0] ^ 0xFFFFFFFF),
        )
    )

    return ipv4_broadcast


def create_udp_tcp_serversocket():
    """Instantiates the UDP and the TCP Sockets. UDP will be used for the multicast
    SDP messages and TCP will be used for the AppProtocol and V2G Messages
    """
    # UDP Layer
    print("Starting UDP")
    udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udpserver.bind(('0.0.0.0', secc_config.UDP_PORT))
    # TCP Layer
    print("Starting TCP")
    tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpserver.bind(('0.0.0.0', secc_config.TCP_PORT))
    tcpserver.listen()
    return (udpserver, tcpserver)