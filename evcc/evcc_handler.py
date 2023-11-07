from common.exi_utils import exi_utils
from common.security import securityutils
from evcc.evcc_message_sender import EVCCMessageSender


class EVCCMessageHandler:
    def __init__(self, evcc):
        self.evcc = evcc
        self.message_sender = EVCCMessageSender(self.evcc)

        self.message_handlers = {
            'supportedAppProtocolRes': self.handle_supported_app_protocol_res,
            'SessionSetupRes': self.handle_session_setup_res,
            'ServiceDiscoveryRes': self.handle_service_discovery_res,
            'ServiceDetailRes': self.handle_service_detail_res,
            'PaymentServiceSelectionRes': self.handle_payment_service_selection_res,
            'CertificateInstallationRes': self.handle_certificate_installation_res,
            'PaymentDetailsRes': self.handle_payment_details_res,
            'AuthorizationRes': self.handle_authorization_res,
            'ChargeParameterDiscoveryRes': self.handle_charge_parameter_discovery_res,
            'CableCheckRes': self.handle_cable_check_res,
            'PreChargeRes': self.handle_pre_charge_res,
            'PowerDeliveryRes': self.handle_power_delivery_res,
            'CurrentDemandRes': self.handle_current_demand_res,
            'ChargingStatusRes': self.handle_charging_status_res,
            'MeteringReceiptRes': self.handle_metering_receipt_res,
            'WeldingDetectionRes': self.handle_welding_detection_res,
            'SessionStopRes': self.handle_session_stop_res,
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

        if type(msg) == bytes:

            self.handle_secc_discovery_res(msg)
        else:
            message_type = exi_utils.check_v2g_message_type(msg)
            handler = self.message_handlers.get(message_type)
            if handler:
                handler(msg)

    def handle_secc_discovery_res(self, msg):
        # print("New State: ", self.evcc.statemachine.state)
        #     # Processing SECCDiscoveryRes
        #
        # ip1 = int.from_bytes(msg[0:4], 'big')
        # ip2 = int.from_bytes(msg[4:8], 'big')
        # ip3 = int.from_bytes(msg[8:12], 'big')
        # ip4 = int.from_bytes(msg[12:16], 'big')
        #
        # ipadress = str(ip1) + "." + str(ip2) + "." + \
        #         str(ip3) + "." + str(ip4)
        # port = int.from_bytes(msg[16:18], "big")
        #
        #     # Establishing TCP Connection with SECC (TLS if requested)
        # self.evcc.establish_evcc_tcp_connection(ipadress, port)
        #
        #     #Prepare and send supportedAppProtocolReq
        # self.message_sender.send_supported_app_protocol_req()
        #
        # self.evcc.statemachine.send_supportedAppProtocolReq()
        # self.evcc.display_state()
        print("New State:", self.evcc.statemachine.state)

        ip_address = ".".join(str(int.from_bytes(msg[i:i + 4], 'big')) for i in range(0, 16, 4))
        port = int.from_bytes(msg[16:18], "big")

        self.evcc.establish_evcc_tcp_connection(ip_address, port)

        self.message_sender.send_supported_app_protocol_req()

        self.evcc.statemachine.send_supportedAppProtocolReq()
        self.evcc.display_state()

    def handle_payment_details_res(self, msg):
        print("Received PaymentDetailsRes")
        self.evcc.genchallenge = msg.get_Body().BodyElement.GenChallenge
        self.message_sender.send_authorization_req(msg)
        self.evcc.statemachine.send_AuthorizationReq()
        self.evcc.display_state()

    def handle_supported_app_protocol_res(self, msg):
        self.message_sender.send_session_setup_req(msg)
        self.evcc.statemachine.send_SessionSetupReq()
        self.evcc.display_state()

    def handle_session_stop_res(self, msg):
        print("Received SesssionStopRes")
        print("Closing Connection")
        self.evcc.tcpsock.close()
        print("Closed")

    def handle_welding_detection_res(self, msg):
        print("Received WeldingDetectionRes")
        self.message_sender.send_session_stop_req(msg)
        self.evcc.statemachine.send_SessionStopReq()
        self.evcc.display_state()

    def handle_metering_receipt_res(self, msg):
        print("Received MeteringReceiptRes")
        self.message_sender.send_power_delivery_req(msg, "Stop")
        self.evcc.statemachine.send_PowerDeliveryReq()
        self.evcc.display_state()

    def handle_charging_status_res(self, msg):
        print("Received ChargingStatusRes")
        # If not charged send another ChargingStatusReq
        if not self.evcc.controller.AC_charge_complete():
            self.message_sender.send_charging_status_req(msg)
            self.evcc.statemachine.send_ChargingStatusReq()
        else:
            # If fully charged send PowerDeliveryReq with chargeProgress=Stop
            print("###")
            print("EV FULLY AC Charged")
            print("###")
            self.message_sender.send_power_delivery_req(msg, "Stop")
            self.evcc.statemachine.send_PowerDeliveryReq()

        self.evcc.display_state()

    def handle_current_demand_res(self, msg):
        if msg.get_Body(
        ).BodyElement.ReceiptRequired == True and self.evcc.payment_option == "Contract":
            print("Received CurrentDemandRes with Receipt Required (PnC)")
            self.message_sender.send_metering_receipt_req(msg)
            self.evcc.statemachine.send_MeteringReceiptReq()
            self.evcc.display_state()
        else:
            exi_utils.print_colored_red(
                "No Meter Receipt has to be signed!")
            if self.evcc.controller.evressoc < 100:
                # Charge the Battery.
                self.evcc.controller.charge_up()

            else:
                exi_utils.print_colored_red("Fully Charged")
                # Continue the Changing Loop
            self.message_sender.send_current_demand_req(msg)
            self.evcc.statemachine.send_CurrentDemandReq()
            self.evcc.display_state()

    def handle_power_delivery_res(self, msg):
        print("Received PowerDeliveryRes")

        # If We are charging with AC then the next message should be ChargingStatusReq
        if self.evcc.controller.is_AC_mode(
        ) and not self.evcc.controller.ac_charging_finish:
            self.message_sender.send_charging_status_req(msg)
            self.evcc.statemachine.send_ChargingStatusReq()
            # If we finished charging with AC then the next message should be SessionStopReq
        elif self.evcc.controller.is_AC_mode(
        ) and self.evcc.controller.ac_charging_finish:
            self.message_sender.send_session_stop_req(msg)
            self.evcc.statemachine.send_SessionStopReq()

        elif self.evcc.controller.evressoc < 100:
            self.message_sender.send_current_demand_req(msg)
            self.evcc.statemachine.send_CurrentDemandReq()

        else:
            self.message_sender.send_welding_detection_req(msg)
            self.evcc.statemachine.send_WeldingDetectionReq()
        self.evcc.display_state()

    def handle_pre_charge_res(self, msg):
        print("Received PrechargeRes")
        # Check to see if EVTargetVoltage == EVSEPresentVoltage
        # Take EVSEPresentVoltage value from PrechargeRes message
        evsepresentvoltage = msg.get_Body(
        ).BodyElement.EVSEPresentVoltage.get_Value()
        exi_utils.print_colored_red(evsepresentvoltage)

        if (evsepresentvoltage == self.evcc.controller.ev_target_voltage):
            exi_utils.print_colored_red(
                "EV - EVSE Voltage matched. Charging will Start")
            self.message_sender.send_power_delivery_req(msg, "Start")
            self.evcc.statemachine.send_PowerDeliveryReq()
        else:
            # Send PreChargeReq Message again
            exi_utils.print_colored_red(
                "Still waiting for EVSE Present Voltage to match")
            self.message_sender.send_pre_charge_req(msg)
            self.evcc.statemachine.send_PreChargeReq()

        self.evcc.display_state()

    def handle_cable_check_res(self, msg):
        print("Received CableCheckRes")
        # Check if EVSEProcessing=Finished and react
        evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
        if evseprocessing == "Ongoing":
            # Send Another cablecheckreq
            self.message_sender.send_cable_check_req(msg)
            self.evcc.statemachine.send_CableCheckReq()
        elif evseprocessing == 'Finished':
            self.message_sender.send_pre_charge_req(msg)
            self.evcc.statemachine.send_PreChargeReq()
            self.evcc.display_state()

    def handle_charge_parameter_discovery_res(self, msg):
        print("Received ChargeParameterDiscoveryRes")
        # Check if EVSEProcessing=Finished and react
        evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
        if evseprocessing == "Ongoing":
            # Send Another chargeparameterdiscoveryreq
            self.message_sender.send_charge_parameter_discovery_req(msg)
            self.evcc.statemachine.send_ChargeParameterDiscoveryReq()
        elif evseprocessing == 'Finished' and self.evcc.controller.is_AC_mode():
            # IF AC continue with PowerDeliveryReq chargeProgress=Start
            self.message_sender.send_power_delivery_req(msg, "Start")
            # Close Contractor and switch to state C
            self.evcc.controller

            self.evcc.statemachine.send_PowerDeliveryReqAC()
        elif evseprocessing == 'Finished' and self.evcc.controller.is_DC_mode():
            # IF DC continue with CableCheckReq
            self.message_sender.send_cable_check_req(msg)
            self.evcc.statemachine.send_CableCheckReq()
        self.evcc.display_state()

    def handle_authorization_res(self, msg):
        print("Received AuthorizationRes")
        # Process Message
        evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
        if evseprocessing == "Ongoing":
            exi_utils.print_colored_red(
                "Send empty AuthorizationReq again")
            self.message_sender.send_authorization_req(msg)
            self.evcc.statemachine.send_AuthorizationReq()
        else:
            self.message_sender.send_charge_parameter_discovery_req(msg)
            self.evcc.statemachine.send_ChargeParameterDiscoveryReq()
            self.evcc.display_state()

    def handle_certificate_installation_res(self, msg):
        print("Received CertificateInstallationRes")
        # Verify Signature
        securityutils.verify_certificate_installation_res(msg)
        # Store Contract private key
        self.evcc.contract_private_key = securityutils.decrypt_contract_private_key(
            msg, self.evcc.oem_prov_key)
        self.message_sender.send_payment_details_req(msg)
        self.evcc.statemachine.send_PaymentDetailsReq()
        self.evcc.display_state()

    def handle_payment_service_selection_res(self, msg):
        print("Received PaymentServiceSelectionRes")
        # Check if Contract or EIM and react accordingly
        if self.evcc.payment_option == "Contract":
            self.message_sender.send_certificate_installation_req(msg)
            self.evcc.statemachine.send_CertificateInstallationReq()

        elif self.payment_option == "ExternalPayment":
            self.message_sender.send_authorization_req(msg)
            self.evcc.statemachine.send_AuthorizationReq()

        self.evcc.display_state()

    def handle_service_detail_res(self, msg):
        print("Received ServiceDetailRes")
        opt = input("Wanna send another service detail request? y/n")
        if opt == "y":
            # The EVCC wants to gain information about another Service
            serviceid = input(
                "Provide id of the service that you need more details")

            self.message_sender.send_service_detail_req(msg, serviceid)
            self.evcc.statemachine.send_ServiceDetailReq()
        else:
            self.message_sender.send_payment_service_selection_req(msg)
            self.evcc.statemachine.send_PaymentSelectionReq()

        self.evcc.display_state()


    def handle_service_discovery_res(self, msg):
        print("Received ServiceDiscoveryRes")
        # Prepare and send ServiceDetailReq
        self.message_sender.send_service_detail_req(msg, 2)
        self.evcc.statemachine.send_ServiceDetailReq()
        self.evcc.display_state()

    def handle_session_setup_res(self, msg):
        print("Received SessionSetupRes")

        # Prepare and send ServiceDiscoveryReq
        self.message_sender.send_service_discovery_req(msg)
        # Change State
        self.evcc.statemachine.send_ServiceDiscoveryReq()
        self.evcc.display_state()