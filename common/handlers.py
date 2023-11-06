from iso15118.common.exi_utils import exi_utils
from iso15118.common.security import securityutils
from iso15118.secc.secc_message_sender import SECCMessageSender
from iso15118.evcc.evcc_message_sender import EVCCMessageSender

class MessageHandler:
    def __init__(self, evcc, secc):
        self.secc = secc
        self.evcc = evcc
        self.message_sender_secc = SECCMessageSender(self.secc)
        self.message_sender_evcc = EVCCMessageSender(self.evcc)

        self.message_handlers = {
            'supportedAppProtocolReq': self.handle_supported_app_protocol,
            'SessionSetupReq': self.handle_session_setup,
            'ServiceDiscoveryReq': self.handle_service_discovery,
            'ServiceDetailReq': self.handle_service_detail,
            'PaymentServiceSelectionReq': self.handle_payment_service_selection,
            'CertificateInstallationReq': self.handle_certificate_installation,
            'PaymentDetailsReq': self.handle_payment_details,
            'AuthorizationReq': self.handle_authorization,
            'ChargeParameterDiscoveryReq': self.handle_charge_parameter_discovery,
            'CableCheckReq': self.handle_cable_check,
            'PreChargeReq': self.handle_pre_charge,
            'PowerDeliveryReq': self.handle_power_delivery,
            'CurrentDemandReq': self.handle_current_demand,
            'ChargingStatusReq': self.handle_charging_status,
            'MeteringReceiptReq': self.handle_metering_receipt,
            'WeldingDetectionReq': self.handle_welding_detection,
            'SessionStopReq': self.handle_session_stop,

            'supportedAppProtocolRes': self.handle_supported_app_protocol,
            'SessionSetupRes': self.handle_session_setup,
            'ServiceDiscoveryRes': self.handle_service_discovery,
            'ServiceDetailRes': self.handle_service_detail,
            'PaymentServiceSelectionRes': self.handle_payment_service_selection,
            'CertificateInstallationRes': self.handle_certificate_installation,
            'PaymentDetailsRes': self.handle_payment_details,
            'AuthorizationRes': self.handle_authorization,
            'ChargeParameterDiscoveryRes': self.handle_charge_parameter_discovery,
            'CableCheckRes': self.handle_cable_check,
            'PreChargeRes': self.handle_pre_charge,
            'PowerDeliveryRes': self.handle_power_delivery,
            'CurrentDemandRes': self.handle_current_demand,
            'ChargingStatusRes': self.handle_charging_status,
            'MeteringReceiptRes': self.handle_metering_receipt,
            'WeldingDetectionRes': self.handle_welding_detection,
            'SessionStopRes': self.handle_session_stop,
        }

    def process_message_and_react(self, message, is_client=False, address=None):
        """Based on the message input, this methods reacts accordingly:
        State transition -> Send next message -> State transition

        Args:
            message (bytes): The received V2GTP Message
            address : Address of the sender. This parameter will be used for the UDP response
        """
        msg = exi_utils.receiveAndCheckMessageType(message)
        print("RECEIVED: ")
        print(msg)

        if isinstance(msg, bytes):
            if is_client:
                self.handle_secc_discovery_res(msg)
            else:
                self.handle_sdr(message, address)
        else:
            message_type = exi_utils.check_v2g_message_type(msg)
            handler = self.message_handlers.get(message_type)
            if handler and message_type[-1] == 'q':
                handler(msg)
            else:
                handler(msg, False)

    def handle_secc_discovery_res(self, msg):
        print("New State:", self.evcc.statemachine.state)

        ip_address = ".".join(str(int.from_bytes(msg[i:i + 4], 'big')) for i in range(0, 16, 4))
        port = int.from_bytes(msg[16:18], "big")

        self.evcc.establish_evcc_tcp_connection(ip_address, port)

        self.message_sender_evcc.send_supported_app_protocol_req()

        self.evcc.statemachine.send_supportedAppProtocolReq()
        self.evcc.display_state()

    def handle_sdr(self, message, adress):
        print("Received SECCDiscoveryReq")

            # Process SECCDiscoveryReq
        payload = message[8:]
        if (payload[0] == 0 and payload[1] == 0):
            self.secc.tlstcp = True

            # After Processing prepare and send the SECCDiscoveryRes message
        self.message_sender_secc.send_secc_discovery_res(message, adress)

            # Establish TCP Connection
        self.secc.establish_secc_tcp_connection()

    def handle_supported_app_protocol(self, msg, is_request=True):
        if is_request:
            print("Received supportedAppProtocolReq")
            # Change state
            self.secc.statemachine.supportedAppProtocolReq()
            # Prepare and send supportedAppProtocolRes
            self.message_sender_secc.send_supported_app_protocol_res(msg)
            self.secc.statemachine.send_supportedAppProtocolRes()
            self.secc.display_state()
        else:
            self.message_sender_evcc.send_session_setup_req(msg)
            self.evcc.statemachine.send_SessionSetupReq()
            self.evcc.display_state()
        #self.secc.display_state()  # Assuming this line is common for both cases



    def handle_service_detail(self, msg, is_request=True):
        if is_request:
            print("Received ServiceDetailReq")
            self.secc.statemachine.ServiceDetailReq()
            self.message_sender_secc.send_service_detail_res(msg)
            self.secc.statemachine.send_ServiceDetailRes()
            self.secc.display_state()
        else:
            print("Received ServiceDetailRes")
            opt = input("Wanna send another service detail request? y/n")
            if opt == "y":
                # The EVCC wants to gain information about another Service
                serviceid = input(
                    "Provide id of the service that you need more details")

                self.message_sender_evcc.send_service_detail_req(msg, serviceid)
                self.evcc.statemachine.send_ServiceDetailReq()
            else:
                self.message_sender_evcc.send_payment_service_selection_req(msg)
                self.evcc.statemachine.send_PaymentSelectionReq()
                self.evcc.display_state()



    def handle_service_discovery(self, msg, is_request=True):
        if is_request:
            print("Received ServiceDiscoveryReq")
            self.secc.statemachine.ServiceDiscoveryReq()
            self.message_sender_secc.send_service_discovery_res(msg)
            self.secc.statemachine.send_ServiceDiscoveryRes()
            self.secc.display_state()
        else:
            print("Received ServiceDiscoveryRes")
            # Prepare and send ServiceDetailReq
            self.message_sender_evcc.send_service_detail_req(msg, 2)
            self.evcc.statemachine.send_ServiceDetailReq()
            self.evcc.display_state()

    def handle_session_setup(self, msg, is_request=True):
        if is_request:
            print("Received SessionSetupReq")

            # Change state
            self.secc.statemachine.SessionSetupReq()

            # Prepare and send SessionSetupRes
            self.message_sender_secc.send_session_setup_res()
            self.secc.statemachine.send_SessionSetupRes()
            self.secc.display_state()
        else:
            print("Received SessionSetupRes")

            # Prepare and send ServiceDiscoveryReq
            self.message_sender_evcc.send_service_discovery_req(msg)

            # Change State
            self.evcc.statemachine.send_ServiceDiscoveryReq()
            self.evcc.display_state()

    def handle_payment_service_selection(self, msg, is_request=True):
        if is_request:
            print("Received PaymentServiceSelectionReq")
            # If payment option is External Payment, skip to AuthorizationReq/Res message set
            self.secc.payment_option = msg.get_Body().BodyElement.SelectedPaymentOption

            self.secc.statemachine.ServicePaymentSelectionReq()
            self.message_sender_secc.send_payment_service_selection_res(msg)
            self.secc.statemachine.send_ServicePaymentSelectionRes()
            self.secc.display_state()
        else:
            print("Received PaymentServiceSelectionRes")
            # Check if Contract or EIM and react accordingly
            if self.evcc.payment_option == "Contract":
                self.message_sender_evcc.send_certificate_installation_req(msg)
                self.evcc.statemachine.send_CertificateInstallationReq()

            elif self.payment_option == "ExternalPayment":
                self.message_sender_evcc.send_authorization_req(msg)
                self.evcc.statemachine.send_AuthorizationReq()

            self.evcc.display_state()

    def handle_certificate_installation(self, msg, is_request = True):
        if is_request:
            print("Received CertificateInstallationReq")
            self.secc.statemachine.CertificateInstallationReq()
                # Verify Signature
            securityutils.verify_certificate_installation_req(msg)
            self.message_sender_secc.send_certificate_installation_res(msg)
            self.secc.statemachine.send_CertificateInstallationRes()
            self.secc.display_state()
        else:
            print("Received CertificateInstallationRes")
            # Verify Signature
            securityutils.verify_certificate_installation_res(msg)
            # Store Contract private key
            self.evcc.contract_private_key = securityutils.decrypt_contract_private_key(
                msg, self.evcc.oem_prov_key)
            self.message_sender_evcc.send_payment_details_req(msg)
            self.evcc.statemachine.send_PaymentDetailsReq()
            self.evcc.display_state()


    def handle_payment_details(self, msg, is_request = True):
        if is_request:
            print("Received PaymentDetailsReq")
            self.secc.statemachine.PaymentDetailsReq()
            self.message_sender_secc.send_payment_details_res(msg)
            cert = msg.get_Body().BodyElement.ContractSignatureCertChain.Certificate
            self.secc.contract_certificate = securityutils.load_pem_certificate(
                    cert)
            self.secc.statemachine.send_PaymentDetailsRes()
            self.secc.display_state()
        else:
            print("Received PaymentDetailsRes")
            self.evcc.genchallenge = msg.get_Body().BodyElement.GenChallenge
            self.message_sender_evcc.send_authorization_req(msg)
            self.evcc.statemachine.send_AuthorizationReq()
            self.evcc.display_state()

    def handle_authorization(self, msg, is_request = True):
        if is_request:
            print("Received AuthorizationReq")
                # AuthorizationReq <-> AuthorizationRes loop that ends when EVSEProcessing=Finished
            self.secc.statemachine.AuthorizationReq()
            self.message_sender_secc.send_authorization_res(msg)

            self.secc.display_state()
        else:
            print("Received AuthorizationRes")
            # Process Message
            evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
            if evseprocessing == "Ongoing":
                exi_utils.print_colored_red(
                    "Send empty AuthorizationReq again")
                self.message_sender_evcc.send_authorization_req(msg)
                self.evcc.statemachine.send_AuthorizationReq()
            else:
                self.message_sender_evcc.send_charge_parameter_discovery_req(msg)
                self.evcc.statemachine.send_ChargeParameterDiscoveryReq()
                self.evcc.display_state()

    def handle_charge_parameter_discovery(self, msg, is_request = True):
        if is_request:
            print("Received ChargeParameterDiscoveryReq")
                #Checking the request to see if DC or AC and instantiate controller
            if "DC" in msg.get_Body().BodyElement.RequestedEnergyTransferMode:
                self.secc.controller.set_to_dc_charging()
            elif "AC" in msg.get_Body().BodyElement.RequestedEnergyTransferMode:
                self.secc.controller.set_to_ac_charging()

            self.secc.statemachine.ChargeParameterDiscoveryReq()
            self.message_sender_secc.send_charge_parameter_discovery_res(msg)

        else:
            print("Received ChargeParameterDiscoveryRes")
            # Check if EVSEProcessing=Finished and react
            evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
            if evseprocessing == "Ongoing":
                # Send Another chargeparameterdiscoveryreq
                self.message_sender_evcc.send_charge_parameter_discovery_req(msg)
                self.evcc.statemachine.send_ChargeParameterDiscoveryReq()
            elif evseprocessing == 'Finished' and self.evcc.controller.is_AC_mode():
                # IF AC continue with PowerDeliveryReq chargeProgress=Start
                self.message_sender_evcc.send_power_delivery_req(msg, "Start")
                # Close Contractor and switch to state C
                self.evcc.controller

                self.evcc.statemachine.send_PowerDeliveryReqAC()
            elif evseprocessing == 'Finished' and self.evcc.controller.is_DC_mode():
                # IF DC continue with CableCheckReq
                self.message_sender_evcc.send_cable_check_req(msg)
                self.evcc.statemachine.send_CableCheckReq()
            self.evcc.display_state()

    def handle_cable_check(self, msg, is_request = True):
        if is_request:
            print("Received CableCheckReq")
            self.secc.statemachine.CableCheckReq()
            self.message_sender_secc.send_cable_check_res(msg)
            self.secc.display_state()
        else:
            print("Received CableCheckRes")
            # Check if EVSEProcessing=Finished and react
            evseprocessing = msg.get_Body().BodyElement.EVSEProcessing
            if evseprocessing == "Ongoing":
                # Send Another cablecheckreq
                self.message_sender_evcc.send_cable_check_req(msg)
                self.evcc.statemachine.send_CableCheckReq()
            elif evseprocessing == 'Finished':
                self.message_sender_evcc.send_pre_charge_req(msg)
                self.evcc.statemachine.send_PreChargeReq()
                self.evcc.display_state()

    def handle_pre_charge(self, msg, is_request = True):
        if is_request:
            print("Received PrechargeReq")
            self.secc.statemachine.PreChargeReq()
            self.message_sender_secc.send_pre_charge_res(msg)
            self.secc.statemachine.send_PrechargeRes()
            self.secc.display_state()
        else:
            print("Received PrechargeRes")
            # Check to see if EVTargetVoltage == EVSEPresentVoltage
            # Take EVSEPresentVoltage value from PrechargeRes message
            evsepresentvoltage = msg.get_Body(
            ).BodyElement.EVSEPresentVoltage.get_Value()
            exi_utils.print_colored_red(evsepresentvoltage)

            if (evsepresentvoltage == self.evcc.controller.ev_target_voltage):
                exi_utils.print_colored_red(
                    "EV - EVSE Voltage matched. Charging will Start")
                self.message_sender_evcc.send_power_delivery_req(msg, "Start")
                self.evcc.statemachine.send_PowerDeliveryReq()
            else:
                # Send PreChargeReq Message again
                exi_utils.print_colored_red(
                    "Still waiting for EVSE Present Voltage to match")
                self.message_sender_evcc.send_pre_charge_req(msg)
                self.evcc.statemachine.send_PreChargeReq()

            self.evcc.display_state()

    def handle_power_delivery(self, msg, is_request = True):
        if is_request:
            print("Received PowerDeliveryReq")
            self.secc.statemachine.PowerDeliveryReq()
            self.message_sender_secc.send_power_delivery_res(msg)
            if msg.get_Body().BodyElement.ChargeProgress == 'Stop':
                exi_utils.print_colored_red("STOP Charging")

                self.secc.statemachine.send_PowerDeliveryResStop()
            elif  self.secc.controller.is_DC_mode():
                self.secc.statemachine.send_PowerDeliveryResDC()
            else:
                self.secc.statemachine.send_PowerDeliveryRes()
            self.secc.display_state()
        else:
            print("Received PowerDeliveryRes")

            # If We are charging with AC then the next message should be ChargingStatusReq
            if self.evcc.controller.is_AC_mode(
            ) and not self.evcc.controller.ac_charging_finish:
                self.message_sender_evcc.send_charging_status_req(msg)
                self.evcc.statemachine.send_ChargingStatusReq()
                # If we finished charging with AC then the next message should be SessionStopReq
            elif self.evcc.controller.is_AC_mode(
            ) and self.evcc.controller.ac_charging_finish:
                self.message_sender_evcc.send_session_stop_req(msg)
                self.evcc.statemachine.send_SessionStopReq()

            elif self.evcc.controller.evressoc < 100:
                self.message_sender_evcc.send_current_demand_req(msg)
                self.evcc.statemachine.send_CurrentDemandReq()

            else:
                self.message_sender_evcc.send_welding_detection_req(msg)
                self.evcc.statemachine.send_WeldingDetectionReq()
            self.evcc.display_state()

    def handle_current_demand(self, msg, is_request = True):
        if is_request:
            print("Received CurrentDemandReq")
            self.secc.statemachine.CurrentDemandReq()
            self.message_sender_secc.send_current_demand_res(msg)
            if msg.get_Body().BodyElement.ChargingComplete:
                self.secc.statemachine.send_CurrentDemandRes()
            else:
                self.secc.statemachine.send_CurrentDemandResNoReceipt()
            self.secc.display_state()
        else:
            if msg.get_Body(
            ).BodyElement.ReceiptRequired == True and self.evcc.payment_option == "Contract":
                print("Received CurrentDemandRes with Receipt Required (PnC)")
                self.message_sender_evcc.send_metering_receipt_req(msg)
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
                self.message_sender_evcc.send_current_demand_req(msg)
                self.evcc.statemachine.send_CurrentDemandReq()
                self.evcc.display_state()

    def handle_charging_status(self, msg, is_request = True):
        if is_request:
            print("Received ChargingStatusReq")
            self.secc.statemachine.ChargingStatusReq()
            self.message_sender_secc.send_charging_status_res(msg)
            self.secc.statemachine.send_ChargingStatusRes()
            self.secc.display_state()
        else:
            print("Received ChargingStatusRes")
            # If not charged send another ChargingStatusReq
            if not self.evcc.controller.AC_charge_complete():
                self.message_sender_evcc.send_charging_status_req(msg)
                self.evcc.statemachine.send_ChargingStatusReq()
            else:
                # If fully charged send PowerDeliveryReq with chargeProgress=Stop
                print("###")
                print("EV FULLY AC Charged")
                print("###")
                self.message_sender_evcc.send_power_delivery_req(msg, "Stop")
                self.evcc.statemachine.send_PowerDeliveryReq()

            self.evcc.display_state()


    def handle_metering_receipt(self, msg, is_request = True):
        if is_request:
            print("Received MeteringReceiptReq")
            self.secc.statemachine.MeteringReceiptReq()
            self.message_sender_secc.send_metering_receipt_res(msg)
            self.secc.statemachine.send_MeteringReceiptRes()
            self.secc.display_state()
        else:
            print("Received MeteringReceiptRes")
            self.message_sender_evcc.send_power_delivery_req(msg, "Stop")
            self.evcc.statemachine.send_PowerDeliveryReq()
            self.evcc.display_state()

    def handle_welding_detection(self, msg, is_request = True):
        if is_request:
            print("Received WeldingDetectionReq")
            self.secc.statemachine.WeldingDetectionReq()
            self.message_sender_secc.send_welding_detection_res(msg)
            self.secc.statemachine.send_WeldingDetectionRes()
            self.secc.display_state()
        else:
            print("Received WeldingDetectionRes")
            self.message_sender_evcc.send_session_stop_req(msg)
            self.evcc.statemachine.send_SessionStopReq()
            self.evcc.display_state()


    def handle_session_stop(self, msg, is_request = True):
        if is_request:
            print("Received SessionStopReq")
            self.secc.statemachine.SessionStopReq()
            self.message_sender_secc.send_session_stop_res(msg)
            self.secc.statemachine.send_SessionStopRes()
            self.secc.display_state()
        else:
            print("Received SesssionStopRes")
            print("Closing Connection")
            self.evcc.tcpsock.close()
            print("Closed")