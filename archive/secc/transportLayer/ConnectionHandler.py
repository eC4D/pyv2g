#######################################################
# 
# ConnectionHandler.py
# Python implementation of the Class ConnectionHandler
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 12:06:12
# Original author: Fabian.Stichtenoth
# 
#######################################################
import logging
import threading
import socket
import requests
import io
import sys

from shared.misc.V2GTPMessage import V2GTPMessage
from shared.misc.TimeRestrictions import TimeRestrictions


class ConnectionHandler:

    def __init__(self, client_socket, socket_type):
        self._address = ""
        self._bytes_read_from_input_stream = 0
        self._in_stream = None
        self._out_stream = io.BytesIO(b"")
        self._payload_length = 0
        self._port = 0
        self._stop_already_initiated = False
        self._tcp_client_socket = None
        self._tls_client_socket = None
        self._v2g_tp_header = bytearray()
        self._v2g_tp_message = bytearray()
        self._v2g_tp_payload = bytearray()
        self._mask = 0x80  # in Java MASK is final -> don't modify it!
        self._interrupt = False
        self.subscribers = set()

        if socket_type == "tcp":
            self.set_tcp_client_socket(client_socket)

            try:
                # TODO: not sure if next two lines are correct
                self.set_in_stream(self.get_tcp_client_socket().listen(5))
                self.set_out_stream(self.get_tcp_client_socket())
                self.set_v2g_tp_header(bytearray(8))
            except Exception as e:
                self.__stop_and_notify("An IOException was thrown while creating streams from TCP client socket", e)

        elif socket_type == "tls":
            self.set_tls_client_socket(client_socket)

            try:
                # TODO: not sure if next two lines are correct
                self.set_in_stream(self.get_tls_client_socket().listen(5))
                self.set_out_stream(self.get_tls_client_socket())
                self.set_v2g_tp_header(bytearray(8))
            except IOError as e:
                self.__stop_and_notify("An IOException was thrown while creating streams from TLS client socket", e)

    # TODO: is implementation of Observer pattern correct?
    def register(self, who):
        """
        Register (addObserver) method of Observer pattern
        :param who:
        :return: None
        """
        self.subscribers.add(who)

    def unregister(self, who):
        """
        Unregister (deleteObserver) method of Observer pattern
        :param who:
        :return: None
        """
        self.subscribers.discard(who)

    def dispatch(self, obj):
        """
        Dispatch method of Observer pattern. Calls update method in the subscriber class and makes reaction possible
        :return: None
        """
        for subscriber in self.subscribers:
            subscriber.update(obj)

    def get_address(self):
        """
        Returns the _address
        :return _address: str
        """
        return self._address

    def get_bytes_read_from_input_stream(self):
        """
        Returns the _bytes_read_from_input_stream
        :return _bytes_read_from_input_stream: int
        """
        return self._bytes_read_from_input_stream

    def get_in_stream(self):
        """
        Returns the _in_stream
        :return _in_stream:
        """
        return self._in_stream

    def get_out_stream(self):
        """
        Returns the _out_stream
        :return _out_stream:
        """
        return self._out_stream

    def get_payload_length(self):
        """
        Returns the _payload_length
        :return _payload_length: int
        """
        return self._payload_length

    def get_port(self):
        """
        Returns the _port
        :return _port: int
        """
        return self._port

    def get_tcp_client_socket(self):
        """
        Returns the _tcp_client_socket
        :return _tcp_client_socket:
        """
        return self._tcp_client_socket

    def get_tls_client_socket(self):
        """
        Returns the _tls_client_socket
        :return _tls_client_socket:
        """
        return self._tls_client_socket

    def get_v2g_tp_header(self):
        """
        Returns the _v2g_tp_header
        :return _v2g_tp_header: bytearray
        """
        return self._v2g_tp_header

    def get_v2g_tp_message(self):
        """
        Returns the _v2g_tp_message
        :return _v2g_tp_message: bytearray
        """
        return self._v2g_tp_message

    def get_v2g_tp_payload(self):
        """
        Returns the _v2g_tp_payload
        :return _v2g_tp_payload: bytearray
        """
        return self._v2g_tp_payload

    def get_is_stop_already_initiated(self):
        """
        Returns the _stop_already_initiated that indicates if stop was initiated
        :return _stop_already_initiated: bool
        """
        return self._stop_already_initiated

    def run(self):
        """
        Checks if session was interrupted. If not checks for tcp or tls and reads bytes from input stream. Checks if
        payload length of message is correct and finally logs that the message was received. Exceptions are caught
        :return: None
        """
        while not self._interrupt:

            try:
                if self.get_tcp_client_socket() is not None:
                    self.get_tcp_client_socket().settimeout(TimeRestrictions.V2G_SECC_SEQUENCE_TIMEOUT)
                elif self.get_tls_client_socket() is not None:
                    self.get_tls_client_socket().settimeout(TimeRestrictions.V2G_SECC_SEQUENCE_TIMEOUT)
                else:
                    logging.error("Neither TCP nor TLS client socket available")
                    self._interrupt = True

                self.set_bytes_read_from_input_stream(self.get_in_stream().read(self.get_v2g_tp_header()))

                if self._bytes_read_from_input_stream < 0:
                    self.__stop_and_notify("No bytes read from input stream, client socket seems to be closed", None)
                    break

                if self.get_v2g_tp_header()[4] == self._mask \
                        and self._mask == self._mask:
                    self.__stop_and_notify("Payload length of V2GTP message is inappropriately high! "
                                           "There must be an error in the V2GTP message header!", None)
                    break
                else:
                    self.set_payload_length(int.from_bytes(ConnectionHandler.get_v2g_tp_header[4:8], byteorder='big'))
                    byte = bytearray(self._payload_length)
                    self.set_v2g_tp_payload(byte)

                    self.get_in_stream().read(self.get_v2g_tp_payload())

                    byte = bytearray((len(self.get_v2g_tp_header()) + len(self.get_v2g_tp_payload())))
                    self.set_v2g_tp_message(byte)
                    self.arrayCopy(self.get_v2g_tp_header(), 0, self.get_v2g_tp_message(), 0, len(
                        self.get_v2g_tp_header()))
                    self.arrayCopy(self.get_v2g_tp_payload(), 0, self.get_v2g_tp_message(), len(
                        self.get_v2g_tp_header()),
                                   len(self.get_v2g_tp_payload()))

                    logging.debug("Message received")

                    # TODO: not sure if implementation of the following line is correct
                    self.dispatch(self.get_v2g_tp_message())

            except socket.timeout:
                self.__stop_and_notify("A SocketTimeoutException occurred", None)
                break
            except requests.exceptions.SSLError as e1:
                self.__stop_and_notify("An SSLHandshakeException occurred", e1)
                break
            except IOError as e2:
                self.__stop_and_notify("IOException occurred", e2)
                break
        pass

    @staticmethod
    def arrayCopy(src, srcPos, dest, destPos, length):
        """
        Copies content of array src beginning from srcPos to dest starting at destPos for length length
        :param src:
        :param srcPos:
        :param dest:
        :param destPos:
        :param length:
        :return: None
        """
        for i in range(length):
            dest[i + destPos] = src[i + srcPos]
        pass

    def send(self, message: V2GTPMessage):
        """
        Writes to the output stream and sends all that was written
        :param message:
        :return: bool
        """
        try:
            self.get_out_stream().write(message.get_message())
            self.get_out_stream().flush()
        except IOError as e:
            logging.error("Error occurred while trying to send V2GTPMessage (IOException)!", e)

        logging.debug("Message sent")

        return False

    def set_address(self, address):
        """
        Sets the _address
        :param address:
        :return: None
        """
        self._address = address
        pass

    def set_bytes_read_from_input_stream(self, bytes_read_from_input_stream):
        """
        Sets the _bytes_read_from_input_stream
        :param bytes_read_from_input_stream:
        :return: None
        """
        self._bytes_read_from_input_stream = bytes_read_from_input_stream
        pass

    def set_in_stream(self, in_stream):
        """
        Sets the _in_stream
        :param in_stream:
        :return: None
        """
        self._in_stream = in_stream
        pass

    def set_out_stream(self, out_stream):
        """
        Sets the _out_stream
        :param out_stream:
        :return: None
        """
        self._out_stream = out_stream
        pass

    def set_payload_length(self, payload_length):
        """
        Sets the _payload_length
        :param payload_length:
        :return: None
        """
        self._payload_length = payload_length
        pass

    def set_port(self, port):
        """
        Sets the _port
        :param port:
        :return: None
        """
        self._port = port
        pass

    def set_is_stop_already_initiated(self, stop_already_initiated):
        """
        Sets the _stop_already_initiated
        :param stop_already_initiated:
        :return: None
        """
        self._stop_already_initiated = stop_already_initiated
        pass

    def set_tcp_client_socket(self, tcp_client_socket):
        """
        Sets the _tcp_client_socket, gets the address of it as well as the port
        :param tcp_client_socket:
        :return: None
        """
        self._tcp_client_socket = tcp_client_socket
        self.set_address(tcp_client_socket.getsockname()[0])
        self.set_port(tcp_client_socket.getsockname()[1])
        pass

    def set_tls_client_socket(self, tls_client_socket):
        """
        Sets the _tls_client_socket, gets the address of it as well as the port
        :param tls_client_socket:
        :return: None
        """
        self._tls_client_socket = tls_client_socket
        self.set_address(tls_client_socket.getsockname()[0])
        self.set_port(tls_client_socket.getsockname()[1])
        pass

    def set_v2g_tp_header(self, v2g_tp_header):
        """
        Sets the _v2g_tp_header
        :param v2g_tp_header:
        :return: None
        """
        self._v2g_tp_header = v2g_tp_header
        pass

    def set_v2g_tp_message(self, v2g_tp_message):
        """
        Sets the _v2g_tp_message
        :param v2g_tp_message:
        :return: None
        """
        self._v2g_tp_message = v2g_tp_message
        pass

    def set_v2g_tp_payload(self, v2g_tp_payload):
        """
        Sets the _v2g_tp_payload
        :param v2g_tp_payload:
        :return: None
        """
        self._v2g_tp_payload = v2g_tp_payload
        pass

    def stop(self):
        """
        Checks if stop was already initiated and if not sets the parameter to True. Closes the input and output stream
        as well as the sockets
        :return: None
        """
        if not self.get_is_stop_already_initiated():
            logging.debug("Closing connection to client ...")
            self.set_is_stop_already_initiated(True)

            try:
                self.get_in_stream().close()
                self.get_out_stream().close()

                if self.get_tcp_client_socket() is not None:
                    self.get_tcp_client_socket().close()
                elif self.get_tls_client_socket() is not None:
                    self.get_tls_client_socket().close()
                else:
                    logging.error("Neither TCP nor TLS client socket could be closed")

                self._interrupt = True
                logging.debug("Connection to client closed")

            except IOError as e:
                logging.error("Error occurred while trying to close socket to client", e)
        pass

    def __stop_and_notify(self, error_message, e):
        """If an error occurred in the run()-method, the client will be stopped by closing
        all streams and the socket and interrupting the Thread.
        V2GCommunicationSessionSECC will be notified as well. The method's statements
        will not be executed if a stop of the client has already been initiated by the
        V2GCommunicationSessionSECC (which might induce an error in the run()-method).
        :return: None
        """
        if not self.get_is_stop_already_initiated():
            logging.error(error_message, e)
            self.stop()

            # TODO: not sure if implementation of the following line is correct
            self.dispatch(None)
        pass
