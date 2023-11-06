from transitions import Machine
# pylint: disable=no-member
#evcc ac v2g

class SECC_State(object):
    pass


def create_secc_state_machine():
    #enum or class ta states
    states = ['WaitForSupportedAppProtocolReq','process_supportedAppProtocolReq','NegativeResponseMessage',
    'WaitForSessionSetupReq', 'process_SessionSetupReq', 'WaitForServiceDiscoveryReq','process_ServiceDiscoveryReq',
    'WaitForServiceDetailDescriptionReq','process_ServiceDetailReq','WaitForSDDorSPSReq','process_PaymentDetailsReq',
    'process_CertificateInstallationReq','WaitForPaymentDetailsReq', 'process_CertificateUpdateReq','process_ServicePaymentSelectionReq',
    'WaitForPDRorARorCIRorCUReq','process_AuthorizationReq','process_PaymentDetailsReq','process_CertificateInstallationReq',
    'WaitForPaymentDetailsReq', 'process_CertificateUpdateReq', 'WaitForPaymentDetailsReq', 'process_PaymentDetailsReq',
    'WaitForAuthorizationReq','WaitForChargeParameterDiscoveryReq','process_ChargeParameterDiscoveryReq','WaitForPowerDeliveryReq','WaitForCableCheckReq',
    'process_CableCheckReq','WaitForChargingStatusReq','process_ChargingStatusReq'
    ,'WaitForCSRorPDR','WaitForPreChargeReq','process_PreChargeReq','WaitForPCRorPDR','WaitForWDRorCPDRorSSReq','WaitForCDRorPDReq',
    'process_PowerDeliveryReq','process_CurrentDemandReq','WaitForMeteringReceiptReq','process_MeteringReceiptReq',
    'ProcessWeldingDetectionReq','process_SessionStopReq','Stop_Session_NoError'

    
    ]


    #trigger, source, destination
    transitions = [
        ['supportedAppProtocolReq', 'WaitForSupportedAppProtocolReq', 'process_supportedAppProtocolReq'], #
        
        ['send_supportedAppProtocolRes','process_supportedAppProtocolReq', 'WaitForSessionSetupReq'],
        ['SessionSetupReq', 'WaitForSessionSetupReq', 'process_SessionSetupReq'],
        ['send_SessionSetupRes', 'process_SessionSetupReq', 'WaitForServiceDiscoveryReq'],
        ['ServiceDiscoveryReq','WaitForServiceDiscoveryReq','process_ServiceDiscoveryReq'],
        
        #SDD =ServiceDetailDescription, SPS=ServicePaymentSelection
        ['send_ServiceDiscoveryRes','process_ServiceDiscoveryReq','WaitForSDDorSPSReq'],
        ['ServiceDetailReq', 'WaitForSDDorSPSReq', 'process_ServiceDetailReq'],
        ['send_ServiceDetailRes','process_ServiceDetailReq','WaitForSDDorSPSReq'],
        ['ServicePaymentSelectionReq','WaitForSDDorSPSReq','process_ServicePaymentSelectionReq'],
        
        #PDR=PaymentDetailsReq/ AR=AuthorizationReq/ CIR=CertificateInstallationReq/ CIR=CertificateUpdateReq
        ['send_ServicePaymentSelectionRes','process_ServicePaymentSelectionReq','WaitForPDRorARorCIRorCUReq'],
        #IF AC/DC Charging EIM
        ['AuthorizationReq','WaitForPDRorARorCIRorCUReq','process_AuthorizationReq'],

        #If AC/DC PnC
        #If Contract already installed
        ['PaymentDetailsReq','WaitForPDRorARorCIRorCUReq','process_PaymentDetailsReq'],
        #If Contract not installed
        ['CertificateInstallationReq','WaitForPDRorARorCIRorCUReq','process_CertificateInstallationReq'],
        ['send_CertificateInstallationRes','process_CertificateInstallationReq','WaitForPaymentDetailsReq'],
        #If Contract needs update
        ['CertificateUpdateReq','WaitForPDRorARorCIRorCUReq','process_CertificateUpdateReq'],
        #Either with ResponseCode=FAILED or ResponseCode=OK
        ['send_CertificateUpdateRes','process_CertificateUpdateReq','WaitForPaymentDetailsReq'],
        ['PaymentDetailsReq','WaitForPaymentDetailsReq','process_PaymentDetailsReq'],
        ['send_PaymentDetailsRes', 'process_PaymentDetailsReq', 'WaitForAuthorizationReq'],
        ['AuthorizationReq','WaitForAuthorizationReq','process_AuthorizationReq'],
        #EVSEProccessing=Ongoing ResponseCode=OK
        ['send_AuthorizationResOngoing','process_AuthorizationReq','WaitForAuthorizationReq'],
        #EVSEProcessing=Finished ResponseCode=OK
        ['send_AuthorizationResFinished','process_AuthorizationReq','WaitForChargeParameterDiscoveryReq'],
        ['ChargeParameterDiscoveryReq','WaitForChargeParameterDiscoveryReq','process_ChargeParameterDiscoveryReq'],
        #ChargeParameterDiscoveryRes ResponseCode OK EVSEProcessing=Ongoing
        ['send_ChargeParameterDiscoveryResOngoing','process_ChargeParameterDiscoveryReq','WaitForChargeParameterDiscoveryReq'],
        #######################AC Charging####################################
        ['send_ChargeParameterDiscoveryResFinishedAC','process_ChargeParameterDiscoveryReq', 'WaitForPowerDeliveryReq'],
        ['PowerDeliveryReq','WaitForPowerDeliveryReq','process_PowerDeliveryReq'],
        ['send_PowerDeliveryRes', 'process_PowerDeliveryReq', 'WaitForChargingStatusReq'],
        ['ChargingStatusReq','WaitForChargingStatusReq','process_ChargingStatusReq'],
        #Wait for another ChargingStatusReq or PowerDeliveryReq with chargeProgress=Stop
        ['send_ChargingStatusRes','process_ChargingStatusReq', 'WaitForCSRorPDR'],
        ['ChargingStatusReq','WaitForCSRorPDR','process_ChargingStatusReq'],
        
        ['send_ChargingStatusReq','WaitForCSRorPDR', '='],
        ['PowerDeliveryReq', 'WaitForCSRorPDR', 'process_PowerDeliveryReq'],
        ['send_PowerDeliveryRes','processPowerDeliveryReq','waitForSessionStopReq'],
        ['SessionStopReq','waitForSessionStopReq','process_SessionStopReq'],

        #######################DC Charging####################################

        #ChargeParameterDiscoveryRes ResponseCode OK EVSEProcessing=Ongoing
        ['send_ChargeParameterDiscoveryResFinished','process_ChargeParameterDiscoveryReq','WaitForCableCheckReq'],
        ['CableCheckReq','WaitForCableCheckReq','process_CableCheckReq'],

        #CableCheckRes EVSE=Ongoing ResponseCode=OK
        ['send_CableCheckResOngoing','process_CableCheckReq','WaitForCableCheckReq'],
        #CableCheckRes EVSE=Finished ResponseCode=OK
        ['send_CableCheckResFinished','process_CableCheckReq','WaitForPreChargeReq'],
        ['PreChargeReq','WaitForPreChargeReq','process_PreChargeReq'],
        ['send_PrechargeRes','process_PreChargeReq','WaitForPCRorPDR'],
        ['PreChargeReq','WaitForPCRorPDR','process_PreChargeReq'],
        ['PowerDeliveryReq','WaitForPCRorPDR','process_PowerDeliveryReq'],

        #If PowerDelivery Req ChargeProgress=Renegotiate
        ['send_PowerDeliveryResRenegotiate','process_PowerDeliveryReq','WaitForChargeParameterDiscoveryReq'],

        #If PowerDelivery Req ChargeProgress=Stop
        ['send_PowerDeliveryResStop','process_PowerDeliveryReq','WaitForWDRorCPDRorSSReq'],

        #If PowerDeliveryReq ChargeProgress=Start
        ['send_PowerDeliveryResDC','process_PowerDeliveryReq','WaitForCDRorPDReq'],
        ['PowerDeliveryReq','WaitForCDRorPDReq','process_PowerDeliveryReq'],
        ['CurrentDemandReq','WaitForCDRorPDReq','process_CurrentDemandReq'],

        #CurrentDemandRes MeteringReceipt=False
        ['send_CurrentDemandResNoReceipt','process_CurrentDemandReq','WaitForCDRorPDReq'],
        #CurrentDemandRes MeteringReceipt=True
        ['send_CurrentDemandRes','process_CurrentDemandReq','WaitForMeteringReceiptReq'],
        ['MeteringReceiptReq','WaitForMeteringReceiptReq','process_MeteringReceiptReq'],
        ['send_MeteringReceiptRes','process_MeteringReceiptReq','WaitForCDRorPDReq'],
        ['WeldingDetectionReq','WaitForWDRorCPDRorSSReq','ProcessWeldingDetectionReq'],
        ['send_WeldingDetectionRes','ProcessWeldingDetectionReq','WaitForWDRorCPDRorSSReq'],
        ['SessionStopReq','WaitForWDRorCPDRorSSReq','process_SessionStopReq'],
        ['send_SessionStopRes','process_SessionStopReq','Stop_Session_NoError'],

        


        

        # FAILED_SequenceError
        ['error_Message', '*', 'NegativeResponseMessage'],
        ['timeout_error', '*', 'Error']
        

        

    
    ]
    sm = SECC_State()
    SECC_machine = Machine(model = sm, states = states, transitions=transitions, initial='WaitForSupportedAppProtocolReq')
    return sm,SECC_machine




