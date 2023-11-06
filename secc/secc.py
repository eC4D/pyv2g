"""Module describing the behaviour from the SECC side . The constructor
will instantiate an SECC object, new attributes can be added that simulate
the controller. The SECC object is capable of:
1)Receiving Messages
2)Processing Messages
3)Reacting to Messages
4)Change States
"""
import os
import time
# pylint: disable=import-error
from iso15118.secc import secc_states
from iso15118.secc import secc_config
from iso15118.secc import evsecontroller
from iso15118.common.exi_utils import exi_utils
from iso15118.common.network import network
from iso15118.common.XML import msgbody1, msgdatatypes1
from iso15118.secc.secc_handler import SECCMessageHandler
import cProfile

from iso15118.common.handlers import MessageHandler

path="../"
os.chdir(path)


# pylint: disable=no-member
# pylint: disable=line-too-long
class SECC():
    """Class Repressenting SECC. Stores important attributes that simulate SECC behaviour
    and enables the functionality to receive, process and send messages
    """

    def __init__(self):
        self.udp_port = 15118

        self.ipadress = secc_config.IP_ADRESS
        self.tcp_port = 8081
        self.tls_port = 8082
        self.gen = None
        self.contract_certificate = None
        self.smart_meter_receipt_needed = None
        self.smart_meter_receipt_done = False
        self.udpserver, self.tcpserver = network.create_udp_tcp_serversocket()
        self.tlstcp = None
        self.evcc_client = None
        self.secc_key_path = secc_config.SECC_PRIVATEKEY_PATH
        self.secc_cert_chain = secc_config.SECC_CERTCHAIN_PATH
        self.payment_option = None
        self.controller = evsecontroller.EVSESimController()
        # State Machine for SECC
        res = secc_states.create_secc_state_machine()
        self.statemachine = res[0]
        #self.message_handler = SECCMessageHandler(self)
        self.message_handler = MessageHandler(None, self)

    def display_state(self):
        """Used for logging Porpuses. Displays the state
        """
        print("New State: ", self.statemachine.state)


    def check_incoming_messages(self):
        """Checks for the next incoming message. If the SECC State is WaitForSupportedAppProtocolReq
        the UDP socket will wait for the SDP request message. If the TCP connection with the EVCC
        is established, the method will wait for a V2G Message. After the message has been received
        the process_message_and_react method will be called.

        """
        while True:
            # Check For UDP Messages IF State is WaitForSupportedAppProtocolReq
            if self.statemachine.state == "WaitForSupportedAppProtocolReq" and self.evcc_client is None:
                print("Waiting For SECCDiscoveryReq UDP Message...")
                seccdiscoveryreq_message, address = self.udpserver.recvfrom(1024)
                #self.message_handler.process_message_and_react(seccdiscoveryreq_message, address)
                self.message_handler.process_message_and_react(seccdiscoveryreq_message, False, address)

            # Check For TCP Messages (AppProtocl or V2G)
            elif self.evcc_client:

                while True:
                    data = network.recvall(self.evcc_client)

                    if data:
                        #self.message_handler.process_message_and_react(data)
                        self.message_handler.process_message_and_react(data, False)

    def establish_secc_tcp_connection(self):
        """Establishes TCP connection after sending SECCDiscoveryReq Message.
        IF TLS is used, the SECC will be authorized by the EVCC. For TLS handhsake, SECC
        will offer its SECC certificate chain that leads up to the V2G certificate. In order
        for the SECC to be verified, EVCC's installed V2G certificate has to match with the
        V2G certificate offered by the SECC
        """
        exi_utils.print_colored_red("3: Starting TCP connection")
        try:
            client, address = self.tcpserver.accept()
        except:
            print("An exception occurred")
        exi_utils.print_colored_red(f"3: Connected to {address}")
        exi_utils.print_colored_red(self.tlstcp)
        if self.tlstcp:
            exi_utils.print_colored_red("Establish TLS Connection")

            context = network.create_secc_sll_context(
                server_cert=secc_config.SECC_CERTCHAIN_PATH,
                server_key=secc_config.SECC_PRIVATEKEY_PATH)
            self.evcc_client = context.wrap_socket(client, server_side=True)
            exi_utils.print_colored_red("SSL established")


    def parse_evse_status(self):
        '''Parses the values of the EVSEStatus to the XML format'''
        evsestatus = self.controller.get_evse_status()

        if self.controller.is_DC_mode():
            res =  msgbody1.DC_EVSEStatusType(
            NotificationMaxDelay=evsestatus["NotificationMaxDelay"],
            EVSENotification=evsestatus["EVSENotification"],
            EVSEIsolationStatus=evsestatus["EVSEIsolationStatus"],
            EVSEStatusCode=evsestatus["EVSEStatusCode"])
            res.original_tagname_ = "DC_EVSEStatus"
            return res
        if self.controller.is_AC_mode():
            res= msgdatatypes1.AC_EVSEStatusType(
                NotificationMaxDelay=evsestatus["NotificationMaxDelay"],
                EVSENotification=evsestatus["EVSENotification"],
                RCD=evsestatus["RCD"]
            )
            res.original_tagname_= "AC_EVSEStatus"



if __name__ == '__main__':
    t1_secc=time.time()
    secc = SECC()
    print(f't1_sec = {time.time()-t1_secc}')
    secc.check_incoming_messages()
    #secc.prossecc()
    #cProfile.run('establish_secc_tcp_connection(self)')