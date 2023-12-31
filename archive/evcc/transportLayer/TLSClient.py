#######################################################
# 
# TLSClient.py
# Python implementation of the Class TLSClient
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 11:23:30
# Original author: Fabian.Stichtenoth
# 
#######################################################
import ssl
import socket
import logging
import threading
import io
import OpenSSL

from shared.misc.V2GTPMessage import V2GTPMessage
from shared.misc.TimeRestrictions import TimeRestrictions
from shared.utils.SecurityUtils import SecurityUtils
from shared.enumerations.GlobalValues import GlobalValues
from evcc.transportLayer.StatefulTransportLayerClient import StatefulTransportLayerClient

_unique_tls_client_instance = None
thread_lock = threading.Lock()


class TLSClient(StatefulTransportLayerClient):

    def __init__(self):
        super().__init__()
        self._tls_socket_to_server = None
        self._unique_tls_client_instance = TLSClient()
        self._interrupt = False

    @classmethod
    def get_instance(cls):
        """Checks for an instance and creates one if there isn't one already. The
        synchronized block is only entered once as long as there is no existing
        instance of the TLSClient (safes valuable resource)
        :return: None
        """
        global _unique_tls_client_instance
        if _unique_tls_client_instance is None:
            thread_lock.acquire()
            if _unique_tls_client_instance is None:
                _unique_tls_client_instance = TLSClient()
            thread_lock.release()
        return _unique_tls_client_instance

    def get_tls_socket_to_server(self) -> socket:
        return self._tls_socket_to_server

    def initialize(self, host=None, port=None) -> bool:
        """Initializes the TLS client as soon as a SECCDiscoveryRes message arrived. Exceptions are caught
        :param host:
        :param port:
        :return: bool
        """
        super().initialize()
        try:
            SecurityUtils.set_ssl_context(str(GlobalValues.EVCC_KEYSTORE_FILEPATH),
                                          str(GlobalValues.EVCC_TRUSTSTORE_FILEPATH),
                                          str(GlobalValues.PASSPHRASE_FOR_CERTIFICATES_AND_KEYS))

            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

            cipher = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256"
            context.set_ciphers(cipher)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.debug("Creating socket to TLS server ...")
            # s.bind((host, port))
            logging.debug("TLS socket to server created")

            self.get_tls_socket_to_server().settimeout(TimeRestrictions.V2G_EVCC_COMMUNICATION_SETUP_TIMEOUT)

            logging.debug("Starting TLS handshake ...")

            conn = context.wrap_socket(s, server_side=False)
            conn.connect((host, port))

            logging.debug("TLS handshake finished")

            # TODO: correctly implement the following
            cert = ssl.get_server_certificate(self.get_tls_socket_to_server())
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            secc_certificates = x509.get_subject().get_components()
            secc_leaf_certificate = secc_certificates[0]

            if not SecurityUtils.verify_domain_component(secc_leaf_certificate, "CPO"):
                # TODO: implement .getSubjectX500Principal().getName()
                logging.error("TLS client connection failed. \n\t" +
                              "Reason: Domain component of SECC certificate not valid, expected 'DC=CPO'. \n\t" +
                              "Distinuished name of SECC certificate: " + secc_leaf_certificate)
                # .getSubjectX500Principal().getName())

                return False

            logging.info("TLS client connection established \n\t from link-local address " +
                         str(self.get_client_address()) + " and port " + str(self.get_client_port()) +
                         "\n\t to host " + str(host.gethostname()) + " and port " + str(port))

            return True

        except socket.herror as e:
            logging.error("TLS client connection failed (UnknownHostException)!", e)

        except ssl.SSLError as e:
            logging.error("TLS client connection failed (SSLHandshakeException)", e)

        except socket.timeout as e:
            logging.fatal("TLS client connection failed (SocketTimeoutException) due to session setup timeout", e)

        except IOError as e:
            logging.error("TLS client connection failed (IOException)!", e)

        except TypeError:
            logging.fatal(
                "NullPointerException while trying to set keystores," +
                " resource path to keystore/truststore might be incorrect")

        return False

    def run(self) -> None:
        """
        Run-method of a thread. While the thread is not interrupted, a timeout is set if necessary. Also the incoming
        messages are processed. Exceptions are caught and the thread is stopped at the end
        :return: None
        """
        while not self._interrupt:
            if self.get_timeout() >= 0:
                try:
                    self.get_tls_socket_to_server().settimeout(self.get_timeout())

                    if not self.process_incoming_message():
                        break

                except socket.timeout:
                    self.stop_and_notify("A timeout occurred while waiting for response message", None)
                    break

                except IOError as e2:
                    self.stop_and_notify("An IOException occurred while trying to read message", e2)
                    break

            else:
                self.stop_and_notify("Timeout value is negative: " + str(self.get_timeout()), None)
                break

        self.stop()

    def send(self, message: V2GTPMessage, timeout: int) -> None:
        """
        Message is written to Output-Stream and it is tried to be sent. Possible exceptions are caught
        :param message: V2GTPMessage
        :param timeout: int
        :return: None
        """
        self.set_v2g_tp_message(None)

        try:
            self.get_out_stream().write(message.get_message())
            self.get_out_stream().flush()
            logging.debug("Message sent")
            self.set_timeout(timeout)

        except ssl.SSLError as e1:
            self.stop_and_notify("An SSLHandshakeException occurred", e1)

        except IOError as e2:
            self.stop_and_notify("An undefined IOException occurred while trying to send message", e2)

    def set_tls_socket_to_server(self, tls_socket_to_server) -> None:
        """
        Sets the socket that is connected to the server
        :param tls_socket_to_server:
        :return: None
        """
        self._tls_socket_to_server = tls_socket_to_server

    def stop(self) -> None:
        """
        Checks if stop was already initiated and if not, initiates it. Closes Input Stream, Output Stream and socket and
        sets interrupt-parameter to True. Exceptions are caught
        :return: None
        """
        if not self.is_stop_already_initiated():
            logging.debug("Stopping TLS client ...")
            self.set_stop_already_initiated(True)

            try:
                self.get_in_stream().close()
                self.get_out_stream().close()
                self.get_tls_socket_to_server().close()
                self._interrupt = True

            except IOError as e:
                logging.error("Error occurred while trying to close TCP socket to server", e)

            logging.debug("TLS client stopped")
