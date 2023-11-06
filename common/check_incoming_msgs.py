from iso15118.secc import secc_handler
from iso15118.evcc import evcc_handler
from iso15118.common.exi_utils import exi_utils



def check_incoming_messages(statemachine, client, udpserver, secc_msg_handler, evcc_msg_handler, tcpsock):
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
            self.message_handler.process_message_and_react(
                seccdiscoveryreq_message, address)

        # Check For TCP Messages (AppProtocl or V2G)
        elif self.evcc_client:

            while True:
                data = network.recvall(self.evcc_client)

                if data:
                    self.message_handler.process_message_and_react(data)