from datetime import datetime
from iso15118.common.XML import appprotocol1, msgbody1, msgdatatypes1, msgDef1
from iso15118.secc import secc_config
from iso15118.common.exi_utils import exi_utils
from iso15118.common.security import securityutils
import time


class SECCMessageSender:
    def __init__(self, secc):
        self.secc = secc
        self.sessionid = None

    def send_secc_discovery_res(self, secc_discovery_req_msg, adress=None):
        """ Send SECCDiscoveryRes, a payload of 20 bytes, with the first 16 bytes denoting
        the IP address of the SECC, bytes 17 and 18 specifying its port, byte 19 stating the
        agreed-upon security level and byte 20 the transport protocol.

        Args:
            secc_discovery_req_msg (bytes): The previous SECCDiscoveryReq message
        """
        print("2: Preparing SECCDiscoveryRes")

        # ip adress 16bytes
        # ipadress = [int(x) for x in self.secc.ipadress.split(".")]
        # ipadress_endian = ipadress[0].to_bytes(
        #     4, "big") + ipadress[1].to_bytes(4, "big") + ipadress[2].to_bytes(
        #         4, "big") + ipadress[3].to_bytes(4, "big")

        # # port 17-18 bytes
        # sock_number = self.secc.tcpserver.getsockname()[1]
        # sock_number_endian = sock_number.to_bytes(2, "big")
        # # agreed security (0x00 for TLS) 19 byte
        # security = secc_discovery_req_msg[0:1]
        # # transport protocol 20 byte
        # transport = secc_discovery_req_msg[1:2]
        #
        # seccdiscoveryres = ipadress_endian + sock_number_endian + security + transport
        #
        # # Add Header
        # v2gmsg = exi_utils.add_Header_v2gEXI(seccdiscoveryres, "sdpres")
        #
        # if secc_config.SLOW_MODE:
        #     print("2: Send SECCDiscoveryRes?")
        #     print("2:Message to send:")
        #     print(v2gmsg)
        #     input("Press Enter to continue...")
        # self.secc.udpserver.sendto(v2gmsg, adress)
        #
        # print("2: SECCDiscoveryRes sent")

        #Instead of concatenating the byte values using the + operator,
        # you can use a bytearray and the extend() method to append each octet as bytes.
        ip_address = self.secc.ipadress.split(".")
        ip_address_endian = bytearray()

        for octet in ip_address:
            #Append each converted octet to the ip_address_endian bytearray using the extend() method.
            ip_address_endian.extend(int(octet).to_bytes(4, "big"))

        # Port (17-18 bytes)
        sock_number = self.secc.tcpserver.getsockname()[1]
        sock_number_endian = sock_number.to_bytes(2, "big")

        # Agreed security (19 byte)
        security = secc_discovery_req_msg[0:1]

        # Transport protocol (20 byte)
        transport = secc_discovery_req_msg[1:2]

        seccdiscoveryres = ip_address_endian + sock_number_endian + security + transport

        # Add Header
        v2gmsg = exi_utils.add_Header_v2gEXI(seccdiscoveryres, "sdpres")

        if secc_config.SLOW_MODE:
            print("2: Send SECCDiscoveryRes? \n"
                  "2: Message to send: \n" + v2gmsg )
            #print("2: Message to send:")
            #print(v2gmsg)
            input("Press Enter to continue...")

        self.secc.udpserver.sendto(v2gmsg, adress)

        print("2: SECCDiscoveryRes sent")

    def send_supported_app_protocol_res(self, supp_app_protocol_req_msg):
        """Send supportedAppProtocolRes message. Protocols supported by the SECC will
        be imported from the secc_config file. EVCC Protocol with the highest priority (Lowest
        number in supportedAppProtocolReq in Priority element) is being matched with the SECC
        supported protocols. Versions should match too. If versions don't match, continue with
        OK_SuccessfulNegotiationWithMinorDeviation response code. Protocol Namespace should
        be agreed, versions can be varied. supportedAppProtocolRes has the following structure:

        -supportedAppProtocolRes
            -SchemaID:  The agreed schema referenced by its id. SchemaID is the same as the request message
            -ResponseCode:  Indicate if a common protocol has been found between EVCC and SECC



        Args:
            supp_app_protocol_req_msg : The received supportedAppProtocolReq Message
        """
        print("4: Preparing supportedAppProtocolRes")
        appprotocols = supp_app_protocol_req_msg.get_AppProtocol()

        # Check if at least a protocol provided by EVCC match with protocols stored SECC
        secc_protocols = secc_config.appprotocols

        evcc_procolol_names = [x.get_ProtocolNamespace() for x in appprotocols]
        secc_protocol_names = [x[0] for x in secc_protocols]

        # Store the common ProtocolNamespaces
        common_protocols = bool(
            set(evcc_procolol_names) & set(secc_protocol_names))

        if common_protocols:
            protocolsdict = {}
            for protocol in appprotocols:
                protocolsdict.update({protocol: protocol.get_Priority()})
            protocol_chosen = min(protocolsdict, key=protocolsdict.get)

            # Check for selected protocol deviations
            if ([
                    x for x in secc_protocols
                    if (x[0] == protocol_chosen.get_ProtocolNamespace()
                        and x[1] > protocol_chosen.get_VersionNumberMinor())
            ]):
                response_code = "OK_SuccessfulNegotiationWithMinorDeviation"
            else:
                response_code = "OK_SuccessfulNegotiation"
            supappprres = appprotocol1.supportedAppProtocolRes(
                SchemaID=protocol_chosen.get_SchemaID(),
                ResponseCode=response_code)
        else:
            supappprres = appprotocol1.supportedAppProtocolRes(
                ResponseCode=appprotocol1.responseCodeType.
                FAILED__NO_NEGOTIATION)

        supappprres.original_tagname_ = "supportedAppProtocolRes"

        # Transform to EXI
        v2gtp = exi_utils.xml_to_v2gtp(supappprres, 'appprotres')

        exi_utils.display_before_send(supappprres, v2gtp)
        self.secc.evcc_client.sendall(v2gtp)
        print("4: supportedAppProtocolRes sent")

    def send_session_setup_res(self):
        """By using the SessionSetupRes the SECC responds to a SessionSetupReq. With the SessionSetupRes the
        SECC notifies the EVCC with an enclosed ResponseCode, whether establishing a new session or joining a
        previous Communication Session was successful or not.
        -SessionSetupRes
            -ResponseCode:  Aknowledgment status of V2G Messages received by the SECC
            -EVSEID:    Any ID that uniquely identifies the EVSE and the power outlet the vehicle is connected to
            -EVSETimeStamp: Timestamp of the current SECC time. Format is “Unix Time Stamp”. If there are no other
            means of synchronisation, EVCC will synchronise its time
        """
        print("6: Preparing SessionSetupRes")
        self.sessionid = securityutils.generate_session_id()

        responsecode = msgbody1.responseCodeType(
            msgbody1.responseCodeType.OK__NEW_SESSION_ESTABLISHED)
        sessionsetupres = msgbody1.SessionSetupResType(
            EVSEID=secc_config.EVSEID,
            EVSETimeStamp=datetime.timestamp(datetime.now()),
            ResponseCode=responsecode)
        sessionsetupres.original_tagname_ = "SessionSetupRes"

        session_setup_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=sessionsetupres)
        self.send_v2g_message(session_setup_res_msg)

        print("6: SessionSetupRes sent")

    def send_service_discovery_res(self, message):
        """The SECC will respond in its ServiceDiscoveryRes with the mandatory ChargeSer-
        vice and potentially some optional value-added services in the ServiceList element.
        The charging service informs about the supported energy transfer modes for AC and DC
        charging. A charging service is mandatory, whereas the installation or update of a contract
        certificate is just one example of an optional value-added service.
        Furthermore, the SECC informs about the available authentication methods, EIM
        (ExternalPayment) and/or PnC (Contract).

        Every Service is being imported from secc_config file.

        ServiceDiscoveryRes
            -Response Code
            -PaymentOptionList: List of payment options an SECC offers to the EVCC. EVCC can only select one Payment
            -ChargeService: Available charging services supported by the EVSE
            -ServiceList

        Args:
            message: Last V2G Message
        """
        print("8: Preparing ServiceDiscoveryRes")

        responsecode = msgbody1.responseCodeType(msgbody1.responseCodeType.OK)
        paymentoptionlist = msgbody1.PaymentOptionListType()

        paymentoptions = secc_config.paymentoptions
        chargeservices = secc_config.chargeservices
        servicelistfromfile = secc_config.servicelist

        # Payment Options
        for paymentoption in paymentoptions:
            paymentoptionlist.add_PaymentOption(paymentoption)

        # Charge Services
        for chargeservice in chargeservices:
            for id in chargeservice:
                chargeService = msgbody1.ChargeServiceType(
                    ServiceID=id,
                    ServiceName=chargeservice[id]["ServiceName"],
                    ServiceCategory=chargeservice[id]["ServiceCategory"],
                    FreeService=chargeservice[id]["FreeService"],
                    SupportedEnergyTransferMode=msgdatatypes1.
                    SupportedEnergyTransferModeType())
                for supportedenergytransfermode in (
                        chargeservice[id]["SupportedEnergyTransferMode"]):
                    chargeService.SupportedEnergyTransferMode.add_EnergyTransferMode(
                        supportedenergytransfermode)

        serviceList = msgbody1.ServiceListType()
        # ServiceList
        for service in servicelistfromfile:
            for id in service:
                service = msgdatatypes1.ServiceType(
                    ServiceID=id,
                    ServiceName=service[id]["ServiceName"],
                    ServiceCategory=service[id]["ServiceCategory"],
                    ServiceScope=service[id]["ServiceScope"],
                    FreeService=service[id]["FreeService"])

                serviceList.add_Service(service)
        servdiscres = msgbody1.ServiceDiscoveryResType(
            ResponseCode=responsecode,
            PaymentOptionList=paymentoptionlist,
            ChargeService=chargeService,
            ServiceList=serviceList)
        servdiscres.original_tagname_ = "ServiceDiscoveryRes"

        session_setup_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=servdiscres)
        self.send_v2g_message(session_setup_res_msg)

        print("8: ServiceDiscoveryRes sent")

    def send_service_detail_res(self, message):
        """After receiving the ServiceDetailReq message of an EVCC the SECC sends the ServiceDetailRes message
        and provides details about services. EVCC requested the details for a specific Service ID. Service Details
        are imported from secc_config and are being parsed on the ServiceDetailRes message.

        Args:
            message : The last V2G Message: ServiceDetailReq
        """
        print("10: Preparing ServiceDetailRes")

        service_id = message.get_Body().BodyElement.ServiceID
        servicelistfromfile = secc_config.servicelist

        serparlist = msgbody1.ServiceParameterListType()

        for servicelistelement in servicelistfromfile:
            for key in servicelistelement:
                if key == service_id:
                    for element in servicelistelement[key]["ParameterList"]:
                        parametertype = msgdatatypes1.ParameterType()
                        parametertype.stringValue = element[1]
                        parametertype.set_Name(element[2])
                        parameterset = msgdatatypes1.ParameterSetType()
                        parameterset.add_Parameter(parametertype)
                        parameterset.set_ParameterSetID(element[0])
                        serparlist.add_ParameterSet(parameterset)
        servdetres = msgbody1.ServiceDetailResType(
            ResponseCode=msgdatatypes1.responseCodeType.OK,
            ServiceID=service_id,
            ServiceParameterList=serparlist)
        servdetres.original_tagname_ = "ServiceDetailRes"

        session_setup_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=servdetres)
        self.send_v2g_message(session_setup_res_msg)
        print("10: ServiceDetailRes sent")

    def send_payment_service_selection_res(self, message):
        """Aknowledges the services selected by the EVCC and the payment option.

        Args:
            message : The last V2G Message
        """
        print("12: Preparing PaymentServiceSelectionRes")

        ############################################

        payserselres = msgbody1.PaymentServiceSelectionResType(
            ResponseCode=msgbody1.responseCodeType.OK)
        payserselres.original_tagname_ = "PaymentServiceSelectionRes"

        ############################################

        session_setup_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=payserselres)
        self.send_v2g_message(session_setup_res_msg)
        print("12: PaymentServiceSelectionRes sent")

    def send_certificate_installation_res(self, message):
        """Send CertificateInstallRes message which contains the Contract Certificate chain,
        the encrypted contract private key corresponding to the Contract Certificate chain, the Secondary
        Actor certificate chain (e.g CPS Certificate Chain) and the DH public that will be used
        to encrypt the encrypted contract private key

        Args:
            message : Last message received
        """
        print("14: Preparing CertificateInstallationRes")

        # Create CertificateInstallationResponse Template
        certinstres = securityutils.generate_certificate_installation_res_body(
        )

        # Load Contract Certificate
        certinstres = securityutils.load_contract_certificates_to_xml(
            'common/PKI/CPS/moCertChain.p12', certinstres)
        # Load CPS Certificate
        certinstres = securityutils.load_cps_certificates_to_xml(
            'common/PKI/CPS/cpsCertChain.p12', certinstres)
        # Generate DH PublicKey
        certinstres = securityutils.generate_dhpublickey_contractsignatureencryptedprivatekey(
            'common/PKI/EVCC/oemProvCert.pem', 'common/PKI/CPS/contract.key', certinstres)

        certinstres.original_tagname_ = "CertificateInstallationRes"

        # Create V2g Message
        certificate_installation_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=certinstres)
        # Attach reference identifiers
        certificate_installation_res_msg = securityutils.attach_reference_identifiers(
            certificate_installation_res_msg)
        # Sign V2G Message
        certificate_installation_res_msg = securityutils.sign_cert_install_res_message(
            certificate_installation_res_msg, 'common/PKI/CPS/cpsSubCA2.key')
        self.send_v2g_message(certificate_installation_res_msg)

    def send_payment_details_res(self, message):
        """With the PaymentDetailsRes the SECC informs the EVCC whether the previously provided payment details
        were accepted or not. The SECC sends also a challenge in the form of a random number, which has to be
        signed by the EVCC in the AuthorizationReq message.

        Args:
            message : PaymentDetailsReq message
        """
        print("16: Preparing PaymentDetailsRes")

        paydetres = msgbody1.PaymentDetailsResType()
        paydetres.ResponseCode = msgbody1.responseCodeType.OK
        self.secc.gen = securityutils.generate_gen_challenge()
        paydetres.GenChallenge = self.secc.gen
        paydetres.EVSETimeStamp = int(time.time())

        paydetres.original_tagname_ = "PaymentDetailsRes"

        pay_det_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=paydetres)
        self.send_v2g_message(pay_det_res_msg)

        print("16: PaymentDetailsRes Sent")

    def send_authorization_res(self, message):
        """the SECC verifies the challenge signature (and the certificate with
        its chain if not done before) and sends the corresponding authorization response message.

        AythorizationRes
            -EVSEProcessing: Parameter indicating that the EVSE has finished the processing that was
            initiated after the AuthorizationReq or if the EVSE is still processing at the
            time, the response message was sent.
            -ResponseCode: ResponseCode indicating the acknowledgment status of any of the
            V2G messages received by the SECC.


        Args:
            message : The last AuthorizationReq message
        """
        print("18: Preparing AuthorizationRes")

        # Verifying the Genchallenge Value with the previous one
        if not message.get_Body().BodyElement._hasContent():
            exi_utils.print_colored_red("EIM Authorization")

        # Check to see if EIM was used
        elif message.get_Body().BodyElement.GenChallenge != self.secc.gen:
            exi_utils.print_colored_red(
                "GenChallenge value does not match with PaymentDetailsRes ")

        # In case of PnC
        else:
            # Verifying The Signature of AutharizationReq. Verified by contract certificate
            # public key
            securityutils.verify_authorization_req(
                message, self.secc.contract_certificate)

        autres = msgbody1.AuthorizationResType()
        autres.ResponseCode = msgbody1.responseCodeType.OK

        autres.EVSEProcessing = "Finished"
        autres.original_tagname_ = "AuthorizationRes"

        aut_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                              body_element=autres)
        self.send_v2g_message(aut_res_msg)

        if autres.EVSEProcessing == "Finished":
            self.secc.statemachine.send_AuthorizationResFinished()
        else:
            self.secc.statemachine.send_AuthorizationResOngoing()

        print("18: AuthorizationRes Sent")

    def send_charge_parameter_discovery_res(self, message):
        """With the ChargeParameterDiscoveryRes message the SECC provides applicable
        charge parameters from the grid’s perspective. Next to general charge parameters of
        the EVSE this optionally includes further information on cost over time, cost over demand,
        cost over consumption or a combination of these.

        ChargeParameterDiscoveryRes
            -EVSEProcessing: Parameter indicating that the EVSE has
                finished the processing that was initiated after the ChargeParameterDiscoveryReq
                or that the EVSE is still processing at the time, the response message was sent.
            -ResponseCode: ResponseCode indicating the acknowledgment status of any of the V2G messages received by the SECC.
            -SAScheduleList: Includes several tuples of schedules from secondary actors.
            -AC_EVSEChargeParameter: Target setting process for AC charging
            -DC_EVSEChargeParameter: Target setting process for DC charging

        Args:
            message : Last ChargeParameterDiscoveryReq message
        """
        print("20: Preparing ChargeParameterDiscoveryRes")

        charparamdisres = msgbody1.ChargeParameterDiscoveryResType()
        charparamdisres.original_tagname_ = "ChargeParameterDiscoveryRes"
        charparamdisres.ResponseCode = msgbody1.responseCodeType.OK

        charparamdisres.EVSEProcessing = self.secc.controller.get_evse_processing(
            "ChargeParameterDiscoveryRes")

        # If EVSE Processing is finished, then it is ready to send the PmaxSchedules
        if charparamdisres.EVSEProcessing == "Finished":

            # PmaxSchedule
            pmaxschedule = msgdatatypes1.PMaxScheduleType()

            # PmaxscheduleEntry
            pmaxschedulentry1 = msgdatatypes1.PMaxScheduleEntryType(
                TimeInterval=msgdatatypes1.RelativeTimeIntervalType(0),
                PMax=msgdatatypes1.PhysicalValueType(3, 'W', 25))
            pmaxschedule.add_PMaxScheduleEntry(pmaxschedulentry1)

            pmaxschedulentry1 = msgdatatypes1.PMaxScheduleEntryType(
                TimeInterval=msgdatatypes1.RelativeTimeIntervalType(600),
                PMax=msgdatatypes1.PhysicalValueType(3, 'W', 50))
            pmaxschedule.add_PMaxScheduleEntry(pmaxschedulentry1)

            # SAScheduleTuple
            sascheduletuple = msgdatatypes1.SAScheduleTupleType(
                SAScheduleTupleID=1, PMaxSchedule=pmaxschedule)

            # SAScheduleList
            sasschelist = msgdatatypes1.SAScheduleListType()
            sasschelist.original_tagname_ = "SAScheduleList"

            sasschelist.add_SAScheduleTuple(sascheduletuple)

            charparamdisres.SASchedules = sasschelist

        #Prepare message for DC case
        if self.secc.controller.is_DC_mode():

            # DC_EVSEChargeParameter
            dcevchargeparameter = msgdatatypes1.DC_EVSEChargeParameterType()
            dcevchargeparameter.original_tagname_ = "DC_EVSEChargeParameter"

            dcevchargeparameter.DC_EVSEStatus = self.secc.parse_evse_status()

            dcevchargeparameter.EVSEMaximumCurrentLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.A,
                Value=self.secc.controller.evse_maximum_current_limit)
            dcevchargeparameter.EVSEMaximumPowerLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.W,
                Value=self.secc.controller.evse_maximum_power_limit)
            dcevchargeparameter.EVSEMaximumVoltageLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.V,
                Value=self.secc.controller.evse_maximum_voltage_limit)
            dcevchargeparameter.EVSEMinimumCurrentLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.A,
                Value=self.secc.controller.evse_minimum_current_limit)
            dcevchargeparameter.EVSEMinimumVoltageLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.V,
                Value=self.secc.controller.evse_minimum_voltage_limit)
            dcevchargeparameter.EVSEPeakCurrentRipple = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgbody1.unitSymbolType.A,
                Value=self.secc.controller.evse_peak_current_ripple)

            charparamdisres.EVSEChargeParameter = dcevchargeparameter
        else:

            acevchargeparameter = msgdatatypes1.AC_EVSEChargeParameterType()
            acevchargeparameter.original_tagname_ = "AC_EVSEChargeParameter"

            # AC_EVSEstatus

            acevchargeparameter.AC_EVSEStatus = self.secc.parse_evse_status()

            acevchargeparameter.EVSENominalVoltage = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.V,
                Value=self.secc.controller.evse_nominal_voltage)

            acevchargeparameter.EVSEMaxCurrent = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit=msgdatatypes1.unitSymbolType.V,
                Value=self.secc.controller.evse_max_current)

            charparamdisres.EVSEChargeParameter = acevchargeparameter

        char_param_disc_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=charparamdisres)
        self.send_v2g_message(char_param_disc_res_msg)

        if charparamdisres.EVSEProcessing == "Ongoing":
            self.secc.statemachine.send_ChargeParameterDiscoveryResOngoing()

        elif charparamdisres.EVSEProcessing == "Finished" and self.secc.controller.is_DC_mode(
        ):
            self.secc.statemachine.send_ChargeParameterDiscoveryResFinished()
        elif charparamdisres.EVSEProcessing == "Finished" and self.secc.controller.is_AC_mode(
        ):
            self.secc.statemachine.send_ChargeParameterDiscoveryResFinishedAC()
        self.secc.display_state()
        print("20: ChargeParameterDiscoveryRes Sent")

    def send_cable_check_res(self, message):
        """As soon as the high-voltage system isolation status check is finished, the CableCheckRes
        will have its parameter EVSEProcessing set to ”Finished”, together with the EVSEIso-
        lationStatus parameter set to ”Valid” in case the isolation test has been carried out
        successfully and did not result in an isolation warning or fault.

        Args:
            message : CableCheckReq message
        """
        print("22: Preparing CableCheckRes")

        cablecheckres = msgbody1.CableCheckResType()

        cablecheckres.ResponseCode = msgbody1.responseCodeType.OK
        # Get DC_EVSEStatus
        cablecheckres.DC_EVSEStatus = self.secc.parse_evse_status()
        evseprocessing = self.secc.controller.get_evse_processing(
            "CableCheckRes")
        cablecheckres.EVSEProcessing = evseprocessing

        cablecheckres.original_tagname_ = "CableCheckRes"

        cable_check_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=cablecheckres)
        self.send_v2g_message(cable_check_res_msg)

        if evseprocessing == "Ongoing":
            self.secc.statemachine.send_CableCheckResOngoing()
        else:
            self.secc.statemachine.send_CableCheckResFinished()

        print("22: CableCheckRes Sent")

    def send_pre_charge_res(self, message):
        """The Precharge Loop will end when EVSEPresentVoltage==EVTargetVoltage
        """
        print("24: Preparing PreChargeRes")

        prechares = msgbody1.PreChargeResType(
            ResponseCode=msgbody1.responseCodeType.OK)
        prechares.DC_EVSEStatus = self.secc.parse_evse_status()

        prechares.EVSEPresentVoltage = msgdatatypes1.PhysicalValueType(
            Multiplier=0,
            Unit=msgdatatypes1.unitSymbolType.V,
            Value=self.secc.controller.evse_present_voltage)

        prechares.original_tagname_ = "PreChargeRes"

        pre_char_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                   body_element=prechares)
        self.send_v2g_message(pre_char_res_msg)

        print("24: PreChargeRes Sent")

    def send_power_delivery_res(self, message):
        print("26: Preparing PowerDeliveryRes")

        powdelres = msgbody1.PowerDeliveryResType()

        powdelres.original_tagname_ = "PowerDeliveryRes"

        powdelres.ResponseCode = msgbody1.responseCodeType.OK

        powdelres.EVSEStatus = self.secc.parse_evse_status()

        power_delivery_res_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=powdelres)
        self.send_v2g_message(power_delivery_res_msg)

        print("26: PowerDeliveryRes Sent")

    def send_current_demand_res(self, message):
        print("28: Preparing CurrentDemandRes")

        curdemres = msgbody1.CurrentDemandResType()

        curdemres.ResponseCode = msgbody1.responseCodeType.OK
        curdemres.DC_EVSEStatus = self.secc.parse_evse_status()

        curdemres.EVSEPresentVoltage = msgdatatypes1.PhysicalValueType(
            0, 'V', self.secc.controller.evse_present_voltage)
        curdemres.EVSEPresentCurrent = msgdatatypes1.PhysicalValueType(
            0, 'A', self.secc.controller.evse_present_current)
        curdemres.EVSECurrentLimitAchieved = self.secc.controller.get_evse_current_limit_achieved()
        curdemres.EVSEVoltageLimitAchieved = self.secc.controller.get_evse_voltage_limit_achieved()
        curdemres.EVSEPowerLimitAchieved = self.secc.controller.get_evse_power_limit_achieved()
        curdemres.EVSEMaximumVoltageLimit = msgdatatypes1.PhysicalValueType(
            0, 'A', self.secc.controller.evse_maximum_voltage_limit)
        curdemres.EVSEMaximumCurrentLimit = msgdatatypes1.PhysicalValueType(
            0, 'A', self.secc.controller.evse_maximum_current_limit)
        curdemres.EVSEMaximumPowerLimit = msgdatatypes1.PhysicalValueType(
            3, 'W', self.secc.controller.evse_maximum_power_limit)
        curdemres.EVSEID = secc_config.EVSEID
        curdemres.SAScheduleTupleID = 1

        #If ChargingComplete==True then add receiptRequired=True
        if message.get_Body().BodyElement.ChargingComplete:
            curdemres.MeterInfo = msgbody1.MeterInfoType(
                MeterID="V2G-CLARITY-METER-12345",
                MeterReading=2914,
                TMeter=1480345690)
            curdemres.ReceiptRequired = True
        else:
            curdemres.ReceiptRequired = False

        curdemres.original_tagname_ = "CurrentDemandRes"

        cur_dem_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=curdemres)
        self.send_v2g_message(cur_dem_res_msg)
        print("28: CurrentDemandRes Sent")

    def send_charging_status_res(self, message):
        print("Preparing ChargingStatusRes")

        chastares = msgbody1.ChargingStatusResType()
        chastares.ResponseCode = "OK"
        chastares.EVSEID = secc_config.EVSEID
        chastares.SAScheduleTupleID = 1
        chastares.EVSEMaxCurrent = msgdatatypes1.PhysicalValueType(
            0, 'A', self.secc.controller.evse_max_current)
        chastares.AC_EVSEStatus = self.secc.parse_evse_status()
        chastares.original_tagname_ = "ChargingStatusRes"

        cur_dem_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=chastares)
        self.send_v2g_message(cur_dem_res_msg)
        print("28: ChargingStatusRes Sent")

    def send_metering_receipt_res(self, message):
        print("30: Preparing MeteringReceiptRes")
        metering_rec_req_verified = securityutils.verify_metering_receipt_req(
            message, self.secc.contract_certificate)

        metrecres = msgbody1.MeteringReceiptResType()

        if metering_rec_req_verified:
            metrecres.ResponseCode = msgbody1.responseCodeType.OK
        else:
            metrecres.ResponseCode = msgbody1.responseCodeType.FAILED__METERING_SIGNATURE_NOT_VALID

        metrecres.EVSEStatus = msgdatatypes1.DC_EVSEStatusType(
            NotificationMaxDelay=0,
            EVSENotification=msgdatatypes1.EVSENotificationType.NONE,
            EVSEIsolationStatus=msgdatatypes1.isolationLevelType.VALID,
            EVSEStatusCode=msgdatatypes1.DC_EVSEStatusCodeType.EVSE__READY)

        metrecres.EVSEStatus.original_tagname_ = "DC_EVSEStatus"

        metrecres.original_tagname_ = "MeteringReceiptRes"

        met_rec_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=metrecres)
        self.send_v2g_message(met_rec_res_msg)

        print("30: MeteringReceiptRes Sent")

    def send_welding_detection_res(self, message):
        print("Preparing WeldingDetectionRes")

        weldetres = msgbody1.WeldingDetectionResType()
        weldetres.DC_EVSEStatus = self.secc.parse_evse_status()
        weldetres.EVSEPresentVoltage = msgdatatypes1.PhysicalValueType(
            Multiplier=0, Unit='V', Value=0)
        weldetres.original_tagname_ = "WeldingDetectionRes"

        wel_det_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=weldetres)
        self.send_v2g_message(wel_det_res_msg)
        print("WeldingDetectionRes Semt")

    def send_session_stop_res(self, message):
        print("32: Preparing SessionStopRes")

        sesstopres = msgbody1.SessionStopResType()
        sesstopres.ResponseCode = msgbody1.responseCodeType.OK

        sesstopres.original_tagname_ = "SessionStopRes"

        wel_det_res_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=sesstopres)
        self.send_v2g_message(wel_det_res_msg)

        print("32: SessionStopRes Sent")

    def create_v2g_message(self, session_id, body_element):
        header = msgDef1.MessageHeaderType(SessionID=session_id)
        body = msgDef1.BodyType(body_element)
        return msgDef1.V2G_Message(Header=header, Body=body)

    def send_v2g_message(self, v2g_message):
        v2gmsg = exi_utils.v2g_to_EXI(v2g_message)
        v2gpmsg = exi_utils.add_Header_v2gEXI(v2gmsg, "v2g")
        exi_utils.display_before_send(v2g_message, v2gpmsg)
        self.secc.evcc_client.sendall(v2gpmsg)