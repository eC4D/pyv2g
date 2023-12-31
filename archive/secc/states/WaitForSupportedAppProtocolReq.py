#######################################################
# 
# WaitForSupportedAppProtocolReq.py
# Python implementation of the Class WaitForSupportedAppProtocolReq
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 12:01:35
# Original author: Fabian.Stichtenoth
# 
#######################################################
import logging

from shared.v2gMessages.appProtocol.SupportedAppProtocolRes import SupportedAppProtocolRes
from shared.v2gMessages.appProtocol.SupportedAppProtocolReq import SupportedAppProtocolReq
from shared.v2gMessages.appProtocol.AppProtocolType import AppProtocolType
from shared.v2gMessages.msgDef.BodyBaseType import BodyBaseType
from shared.v2gMessages.msgDef.ResponseCodeType import ResponseCodeType
from shared.v2gMessages.SECCDiscoveryReq import SECCDiscoveryReq
from shared.messageHandling.ReactionToIncomingMessage import ReactionToIncomingMessage
from shared.enumerations.GlobalValues import GlobalValues
from shared.enumerations.V2GMessages import V2GMessages
from shared.messageHandling.ChangeProcessingState import ChangeProcessingState
from secc.session.V2GCommunicationSessionSECC import V2GCommunicationSessionSECC
from secc.states.ServerState import ServerState


class WaitForSupportedAppProtocolReq(ServerState):

    def __init__(self, comm_session_context: V2GCommunicationSessionSECC):
        super().__init__(comm_session_context)
        self._supported_app_protocol_res = None

    def get_response_message(self):
        """
        Returns the _supported_app_protocol_res
        :return _supported_app_protocol_res:
        """
        return self._supported_app_protocol_res

    @staticmethod
    def __get_supported_app_protocols():
        """All supported versions of the ISO/IEC 15118-2 protocol are listed here.
        Currently, only IS version of April 2014 is supported (see [V2G2-098]), more
        could be provided here. The values for priority and schema ID do not need to be
        set since these values are provided by the EVCC.
        :return supported_app_protocols: A list of supported of AppProtocol entries
        """
        supported_app_protocols = []

        app_protocol1 = AppProtocolType()
        app_protocol1.set_protocol_namespace(str(GlobalValues.V2G_CI_MSG_DEF_NAMESPACE))
        app_protocol1.set_version_number_major(2)
        app_protocol1.set_version_number_minor(0)

        supported_app_protocols.append(app_protocol1)

        return supported_app_protocols

    def process_incoming_message(self, message) -> ReactionToIncomingMessage:
        """
        Checks if message is of instance SupportedAppProtocolReq and if so, acts according to it. Gets supported app
        protocols and checks that evcc-side and secc-side match. If so, negotiation was successful. If message is of
        instance SECCDiscoveryReq, state is changed to WaitForSECCDiscoveryReq. Else message is not valid
        :param message:
        :return: ReactionToIncomingMessage
        """
        self._supported_app_protocol_res = SupportedAppProtocolRes()

        if isinstance(message, SupportedAppProtocolReq):
            logging.debug("SupportedAppProtocolReq received")
            match = False
            response_code = ResponseCodeType.FAILED_NO_NEGOTIATION
            supported_app_protocol_req = message

            supported_app_protocol_req.get_app_protocol().sort(key=lambda x: x.get_priority())

            for evcc_app_protocol in supported_app_protocol_req.get_app_protocol():
                for secc_app_protocol in self.__get_supported_app_protocols():
                    if evcc_app_protocol.get_protocol_namespace() == secc_app_protocol.get_protocol_namespace() \
                            and evcc_app_protocol.get_version_number_major() == secc_app_protocol. \
                            get_version_number_major():
                        if evcc_app_protocol.get_version_number_minor() == secc_app_protocol.get_version_number_minor():
                            response_code = ResponseCodeType.OK_SUCCESSFUL_NEGOTIATION

                        else:
                            response_code = ResponseCodeType.OK_SUCCESSFUL_NEGOTIATION_WITH_MINOR_DEVIATION

                        match = True
                        self._supported_app_protocol_res.set_schema_id(evcc_app_protocol.get_schema_id())
                        break

                if match:
                    break

            self._supported_app_protocol_res.set_response_code(response_code)

        elif isinstance(message, SECCDiscoveryReq):
            logging.debug("Another SECCDiscoveryReq was received, changing to state WaitForSECCDiscoveryReq")
            return ChangeProcessingState(message, self.get_comm_session_context().get_states().get(
                V2GMessages.SECC_DISCOVERY_REQ))

        elif message is not None:
            logging.error("Invalid message (" + message.__class__.__name__ +
                          ") at this state (" + self.__class__.__name__ + ")")
            self._supported_app_protocol_res.set_response_code(ResponseCodeType.FAILED_NO_NEGOTIATION)

        else:
            logging.error("Invalid message at this state, message seems to be null. Check if same XSD schema is used "
                          "on EVCC side.")
            self._supported_app_protocol_res.set_response_code(ResponseCodeType.FAILED_NO_NEGOTIATION)

        if str(self._supported_app_protocol_res.get_response_code()).startswith("OK"):
            v2g_mes = V2GMessages.SESSION_SETUP_REQ

        else:
            v2g_mes = V2GMessages.NONE

        return self.get_send_message(self._supported_app_protocol_res, v2g_mes,
                                     self._supported_app_protocol_res.get_response_code())
