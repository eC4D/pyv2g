from transitions import Machine
# pylint: disable=no-member


class EVCC_State(object):
    pass

# class EStates(Enum):
#     #auto() = automatically generate a unique numbber for each state
#     Initial= auto()
#     WaitForsupportedAppProtocolRes = auto()
#     WaitForSessionSetupRes = auto()
#     WaitForServiceDiscoveryRes = auto()
#     WaitForServiceDetailRes = auto()
#     WaitForServicePaymentSelectionRes = auto()
#     WaitForCertificateInstallationRes = auto()
#     WaitForCertificateUpdateRes = auto()
#     WaitforPaymentDetailsRes = auto()
#     WaitForAuthorizationRes = auto()

def create_evcc_state_machine():

    states = ['Initial', 'WaitForsupportedAppProtocolRes', 'WaitForSessionSetupRes', 'WaitForServiceDiscoveryRes',
    'WaitForServiceDetailRes', 'WaitForServicePaymentSelectionRes', 'WaitForCertificateInstallationRes', 'WaitForCertificateUpdateRes',
    'WaitforPaymentDetailsRes', 'WaitForAuthorizationRes', 'WaitForChargeParameterDiscoveryRes', 'WaitForCableCheckRes',
    'WaitForPreChargeRes', 'WaitForPowerDeliveryRes', 'WaitForCurrentDemandRes', 'WaitForChargingStatusRes',
    'WaitForMeteringReceiptRes', 'WaitForPowerDeliveryRes','WaitForWeldingDetectionRes','WaitForSessionStopRes',
    'StopSession_NoError','Error'
    ]


    #trigger, source, destination
    transitions = [
        ['send_supportedAppProtocolReq','Initial','WaitForsupportedAppProtocolRes'],
        ['send_SessionSetupReq','WaitForsupportedAppProtocolRes','WaitForSessionSetupRes'],
        ['send_ServiceDiscoveryReq','WaitForSessionSetupRes','WaitForServiceDiscoveryRes'],
        
        ['send_PaymentSelectionReq','WaitForServiceDiscoveryRes','WaitForServicePaymentSelectionRes'],
        ['send_ServiceDetailReq','WaitForServiceDiscoveryRes','WaitForServiceDetailRes'],
        ['send_ServiceDetailReq','WaitForServiceDetailRes','='],
        ['send_PaymentSelectionReq','WaitForServiceDetailRes','WaitForServicePaymentSelectionRes'],

        #Install/Update Certificate
        ['send_CertificateInstallationReq','WaitForServicePaymentSelectionRes','WaitForCertificateInstallationRes'],
        ['send_CertificateUpdateReq','WaitForServicePaymentSelectionRes','WaitForCertificateUpdateRes'],
        ['send_PaymentDetailsReq',['WaitForCertificateUpdateRes','WaitForCertificateInstallationRes'],'WaitforPaymentDetailsRes'],
        #Certificate Installed
        ['send_PaymentDetailsReq','WaitForServicePaymentSelectionRes','WaitforPaymentDetailsRes'],
        #EIM
        ['send_AuthorizationReq','WaitForServicePaymentSelectionRes','WaitForAuthorizationRes'],

        ['send_AuthorizationReq','WaitforPaymentDetailsRes','WaitForAuthorizationRes'],

        #AuthorizationRes EVSEProcessing=Ongoing, Empty AuthorizationReq
        ['send_AuthorizationReq','WaitForAuthorizationRes','='],

        #AuthorizationRes EVSEProcessing=Finished
        ['send_ChargeParameterDiscoveryReq','WaitForAuthorizationRes','WaitForChargeParameterDiscoveryRes'],
        #ChargeParameterDiscoveryRes EVSEProcessing=Ongoing
        ['send_ChargeParameterDiscoveryReq','WaitForChargeParameterDiscoveryRes','='],

        #AC
        ['send_PowerDeliveryReqAC','WaitForChargeParameterDiscoveryRes', 'WaitForPowerDeliveryRes'],
        ['send_ChargingStatusReq', 'WaitForPowerDeliveryRes', 'WaitForChargingStatusRes'],
        ['send_ChargingStatusReq', 'WaitForChargingStatusRes', '='],
        ['send_PowerDeliveryReq','WaitForChargingStatusRes','WaitForPowerDeliveryRes'],

       

        ['send_CableCheckReq','WaitForChargeParameterDiscoveryRes','WaitForCableCheckRes'],
        #CableCheckRes EVSEProcessing=Ongoing
        ['send_CableCheckReq','WaitForCableCheckRes','='],
        #CableCheckRes EVSEProcessing=Finished
        ['send_PreChargeReq','WaitForCableCheckRes','WaitForPreChargeRes'],

        #While value of Parameter EVSEPresentVoltage does not fulfil the voltage threshold requirement of the EV
        ['send_PreChargeReq','WaitForPreChargeRes','='],
        #EVSEPresentVoltage fulfils the voltage threshold requirement of the EV
        ['send_PowerDeliveryReq','WaitForPreChargeRes','WaitForPowerDeliveryRes'],
        ['send_CurrentDemandReq','WaitForPowerDeliveryRes','WaitForCurrentDemandRes'],
        #ReceiptRequired=False
        ['send_CurrentDemandReq','WaitForCurrentDemandRes','='],
        #ReceiptRequired=True
        ['send_MeteringReceiptReq','WaitForCurrentDemandRes','WaitForMeteringReceiptRes'],
        ['send_PowerDeliveryReq','WaitForMeteringReceiptRes','WaitForPowerDeliveryRes'],
        
        #Renegotiation: PowerDeliveryReq ChargeProgress=Renegotiate
        #Stop: PowerdeliveryReq ChargeProgress=Stop
        ['send_PowerDeliveryReq','WaitForCurrentDemandRes','WaitForPowerDeliveryRes'],
        #PowerDeliveryRes ChargeProgress = Stop , if EV wishes to do WeldingDetection
        ['send_WeldingDetectionReq','WaitForPowerDeliveryRes','WaitForWeldingDetectionRes'],
        #While WD is not finished on on EV Side
        ['send_WeldingDetectionReq','WaitForWeldingDetectionRes','='],
        #WD Finished
        ['send_SessionStopReq','WaitForWeldingDetectionRes','WaitForSessionStopRes'],
        ['send_SessionStopReq', 'WaitForPowerDeliveryRes' , 'WaitForSessionStopRes'],
       


        ['terminate_communication','WaitForSessionStopRes','StopSession_NoError'],
        ['timeout_error', '*', 'Error']
    ]

        

    
    
    sm = EVCC_State()
    EVCC_machine = Machine(model = sm, states = states, transitions=transitions, initial='Initial')
#    EVCC_machine = Machine(model=sm, states=EStates, transitions=transitions, initial=EStates.Initial)
    return sm,EVCC_machine



