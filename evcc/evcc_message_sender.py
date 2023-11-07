from common.XML import appprotocol1, msgbody1, msgdatatypes1, msgDef1
from evcc import evcc_config
from common.exi_utils import exi_utils
from common.security import securityutils
from common.network import network
from cryptography import x509


class EVCCMessageSender:
    def __init__(self, evcc):
        self.evcc = evcc
        self.sessionid = None

    def send_supported_app_protocol_req(self):
        """Send supportedAppProtocolReq Message. EVCC transmits the list of its supported
        protocols Supproted Protocols are imported from evcc_config. Each Protocol element contains:
        -ProtocolNamespace: Namespace URI
        -VersionNumberMajor: Major version of given ProtocolNamespace
        -VersionNumberMinor: Minor version of given ProtocolNamespace
        -SchemaID:  Schema ID assigned to givem ProtocolNamespace
        -Priority: A number indicating the priority of the given ProtocolNamespace. Low number means high Priority
        """
        print("3: Preparing supportedAppProtocolReq")

        supapppr = appprotocol1.supportedAppProtocolReq()

        appprotocols = evcc_config.appprotocols
        for protocol in appprotocols:
            apppr = appprotocol1.AppProtocolType(
                ProtocolNamespace=protocol[0],
                VersionNumberMinor=protocol[1],
                VersionNumberMajor=protocol[2],
                SchemaID=protocol[3],
                Priority=protocol[4])
            supapppr.add_AppProtocol(apppr)

        supapppr.original_tagname_ = "supportedAppProtocolReq"

        # Transform to EXI
        supp_app_protocol_req_msg = exi_utils.v2g_to_EXI(supapppr)
        v2gmsg = exi_utils.add_Header_v2gEXI(supp_app_protocol_req_msg,
                                             'appprotreq')

        exi_utils.display_before_send(supapppr, v2gmsg)

        print("3: supportedAppProtocolReq sent")

        self.evcc.tcpsock.sendall(v2gmsg)

        print("New State: ", self.evcc.statemachine.state)

    def send_session_setup_req(self, message):
        """Send SessionSetupReq Message. Sends the request to initiate a charging session. SessionID in Header
        is being instanciated with zeroes.

        SessionSetupReq:
            EVCCD: MAC address of the EVCC, given as six hexBinary encodedbytes
        """
        # Preparing SessionSetupReq
        print("5:Preparing SessionSetupReq ")
        header = msgDef1.MessageHeaderType(SessionID=bytes(8))
        mac = network.get_mac_in_hex()

        sesssetreq = msgbody1.SessionSetupReqType(EVCCID=mac)
        sesssetreq.original_tagname_ = 'SessionSetupReq'

        ses_sest_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                   body_element=sesssetreq)
        self.send_v2g_message(ses_sest_req_msg)

        print("5:SessionSetupReq sent")

    def send_service_discovery_req(self, message):
        """By sending the ServiceDiscoveryReq message the EVCC triggers the SECC to send information about all
        services offered by the SECC. Furthermore, the EVCC can limit for particular services by using the service
        scope and service type elements.

        ServiceDiscoveryReq
            -ServiceScope:  Ask for a certain scope of services. Optional. Each scope is mapped to an URI
            -ServiceCategory: Ask for a certain service category (e.g EV charging, internet access etc.)

        Args:
            message : The last V2G Message
        """
        print("7: Preparing ServiceDiscoveryReq")

        sessiondiscreq = msgbody1.ServiceDiscoveryReqType()
        sessiondiscreq.original_tagname_ = "ServiceDiscoveryReq"

        self.session_id = message.get_Header().get_SessionID()

        ses_ser_dis_req = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=sessiondiscreq)
        self.send_v2g_message(ses_ser_dis_req)

        print("7: ServiceDiscoveryReq Sent")

    def send_service_detail_req(self, message, serviceid):
        """By sending the ServiceDetailReq message the EVCC requests the SECC to send specific additional
        information about services offered by the EVSE.

        ServiceDetailReqType
            -ServiceID: This element identifies a service which has been offered by the SECC in the ServiceDiscoveryRes message.

        Args:
            message : The last V2G Message
        """
        print("9: Preparing ServiceDetailReq")

        servdetreq = msgbody1.ServiceDetailReqType(ServiceID=serviceid)
        servdetreq.original_tagname_ = "ServiceDetailReq"

        ser_det_req = self.create_v2g_message(session_id=self.sessionid,
                                              body_element=servdetreq)
        self.send_v2g_message(ser_det_req)

        print("9: ServiceDetailReq Sent")

    def send_payment_service_selection_req(self, message):
        """With this message the SECC informs the EVCC whether the selected services and payment option were accepted.

        PaymentServiceSelectionReq
            -SelectedPaymentOption:
            -SelectedServiceList:

        Args:
            message: The Last V2G Message
        """
        print("11: Preparing PaymentServiceSelectionReq")

        selservlis = msgbody1.SelectedServiceListType()
        selservice1 = msgdatatypes1.SelectedServiceType(ServiceID=1)
        selservice2 = msgdatatypes1.SelectedServiceType(ServiceID=2,
                                                        ParameterSetID=1)
        selservlis.add_SelectedService(selservice1)
        selservlis.add_SelectedService(selservice2)

        payserselreq = msgbody1.PaymentServiceSelectionReqType(
            SelectedPaymentOption=evcc_config.SELECTEDPAYMENTOPTION,
            SelectedServiceList=selservlis)

        payserselreq.original_tagname_ = "PaymentServiceSelectionReq"
        #####################################################################

        pay_ser_sel_req = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=payserselreq)
        self.send_v2g_message(pay_ser_sel_req)
        print("11: PaymentServiceSelectionReq Sent")

    def send_certificate_installation_req(self, message):
        """With this message the EVCC sends the request to install the contract certificate
        coresponding to its OEM_Prov certificate. The EVCC provides the OEM_prov certificate chain
        and the list of its RootCertificateIDs. The body of the message will be signed
        with the private key corresponding to the OEM_prov certificate.

        Args:
            message : The last V2G Message
        """
        print("13: Preparing CertificateInstallationReq")
        _f = open(self.evcc.oem_prov_cert, "rb")

        cert = _f.read()
        cert1 = x509.load_pem_x509_certificate(cert)
        cert = cert.split(b"-----")[2].strip()

        certinstreq = msgbody1.CertificateInstallationReqType()

        certinstreq.OEMProvisioningCert = cert

        listofrootcerts = msgbody1.ListOfRootCertificateIDsType()
        listofrootcerts.add_RootCertificateID(
            msgdatatypes1.X509IssuerSerialType(
                X509IssuerName=cert1.issuer,
                X509SerialNumber=cert1.serial_number))

        certinstreq.ListOfRootCertificateIDs = listofrootcerts

        certinstreq.original_tagname_ = "CertificateInstallationReq"

        certificate_installation_req_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=certinstreq)
        

        
        # Signing CertInstallReq Message
        certificate_installation_req_msg = securityutils.attach_reference_identifiers(
            certificate_installation_req_msg)

        private_key = securityutils.load_private_key(self.evcc.oem_prov_key)

        certificate_installation_req_msg = securityutils.sign_certinstallreq_message(
            certificate_installation_req_msg, private_key)
        
        self.send_v2g_message(certificate_installation_req_msg)

        

        

    def send_payment_details_req(self, message):
        """With the PaymentDetailsReq the EVCC provides the payment details in case the selected
        payment was “Contract”. By sending the signature certificate chain and eMAID, the EVCC
        requests the SECC to send a challenge.

        PaymentDetailsReq
            -eMAID: Element identifies the charging contract.
            -ContractSignatureCertChain: This element contains the Contract Certificate and optional SubCertificates
        Args:
            message : The last V2G Message
        """
        print("15: Preparing PaymentDetailsReq")
        self.evcc.contract_cert = message.get_Body(
        ).BodyElement.ContractSignatureCertChain

        emaid = message.get_Body().BodyElement.eMAID.valueOf_

        paydetreq = msgbody1.PaymentDetailsReqType()
        paydetreq.eMAID = emaid

        contractsignaturecertchain = msgbody1.CertificateChainType()
        contractsignaturecertchain.Certificate = b""

        contractsubcertificates = msgdatatypes1.SubCertificatesType()
        contractsubcertificates.add_Certificate(b"")
        contractsubcertificates.add_Certificate(b"")

        paydetreq.ContractSignatureCertChain = self.evcc.contract_cert

        paydetreq.ContractSignatureCertChain.set_Id(None)

        paydetreq.original_tagname_ = "PaymentDetailsReq"

        pay_det_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=paydetreq)
        self.send_v2g_message(pay_det_req_msg)

    def send_authorization_req(self, message):
        """The EVCC sends the GenChallenge it received within the PaymentDetailsRes back using
        the AuthorizationReq message and proves its authenticity as well as the integrity of the
        data with a signature.
        Signed Parts of AuthorizationReq:
            -Body| Signed by: Contract certificate private key
                 | Verified by: Contract certificate public key

        AuthorizationReq
            -Id: This attribute is used for referencing the message body in the signature
            header when a signature needs to
            be applied.
            -GenChallenge: The challenge sent by the SECC in PaymentDetailsRes message. This
            element contains the generated random number.

        Args:
            message : The last V2G Message
        """
        print("17 Preparing AuthorizationReq ")

        # Preparing AuthorizationReq

        autreq = msgbody1.AuthorizationReqType()

        autreq.original_tagname_ = "AuthorizationReq"

        authorization_req_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=autreq)
        

        

        # In case EIM will be used, CertificateInstallation will not be performed
        # and contract certificate and private key will be already stored in the EV
        if self.evcc.payment_option == "Contract":
            autreq.GenChallenge = self.evcc.genchallenge
            authorization_req_msg = securityutils.attach_reference_identifiers(
                authorization_req_msg)
            authorization_req_msg = securityutils.sign_authorization_req_message(
                authorization_req_msg, self.evcc.contract_private_key)
        
        self.send_v2g_message(authorization_req_msg)
        


        

    def send_charge_parameter_discovery_req(self, message):
        """By sending the ChargeParameterDiscoveryReq message the EVCC provides its
        charging parameters to the SECC. This message provides status information about
        the EV and additional charging parameters, like estimated energy amounts for
        recharging the vehicle, capabilities of the EV charging system and the point in
        time the vehicle operator intends to leave the EVSE.

        ChargeParameterDiscoveryReq
            -MaxEntriesSAScheduleTuple: Indicates the maximal number of entries in the SAScheduleTuple.
            The EVSE can transmit up to the maximum number of entriesdefined in the parameter.

            -RequestedEnergyTransferMode: Selected energy transfer mode for charging
            that is requested by the EVCC.

            -EVChargeParameter
                -AC_EVChargeParameter: Target setting process for AC charging.
                -DC_EVChargeParameter: Target setting process for DC charging.

        Args:
            message : The last V2G Message
        """
        print("19: Preparing ChargeParameterDiscoveryReq")

        ###

        chargeparamreq = msgbody1.ChargeParameterDiscoveryReqType()
        chargeparamreq.original_tagname_ = "ChargeParameterDiscoveryReq"

        chargeparamreq.RequestedEnergyTransferMode = evcc_config.CHARGING

        # Check If DC or AC, prepare messages accordingly
        if ("DC" in evcc_config.CHARGING):
            dcevchargeparameter = msgdatatypes1.DC_EVChargeParameterType()
            # Get DC_EVStatus
            dcevchargeparameter.DC_EVStatus = self.evcc.parse_ev_status()
            dcevchargeparameter.EVMaximumCurrentLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='A',
                Value=self.evcc.controller.maximum_current_limit)
            dcevchargeparameter.EVMaximumVoltageLimit = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='V',
                Value=self.evcc.controller.maximum_voltage_limit)
            dcevchargeparameter.EVEnergyRequest = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='Wh',
                Value=self.evcc.controller.ev_energy_request)
            dcevchargeparameter.original_tagname_ = "DC_EVChargeParameter"
            chargeparamreq.EVChargeParameter = dcevchargeparameter
        elif ("AC" in evcc_config.CHARGING):
            acevchargeparameter = msgdatatypes1.AC_EVChargeParameterType()
            acevchargeparameter.EAmount = msgdatatypes1.PhysicalValueType(
                Multiplier=3, Unit='Wh', Value=self.evcc.controller.eamount)
            acevchargeparameter.EVMaxVoltage = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='V',
                Value=self.evcc.controller.ev_max_voltage)
            acevchargeparameter.EVMaxCurrent = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='A',
                Value=self.evcc.controller.ev_max_current)
            acevchargeparameter.EVMinCurrent = msgdatatypes1.PhysicalValueType(
                Multiplier=0,
                Unit='A',
                Value=self.evcc.controller.ev_min_current)
            acevchargeparameter.original_tagname_ = "AC_EVChargeParameter"
            chargeparamreq.EVChargeParameter = acevchargeparameter

        cha_par_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=chargeparamreq)
        self.send_v2g_message(cha_par_req_msg)

        print("19: ChargeParameterDiscoveryReq Sent")

    def send_cable_check_req(self, message):
        """With the CableCheckReq the EV triggers the EVSE, or actually the DC supply (the power
        unit) to be precise, to start checking the high-voltage system isolation. The state of charge,
        given as a percentage value, is disclosed with the EVRESSOC  parameter. Only for DC charging

        CableCheckReq
            -DC_EVStatus: Current status of the EV

        """
        print("21: Preparing CableCheckReq")

        cablecheckreq = msgbody1.CableCheckReqType()
        #GET DC_EVStatus
        cablecheckreq.DC_EVStatus = self.evcc.parse_ev_status()

        cablecheckreq.original_tagname_ = "CableCheckReq"

        cab_che_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=cablecheckreq)
        self.send_v2g_message(cab_che_req_msg)
        print("21: CableCheckReq Sent")

    def send_pre_charge_req(self, message):
        """Contains both the requested DC current and voltage for the high-voltage battery."""

        print("23: Preparing PreChargeReq")

        prechareq = msgbody1.PreChargeReqType()

        prechareq.DC_EVStatus = self.evcc.parse_ev_status()
        prechareq.EVTargetVoltage = msgdatatypes1.PhysicalValueType(
            Multiplier=0,
            Unit=msgdatatypes1.unitSymbolType.V,
            Value=self.evcc.controller.ev_target_voltage)

        prechareq.EVTargetCurrent = msgdatatypes1.PhysicalValueType(
            Multiplier=0,
            Unit=msgdatatypes1.unitSymbolType.A,
            Value=self.evcc.controller.ev_target_current)

        prechareq.original_tagname_ = "PreChargeReq"

        pre_cha_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=prechareq)
        self.send_v2g_message(pre_cha_req_msg)

        print("23: PreChargeReq Sent")

    def send_power_delivery_req(self, message, chargeprogress):
        print("25: Preparing PowerDeliveryReq")

        ###

        powdelreq = msgbody1.PowerDeliveryReqType()

        powdelreq.original_tagname_ = "PowerDeliveryReq"

        powdelreq.ChargeProgress = msgbody1.chargeProgressType(chargeprogress)
        powdelreq.SAScheduleTupleID = 1

        charprofile = msgbody1.ChargingProfileType()
        profentry1 = msgdatatypes1.ProfileEntryType(
            ChargingProfileEntryStart=0,
            ChargingProfileEntryMaxPower=msgdatatypes1.PhysicalValueType(
                3, msgdatatypes1.unitSymbolType.W, 25))
        profentry2 = msgdatatypes1.ProfileEntryType(
            ChargingProfileEntryStart=600,
            ChargingProfileEntryMaxPower=msgdatatypes1.PhysicalValueType(
                3, msgdatatypes1.unitSymbolType.W, 50))
        profentry3 = msgdatatypes1.ProfileEntryType(
            ChargingProfileEntryStart=1080,
            ChargingProfileEntryMaxPower=msgdatatypes1.PhysicalValueType(
                0, msgdatatypes1.unitSymbolType.W, 0))

        charprofile.add_ProfileEntry(profentry1)
        charprofile.add_ProfileEntry(profentry2)
        charprofile.add_ProfileEntry(profentry3)

        powdelreq.ChargingProfile = charprofile

        pow_del_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=powdelreq)
        self.send_v2g_message(pow_del_req_msg)

        print("25: PowerDeliveryReq Sent")

    def send_charging_status_req(self, message):
        
        

        chastareq = msgDef1.ChargingStatusReqType()
        chastareq.original_tagname_ = "ChargingStatusReq"

        cha_sta_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=chastareq)
        self.send_v2g_message(cha_sta_req_msg)

    def send_current_demand_req(self, message):
        print("27: Preparing CurrentDemandReq")
        ###

        curdemreq = msgbody1.CurrentDemandReqType()

        curdemreq.DC_EVStatus = self.evcc.parse_ev_status()
        curdemreq.EVTargetCurrent = msgdatatypes1.PhysicalValueType(
            0, msgdatatypes1.unitSymbolType.A,
            self.evcc.controller.ev_target_current)
        curdemreq.EVMaximumVoltageLimit = msgdatatypes1.PhysicalValueType(
            0, msgdatatypes1.unitSymbolType.V,
            self.evcc.controller.maximum_voltage_limit)
        curdemreq.EVMaximumCurrentLimit = msgdatatypes1.PhysicalValueType(
            0, msgdatatypes1.unitSymbolType.A,
            self.evcc.controller.maximum_current_limit)
        curdemreq.EVMaximumPowerLimit = msgdatatypes1.PhysicalValueType(
            3, msgdatatypes1.unitSymbolType.W,
            self.evcc.controller.ev_maximum_power_limit)
        curdemreq.BulkChargingComplete = bool(
            self.evcc.controller.evressoc > 80)
        curdemreq.ChargingComplete = bool(self.evcc.controller.evressoc >= 100)
        curdemreq.RemainingTimeToFullSoC = msgdatatypes1.PhysicalValueType(
            0, msgdatatypes1.unitSymbolType.S, 1080)
        curdemreq.EVTargetVoltage = msgdatatypes1.PhysicalValueType(
            0, msgdatatypes1.unitSymbolType.V, 400)
        curdemreq.original_tagname_ = "CurrentDemandReq"

        cur_dem_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=curdemreq)
        self.send_v2g_message(cur_dem_req_msg)
        print("27: CurrentDemandReq Sent")

    def send_metering_receipt_req(self, message):
        """Send the MeteringReceiptReq message. MeterInfo from PowerDeliveryRes

        Args:
            message : _description_
        """
        meterinfo = message.get_Body().BodyElement.MeterInfo
        
        meterrecreq = msgbody1.MeteringReceiptReqType()
        

        meterrecreq.SAScheduleTupleID = 1

        meterrecreq.original_tagname_ = "MeteringReceiptReq"
        meterrecreq.MeterInfo = meterinfo

        metering_receipt_req_msg = self.create_v2g_message(
            session_id=self.sessionid, body_element=meterrecreq)
        
        metering_receipt_req_msg = securityutils.attach_reference_identifiers(
            metering_receipt_req_msg)

        metering_receipt_req_msg = securityutils.sign_metering_receipt_req_message(
            metering_receipt_req_msg, self.evcc.contract_private_key)

        self.send_v2g_message(metering_receipt_req_msg)

    def send_welding_detection_req(self, message):
        
        
        weldetreq = msgbody1.WeldingDetectionReqType()
        weldetreq.DC_EVStatus = self.evcc.parse_ev_status()
        weldetreq.original_tagname_ = "WeldingDetectionReq"

        

        wel_det_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=weldetreq)
        self.send_v2g_message(wel_det_req_msg)

    def send_session_stop_req(self, message):
        """Send the request to SECC to  stop the session

        Args:
            message: Last V2G message
        """
        
        sessetreq = msgbody1.SessionStopReqType()
        sessetreq.ChargingSession = msgbody1.chargingSessionType.TERMINATE
        sessetreq.original_tagname_ = "SessionStopReq"
        
        ses_set_req_msg = self.create_v2g_message(session_id=self.sessionid,
                                                  body_element=sessetreq)
        self.send_v2g_message(ses_set_req_msg)

        

    def create_v2g_message(self, session_id, body_element):
        header = msgDef1.MessageHeaderType(SessionID=session_id)
        body = msgDef1.BodyType(body_element)
        return msgDef1.V2G_Message(Header=header, Body=body)

    def send_v2g_message(self, v2g_message):
        v2gmsg = exi_utils.v2g_to_EXI(v2g_message)
        v2gpmsg = exi_utils.add_Header_v2gEXI(v2gmsg, "v2g")
        exi_utils.display_before_send(v2g_message, v2gpmsg)
        self.evcc.tcpsock.sendall(v2gpmsg)