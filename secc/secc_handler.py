from common.exi_utils import exi_utils
from common.security import securityutils
from secc.secc_message_sender import SECCMessageSender

class SECCMessageHandler:
    def __init__(self, secc):
        self.secc = secc
        self.message_sender = SECCMessageSender(self.secc)

        self.message_handlers = {
        'supportedAppProtocolReq': self.handle_supported_app_protocol_req,
        'SessionSetupReq': self.handle_session_setup_req,
        'ServiceDiscoveryReq': self.handle_service_discovery_req,
        'ServiceDetailReq': self.handle_service_detail_req,
        'PaymentServiceSelectionReq': self.handle_payment_service_selection_req,
        'CertificateInstallationReq': self.handle_certificate_installation_req,
        'PaymentDetailsReq': self.handle_payment_details_req,
        'AuthorizationReq': self.handle_authorization_req,
        'ChargeParameterDiscoveryReq': self.handle_charge_parameter_discovery_req,
        'CableCheckReq': self.handle_cable_check_req,
        'PreChargeReq': self.handle_pre_charge_req,
        'PowerDeliveryReq': self.handle_power_delivery_req,
        'CurrentDemandReq': self.handle_current_demand_req,
        'ChargingStatusReq': self.handle_charging_status_req,
        'MeteringReceiptReq': self.handle_metering_receipt_req,
        'WeldingDetectionReq': self.handle_welding_detection_req,
        'SessionStopReq': self.handle_session_stop_req,
        }


    def process_message_and_react(self, message, adress=None):
        """Based on the message input, this methods reacts accordingly:
        State transition -> Send next message -> State transition

        Args:
            message (bytes): The received V2GTP Message
            adress : Adress of the sender. This parameter will be used for the UDP response
        """
        msg = exi_utils.receiveAndCheckMessageType(message)
        print("RECEIVED: ")
        print(msg)


        if type(msg) == (bytes):

            self.handle_sdr(message, adress)
        else:
            message_type = exi_utils.check_v2g_message_type(msg)
            handler = self.message_handlers.get(message_type)
            if handler:
                handler(msg)


    def handle_charging_status_req(self, msg):
        print("Received ChargingStatusReq")
        self.secc.statemachine.ChargingStatusReq()
        self.message_sender.send_charging_status_res(msg)
        self.secc.statemachine.send_ChargingStatusRes()
        self.secc.display_state()





    def handle_metering_receipt_req(self, msg):
        print("Received MeteringReceiptReq")
        self.secc.statemachine.MeteringReceiptReq()
        self.message_sender.send_metering_receipt_res(msg)
        self.secc.statemachine.send_MeteringReceiptRes()
        self.secc.display_state()



    def handle_session_stop_req(self, msg):
        print("Received SessionStopReq")
        self.secc.statemachine.SessionStopReq()
        self.message_sender.send_session_stop_res(msg)
        self.secc.statemachine.send_SessionStopRes()
        self.secc.display_state()

    def handle_welding_detection_req(self, msg):
        print("Received WeldingDetectionReq")
        self.secc.statemachine.WeldingDetectionReq()
        self.message_sender.send_welding_detection_res(msg)
        self.secc.statemachine.send_WeldingDetectionRes()
        self.secc.display_state()



    def handle_current_demand_req(self, msg):
        print("Received CurrentDemandReq")
        self.secc.statemachine.CurrentDemandReq()
        self.message_sender.send_current_demand_res(msg)
        if msg.get_Body().BodyElement.ChargingComplete:
            self.secc.statemachine.send_CurrentDemandRes()
        else:
            self.secc.statemachine.send_CurrentDemandResNoReceipt()
        self.secc.display_state()



    def handle_authorization_req(self, msg):
        print("Received AuthorizationReq")
            # AuthorizationReq <-> AuthorizationRes loop that ends when EVSEProcessing=Finished
        self.secc.statemachine.AuthorizationReq()
        self.message_sender.send_authorization_res(msg)

        self.secc.display_state()

    def handle_charge_parameter_discovery_req(self, msg):
        print("Received ChargeParameterDiscoveryReq")
            #Checking the request to see if DC or AC and instantiate controller
        if "DC" in msg.get_Body().BodyElement.RequestedEnergyTransferMode:
            self.secc.controller.set_to_dc_charging()
        elif "AC" in msg.get_Body().BodyElement.RequestedEnergyTransferMode:
            self.secc.controller.set_to_ac_charging()

        self.secc.statemachine.ChargeParameterDiscoveryReq()
        self.message_sender.send_charge_parameter_discovery_res(msg)

    def handle_payment_details_req(self, msg):
        print("Received PaymentDetailsReq")
        self.secc.statemachine.PaymentDetailsReq()
        self.message_sender.send_payment_details_res(msg)
        cert = msg.get_Body().BodyElement.ContractSignatureCertChain.Certificate
        self.secc.contract_certificate = securityutils.load_pem_certificate(
                cert)
        self.secc.statemachine.send_PaymentDetailsRes()
        self.secc.display_state()

    def handle_certificate_installation_req(self, msg):
        print("Received CertificateInstallationReq")
        self.secc.statemachine.CertificateInstallationReq()
            # Verify Signature
        securityutils.verify_certificate_installation_req(msg)
        self.message_sender.send_certificate_installation_res(msg)
        self.secc.statemachine.send_CertificateInstallationRes()
        self.secc.display_state()

    def handle_payment_service_selection_req(self, msg):
        print("Received PaymentServiceSelectionReq")
            #If payment option is External Payment, skip to AuthorizationReq/Res message set
        self.secc.payment_option = msg.get_Body().BodyElement.SelectedPaymentOption

        self.secc.statemachine.ServicePaymentSelectionReq()
        self.message_sender.send_payment_service_selection_res(msg)
        self.secc.statemachine.send_ServicePaymentSelectionRes()
        self.secc.display_state()

    def handle_service_detail_req(self, msg):
        print("Received ServiceDetailReq")
        self.secc.statemachine.ServiceDetailReq()
        self.message_sender.send_service_detail_res(msg)
        self.secc.statemachine.send_ServiceDetailRes()
        self.secc.display_state()

    def handle_service_discovery_req(self, msg):
        print("Received ServiceDiscoveryReq")
        self.secc.statemachine.ServiceDiscoveryReq()
        self.message_sender.send_service_discovery_res(msg)
        self.secc.statemachine.send_ServiceDiscoveryRes()
        self.secc.display_state()

    def handle_session_setup_req(self,msg):
        print("Received SessionSetupReq")
            # Change state
        self.secc.statemachine.SessionSetupReq()
            # Prepare and send SessionSetupRes
        self.message_sender.send_session_setup_res()
        self.secc.statemachine.send_SessionSetupRes()
        self.secc.display_state()

    def handle_supported_app_protocol_req(self, msg):
        print("Received supportedAppProtocolReq")
            # Change state
        self.secc.statemachine.supportedAppProtocolReq()
            # Prepare and send supportedAppProtocolRes
        self.message_sender.send_supported_app_protocol_res(msg)
        self.secc.statemachine.send_supportedAppProtocolRes()
        self.secc.display_state()

    def handle_sdr(self, message, adress):
        print("Received SECCDiscoveryReq")

            # Process SECCDiscoveryReq
        payload = message[8:]
        if (payload[0] == 0 and payload[1] == 0):
            self.secc.tlstcp = True

            # After Processing prepare and send the SECCDiscoveryRes message
        self.message_sender.send_secc_discovery_res(message, adress)

            # Establish TCP Connection
        self.secc.establish_secc_tcp_connection()



    def handle_power_delivery_req(self, msg):
        print("Received PowerDeliveryReq")
        self.secc.statemachine.PowerDeliveryReq()
        self.message_sender.send_power_delivery_res(msg)
        if msg.get_Body().BodyElement.ChargeProgress == 'Stop':
            exi_utils.print_colored_red("STOP Charging")

            self.secc.statemachine.send_PowerDeliveryResStop()
        elif  self.secc.controller.is_DC_mode():
            self.secc.statemachine.send_PowerDeliveryResDC()
        else:
            self.secc.statemachine.send_PowerDeliveryRes()
        self.secc.display_state()

    def handle_pre_charge_req(self, msg):
        print("Received PrechargeReq")
        self.secc.statemachine.PreChargeReq()
        self.message_sender.send_pre_charge_res(msg)
        self.secc.statemachine.send_PrechargeRes()
        self.secc.display_state()

    def handle_cable_check_req(self, msg):
        print("Received CableCheckReq")
        self.secc.statemachine.CableCheckReq()
        self.message_sender.send_cable_check_res(msg)

        self.secc.display_state()