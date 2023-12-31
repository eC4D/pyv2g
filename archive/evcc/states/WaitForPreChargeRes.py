#######################################################
# 
# WaitForPreChargeRes.py
# Python implementation of the Class WaitForPreChargeRes
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 11:17:02
# Original author: Fabian.Stichtenoth
# 
#######################################################
import time

from shared.messageHandling.ReactionToIncomingMessage import ReactionToIncomingMessage
from shared.messageHandling.TerminateSession import TerminateSession
from shared.v2gMessages.msgDef.PreChargeResType import PreChargeResType
from shared.v2gMessages.msgDef.PreChargeReqType import PreChargeReqType
from shared.v2gMessages.msgDef.ChargeProgressType import ChargeProgressType
from shared.v2gMessages.msgDef.V2GMessage import V2GMessage
from shared.enumerations.V2GMessages import V2GMessages
from shared.misc.TimeRestrictions import TimeRestrictions
from evcc.session.V2GCommunicationSessionEVCC import V2GCommunicationSessionEVCC
from evcc.states.ClientState import ClientState
from evcc.evController.IDCEVController import IDCEVController


class WaitForPreChargeRes(ClientState):

    def __init__(self, comm_session_context: V2GCommunicationSessionEVCC):
        super().__init__(comm_session_context)

    def process_incoming_message(self, message) -> ReactionToIncomingMessage:
        """
        Initiates check if message is valid. If so, checks if target voltage and current voltage are equal. If not,
        adjusts ev target voltage and current. If there's an failure, session is terminated
        :param message:
        :return: ReactionToIncomingMessage
        """
        if self.is_incoming_message_valid(message, PreChargeResType.__class__):
            v2g_message_res: V2GMessage = message
            pre_charge_res: PreChargeResType = v2g_message_res.get_body().get_body_element().get_value()

            dc_ev_controller = self.get_comm_session_context().get_ev_controller()
            target_voltage = dc_ev_controller.get_target_voltage().get_value() * pow(
                10, dc_ev_controller.get_target_voltage().get_multiplier())
            present_voltage = pre_charge_res.get_evse_present_voltage().get_value() * pow(
                10, pre_charge_res.get_evse_present_voltage().get_multiplier())

            if target_voltage == present_voltage:
                self.get_comm_session_context().set_ongoing_timer_active(False)
                self.get_comm_session_context().set_ongoing_timer(0)

                return self.get_send_message(self.get_power_delivery_req(ChargeProgressType.START),
                                             V2GMessages.POWER_DELIVERY_RES)

            else:
                elapsed_time = time.time_ns() - self.get_comm_session_context().get_ongoing_timer()
                elapsed_time_in_ms = elapsed_time / 1000000

                if elapsed_time_in_ms > TimeRestrictions.V2G_EVCC_PRE_CHARGE_TIMEOUT:
                    return TerminateSession("PreCharge timer timed out for PreChargeReq")

                else:
                    pre_charge_req = PreChargeReqType()
                    pre_charge_req.set_dc_ev_status(dc_ev_controller.get_dc_ev_status())
                    pre_charge_req.set_ev_target_current(dc_ev_controller.get_target_current())
                    pre_charge_req.set_ev_target_voltage(dc_ev_controller.get_target_voltage())

                    return self.get_send_message(pre_charge_req, V2GMessages.PRE_CHARGE_RES, min(
                        TimeRestrictions.V2G_EVCC_PRE_CHARGE_TIMEOUT - elapsed_time_in_ms,
                        TimeRestrictions.get_v2g_evcc_msg_timeout(V2GMessages.PRE_CHARGE_RES)
                    ))

        else:
            return TerminateSession("Incoming message raised an error")
