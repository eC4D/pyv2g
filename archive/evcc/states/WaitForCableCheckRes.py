#######################################################
# 
# WaitForCableCheckRes.py
# Python implementation of the Class WaitForCableCheckRes
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 11:13:42
# Original author: Fabian.Stichtenoth
# 
#######################################################
import logging
import time

from shared.messageHandling.ReactionToIncomingMessage import ReactionToIncomingMessage
from shared.messageHandling.TerminateSession import TerminateSession
from shared.v2gMessages.msgDef.CableCheckResType import CableCheckResType
from shared.v2gMessages.msgDef.V2GMessage import V2GMessage
from shared.v2gMessages.msgDef.EVSEProcessingType import EVSEProcessingType
from shared.v2gMessages.msgDef.PreChargeReqType import PreChargeReqType
from shared.enumerations.V2GMessages import V2GMessages
from shared.misc.TimeRestrictions import TimeRestrictions
from evcc.session.V2GCommunicationSessionEVCC import V2GCommunicationSessionEVCC
from evcc.states.ClientState import ClientState
from evcc.evController.IDCEVController import IDCEVController


class WaitForCableCheckRes(ClientState):

    def __init__(self, comm_session_context: V2GCommunicationSessionEVCC):
        super().__init__(comm_session_context)

    def process_incoming_message(self, message) -> ReactionToIncomingMessage:
        """
        Initiates check if message is valid. If so, processes message dependent on the Processing Type. Type can be
        FINISHED or ONGOING. If something goes wrong, Session is terminated.
        :param message:
        :return: ReactionToIncomingMessage
        """
        if self.is_incoming_message_valid(message, CableCheckResType.__class__):
            v2g_message_res: V2GMessage = message
            cable_check_res: CableCheckResType = v2g_message_res.get_body().get_body_element().get_value()

            if cable_check_res.get_evse_processing() == EVSEProcessingType.FINISHED:
                logging.debug("EVSEProcessing was set to FINISHED")

                dc_ev_controller: IDCEVController = self.get_comm_session_context().get_ev_controller()

                pre_charge_req: PreChargeReqType = PreChargeReqType()
                pre_charge_req.set_dc_ev_status(dc_ev_controller.get_dc_ev_status())
                pre_charge_req.set_ev_target_current(dc_ev_controller.get_target_current())
                pre_charge_req.set_ev_target_voltage(dc_ev_controller.get_target_voltage())

                self.get_comm_session_context().set_ongoing_timer(time.time_ns())
                self.get_comm_session_context().set_ongoing_timer_active(True)

                return self.get_send_message(pre_charge_req, V2GMessages.PRE_CHARGE_RES)

            else:
                logging.debug("EVSEProcessing was set to ONGOING")

                elapsed_time_in_ms = 0

                if self.get_comm_session_context().is_ongoing_timer_active:
                    elapsed_time = time.time_ns() - self.get_comm_session_context().get_ongoing_timer()
                    elapsed_time_in_ms = elapsed_time / 1000000

                    if elapsed_time_in_ms > TimeRestrictions.V2G_EVCC_CABLE_CHECK_TIMEOUT:
                        return TerminateSession("CableCheck timer timed out for CableCheckReq")

                else:
                    self.get_comm_session_context().set_ongoing_timer(time.time_ns())
                    self.get_comm_session_context().set_ongoing_timer_active(True)

                return self.get_send_message(self.get_cable_check_req(), V2GMessages.CABLE_CHECK_RES,
                                             min(TimeRestrictions.V2G_EVCC_CABLE_CHECK_TIMEOUT - elapsed_time_in_ms,
                                                 TimeRestrictions.get_v2g_evcc_msg_timeout(
                                                     V2GMessages.CABLE_CHECK_RES)))
        else:
            return TerminateSession("Incoming message raised an error")
