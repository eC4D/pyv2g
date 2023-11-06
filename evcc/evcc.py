
"""Module describing the behiavour from the EVCC side . The constructor
will instantiate an EVCC object, new attributes can be added that simulate
the controller. The EVCC object is capable of:
1)Receiving Messages
2)Processing Messages
3)Reacting to Messages
4)Change States
"""
# pylint: disable=import-error
import cProfile
import re

import socket

from iso15118.evcc import evcc_states
#from iso5118.evcc import ev_states
from iso15118.evcc.evcontroller import EVSimController
from iso15118.evcc import evcc_config
from iso15118.common.XML import msgdatatypes1
from iso15118.common.exi_utils import exi_utils
from iso15118.common.network import network

from iso15118.common.handlers import MessageHandler

from iso15118.evcc.evcc_handler import EVCCMessageHandler

import os, time

path = "../"
os.chdir(path)


# pylint: disable=no-member
# pylint: disable=line-too-long
class EVCC():
    """Class Repressenting SECC. Stores important attributes that simulate SECC behaviour
    and enables the functionality to receive, process and send messages
    """
    def __init__(self):
        self.port = 15118
        self.tls = evcc_config.TLS
        self.tcp = evcc_config.TCP
        self.charging = evcc_config.CHARGING
        self.contract_cert = None
        self.contract_private_key = None

        self.oem_prov_cert = evcc_config.OEMPATH
        self.oem_prov_key = evcc_config.OEMPROV_PRIV_KEY
        self.payment_option = evcc_config.SELECTEDPAYMENTOPTION
        # Represents the battery status. Percentage value. Will be used for the CurrentDemandReq/Res
        # Charging Loop
        self.controller = EVSimController(evcc_config.CHARGING_MODE)

        self.genchallenge = None

        # Initiating UDP socket
        self.udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #Enabling UDP Broadcasting
        self.udpclient.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # TCP socket. Will be Initiated after SECCDiscoveryRes
        self.tcpsock = None

        # State Machine for EVCC
        res = evcc_states.create_evcc_state_machine()
        #res = ev_states.ControlPilot
        self.statemachine = res[0]

        #self.message_handler = EVCCMessageHandler(self)
        self.message_handler = MessageHandler(self, None)

    def display_state(self):
        """Displays the current state of the EVCC
        """
        print("New State: ", self.statemachine.state)



    def check_incoming_messages(self):
        """Waits for the next message (either from the UDP or TCP socket). EVCC will
        receive the message and react accordingly.
        """
        while True:

            # Check For UDP Messages IF State is Initial
            if self.statemachine.state == "Initial":
                print("Waiting For SECCDiscoveryRes UDP Message...")
                seccdiscoveryres_message, address = self.udpclient.recvfrom(
                    1024)
                #self.message_handler.process_message_and_react(seccdiscoveryres_message, address)
                self.message_handler.process_message_and_react(seccdiscoveryres_message, True, address)

            # Check For TCP Messages on other States (Will happen after SECCDisoveryReq/Res)
            elif self.tcpsock:
                try:
                    data = network.recvall(self.tcpsock)
                except socket.error:
                    print("Socket is closed")
                    break
                self.message_handler.process_message_and_react(data, True)
                #self.message_handler.process_message_and_react(data)
            else:
                exi_utils.print_colored_red("Client closed")





    def check_state_and_react(self):
        """Method used to initiate the ISO process
        """
        current_state = self.statemachine.state
        if current_state == 'Initial':
            self.send_secc_discovery_req()

    def send_secc_discovery_req(self):
        """Generates and sends SECC message  with a payload of two bytes length, one for
        the security level and one for the transport protocol to use
        First Byte:    1 with TLS, 0 without TLS
        Second Byte:   1 with UDP, 0 without UDP (TCP)
        """
        tls = self.tls
        tcp = self.tcp

        """using byte literals (b"\x00") instead of to_bytes method to create the payload bytes, more concise and efficient.
            By removing redundant conditions and simplifying the code, you can improve its readability and potentially enhance its performance."""
        if tls:
            if tcp:
                payload = b"\x00\x00"
            else:
                payload = b"\x00\x01"
        else:
            if tcp:
                payload = b"\x10\x00"
            else:
                payload = b"\x10\x10"

        """Using a dictionary instead of multiple if statements  to check the values of tls and tcp, 
            use a dictionary to store the corresponding payload values and retrieve them based on a tuple of (tls, tcp):"""

        # payload_map = {
        #     (True, True): b'\x00\x00',
        #     (True, False): b'\x00\x01',
        #     (False, True): b'\x10\x00',
        #     (False, False): b'\x10\x10',
        # }
        # payload = payload_map[(tls, tcp)]

        # if (tls and tcp):
        #     payload = 0x00.to_bytes(1, "big") + 0x00.to_bytes(1, "big")
        # if (tls and not tcp):
        #     payload = 0x00.to_bytes(1, "big") + 0x01.to_bytes(1, "big")
        # if (not tls and tcp):
        #     payload = 0x10.to_bytes(1, "big") + 0x00.to_bytes(1, "big")
        # if (not tls and not tcp):
        #     payload = 0x10.to_bytes(1, "big") + 0x10.to_bytes(1, "big")

        # Converting payload to V2G Message
        v2gmsg = exi_utils.add_Header_v2gEXI(payload, "sdpreq")
        if evcc_config.SLOW_MODE:
            print("1: Send SECCDiscoveryReq?")
            print("1: Message to Send: ")
            print(v2gmsg)
            input("Press Enter to continue...")
        self.udpclient.sendto(v2gmsg, ("<broadcast>", 15118))
        print("Message sent!")


    def establish_evcc_tcp_connection(self, ipadress, port):

        exi_utils.print_colored_red("Starting TCP")
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if (self.tcp and self.tls):
            context = network.create_evcc_ssl_context(evcc_config.V2GROOTPATH)
            self.tcpsock = context.wrap_socket(self.tcpsock, server_side=False)
            self.tcpsock.connect((ipadress, port))
            exi_utils.print_colored_red("SSL established. Peer: {}".format(
                self.tcpsock.getpeercert()))

    def parse_ev_status(self):
        '''Parses the values of the EVStatus Controller to XML format'''
        evstatus = self.controller.get_ev_status()
        if self.controller.is_DC_mode:
            return msgdatatypes1.DC_EVStatusType(
                EVReady=evstatus["EVReady"],
                EVErrorCode=evstatus["EVErrorCode"],
                EVRESSSOC=self.controller.evressoc)



if __name__ == '__main__':
    ev = EVCC()
    # t1 = time.time()
    ev.check_state_and_react()
    #print(f't1 = {time.time() - t1}')
   # t2 = time.time()
    ev.check_incoming_messages()
   # ev.proccess()
    #print(f't2 = {time.time() - t2}')