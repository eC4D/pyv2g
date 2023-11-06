#######################################################
# 
# ForkState.py
# Python implementation of the Class ForkState
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 11:56:16
# Original author: Fabian.Stichtenoth
# 
#######################################################
from typing import List

from secc.session.V2GCommunicationSessionSECC import V2GCommunicationSessionSECC
from secc.states.ServerState import ServerState
from shared.v2gMessages.msgDef.BodyBaseType import BodyBaseType
from shared.v2gMessages.msgDef.V2GMessage import V2GMessage
from shared.v2gMessages.msgDef.BodyType import BodyType
from shared.v2gMessages.msgDef.ResponseCodeType import ResponseCodeType
from shared.messageHandling.ReactionToIncomingMessage import ReactionToIncomingMessage
from shared.messageHandling.TerminateSession import TerminateSession
from shared.messageHandling.ChangeProcessingState import ChangeProcessingState
from shared.misc.V2GCommunicationSession import V2GCommunicationSession
from shared.enumerations.V2GMessages import V2GMessages


import logging


class ForkState(ServerState):

    def __init__(self, comm_session_context, allowed_requests=None):
        super().__init__(comm_session_context)
        self._allowed_requests = allowed_requests
        self._response_message = 0

    def get_allowed_requests(self) -> List[V2GMessages]:
        """
        Returns the allowed requests
        :return _allowed_requests: List[V2GMessages]
        """
        return self._allowed_requests

    def get_response_message(self):
        """
        Needed for the ForkState to get the respective response message which can be
        used to instantiate a SendMessage() object in case of a sequence error
        :return: None
        """
        return None

    def process_incoming_message(self, message):
        """
        Tries to get the incoming message and catches TypeErrors. Checks that State of the incoming message is not None
        and makes sure that the message is part of the allowed requests. Message is then processed accordingly
        :param message:
        :return: ChangeProcessingState
        """
        v2g_message_req = message

        try:
            incoming_message = V2GMessages.from_value(v2g_message_req.get_body().get_body_element()
                                                      .get_value().__class__.__name__)

        except TypeError:
            return TerminateSession("No valid V2GMessage received")

        new_state = self.get_comm_session_context().get_states().get(incoming_message)

        if new_state is None:
            logging.error("Error occurred while switching from ForkState to a new state: new state is null")

            return TerminateSession("Invalid message (" +
                                    v2g_message_req.get_body().get_body_element().get_value().__class__.__name__ +
                                    ") at this state (" + self.__class__.__name__ + "). " +
                                    "Allowed messages are: " + str(self.get_allowed_requests()))

        if incoming_message in self._allowed_requests:
            self._allowed_requests.clear()
            return ChangeProcessingState(message, new_state)

        else:
            logging.error("Invalid message (" +
                          v2g_message_req.get_body().get_body_element().get_value().__class__.__name__ +
                          ") at this state (" + self.__class__.__name__ + "). " +
                          "Allowed messages are: " + str(self.get_allowed_requests()))

            response_message = self.get_sequence_error_res_message(v2g_message_req)
            new_server_state = new_state

            return new_server_state.get_send_message(
                response_message, V2GMessages.NONE, ResponseCodeType.FAILED_SEQUENCE_ERROR)

    def set_allowed_requests(self, allowed_requests):
        """
        Sets the allowed requests
        :param allowed_requests:
        :return: None
        """
        self._allowed_requests = allowed_requests

    def to_string(self):
        """
        Transforms the allowed requests into one string
        :return allowed_requests: str
        """
        allowed_requests = ""
        for message in self._allowed_requests.get_allowed_requests():
            allowed_requests += message.__class__.__name__ + ", "

        return allowed_requests