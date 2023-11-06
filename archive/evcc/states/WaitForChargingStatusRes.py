#######################################################
# 
# WaitForChargingStatusRes.py
# Python implementation of the Class WaitForChargingStatusRes
# Generated by Enterprise Architect
# Created on:      07-Jan-2021 11:15:29
# Original author: Fabian.Stichtenoth
# 
#######################################################
from shared.messageHandling.ReactionToIncomingMessage import ReactionToIncomingMessage
from shared.messageHandling.TerminateSession import TerminateSession
from shared.v2gMessages.msgDef.ChargingStatusResType import ChargingStatusResType
from shared.v2gMessages.msgDef.ChargingStatusReqType import ChargingStatusReqType
from shared.v2gMessages.msgDef.MeteringReceiptReqType import MeteringReceiptReqType
from shared.v2gMessages.msgDef.V2GMessage import V2GMessage
from shared.v2gMessages.msgDef.ChargeProgressType import ChargeProgressType
from shared.misc.State import State
from shared.utils.SecurityUtils import SecurityUtils
from shared.enumerations.GlobalValues import GlobalValues
from shared.enumerations.V2GMessages import V2GMessages
from evcc.session.V2GCommunicationSessionEVCC import V2GCommunicationSessionEVCC
from evcc.states.ClientState import ClientState
from evcc.evController.IACEVController import IACEVController


class WaitForChargingStatusRes(ClientState):

    def __init__(self, comm_session_context: V2GCommunicationSessionEVCC):
        super().__init__(comm_session_context)

    def default(self):
        """
        Default method of Switcher
        :return: method call get_send_message
        """
        if self.get_comm_session_context().get_ev_controller().is_charging_loop_active():
            charging_status_req = ChargingStatusReqType()
            return self.get_send_message(charging_status_req, V2GMessages.CHARGING_STATUS_RES)

        else:
            self.get_comm_session_context().set_stop_charging_requested(True)
            return self.get_send_message(
                self.get_power_delivery_req(ChargeProgressType.STOP), V2GMessages.POWER_DELIVERY_RES,
                " (ChargeProgress = STOP_CHARGING)"
            )

    def stop(self):
        """
        Stop charging method of Switcher
        :return: method call get_send_message
        """
        self.get_comm_session_context().set_stop_charging_requested(True)
        return self.get_send_message(self.get_power_delivery_req(ChargeProgressType.STOP),
                                     V2GMessages.POWER_DELIVERY_RES, " (ChargeProgress = STOP_CHARGING)"
                                     )

    def re(self):
        """
        Renegotiation method of Switcher
        :return: method call get_send_message
        """
        return self.get_send_message(self.get_power_delivery_req(ChargeProgressType.RENEGOTIATE),
                                     V2GMessages.POWER_DELIVERY_RES, " (ChargeProgress = RE_NEGOTIATION)"
                                     )

    def process_incoming_message(self, message) -> ReactionToIncomingMessage:
        """
        Initiates check if message is valid. If so, checks if receipt is required and if it is TLS. If so, metering
        receipt request is created and prepared to get sent. Switcher is called dependent on charge progress. If there's
        an failure, session gets terminated
        :param message:
        :return: ReactionToIncomingMessage
        """
        if self.is_incoming_message_valid(message, ChargingStatusResType.__class__):
            v2g_message_res: V2GMessage = message
            charging_status_res: ChargingStatusResType = v2g_message_res.get_body().get_body_element().get_value()

            if charging_status_res.is_receipt_required() and self.get_comm_session_context().is_tls_connection():
                metering_receipt_req: MeteringReceiptReqType = MeteringReceiptReqType()
                metering_receipt_req.set_id("id1")
                metering_receipt_req.set_meter_info(charging_status_res.get_sa_schedule_tuple_id())
                metering_receipt_req.set_session_id(self.get_comm_session_context().get_session_id())

                self.get_xml_signature_ref_elements()[metering_receipt_req.get_id()] = SecurityUtils.generate_digest(
                    metering_receipt_req.get_id(), self.get_message_handler().get_jaxb_element(metering_receipt_req))

                self.set_signature_private_key(SecurityUtils.get_private_key(
                    SecurityUtils.get_keystore(
                        str(GlobalValues.EVCC_KEYSTORE_FILEPATH),
                        str(GlobalValues.PASSPHRASE_FOR_CERTIFICATES_AND_KEYS)
                    ), str(GlobalValues.ALIAS_CONTRACT_CERTIFICATE)
                )
                )

                return self.get_send_message(metering_receipt_req, V2GMessages.METERING_RECEIPT_REQ)

            if charging_status_res.get_evse_max_current() is not None:
                self.get_comm_session_context().get_ev_controller().adjust_max_current(
                    charging_status_res.get_evse_max_current())

            switcher = {
                "STOP_CHARGING": "stop",
                "RE_NEGOTIATION": "re",
            }

            func = switcher.get(
                charging_status_res.get_ac_evse_status().get_evse_notification(), lambda: self.default())
            return func()

        else:
            TerminateSession("Incoming message raised an error")