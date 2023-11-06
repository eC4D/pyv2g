from enum import Enum, auto
from transitions import Machine

class States(Enum):
    #auto() = automatically generate a unique numbber for each state
    Initial= auto()
    WaitForsupportedAppProtocolRes = auto()
    WaitForSessionSetupRes = auto()
    WaitForServiceDiscoveryRes = auto()
    WaitForServiceDetailRes = auto()
    WaitForServicePaymentSelectionRes = auto()
    WaitForCertificateInstallationRes = auto()
    WaitForCertificateUpdateRes = auto()
    WaitforPaymentDetailsRes = auto()
    WaitForAuthorizationRes = auto()

    transitions = {
        ('send_supportedAppProtocolReq', 'Initial'): 'WaitForsupportedAppProtocolRes',
        ('send_SessionSetupReq', 'WaitForsupportedAppProtocolRes'): 'WaitForSessionSetupRes',
        ('send_ServiceDiscoveryReq', 'WaitForSessionSetupRes'): 'WaitForServiceDiscoveryRes',

        ('send_PaymentSelectionReq', 'WaitForServiceDiscoveryRes'): 'WaitForServicePaymentSelectionRes',
        ('send_ServiceDetailReq', 'WaitForServiceDiscoveryRes'): 'WaitForServiceDetailRes',
        ('send_ServiceDetailReq', 'WaitForServiceDetailRes'): '=',
        ('send_PaymentSelectionReq', 'WaitForServiceDetailRes'): 'WaitForServicePaymentSelectionRes',

        # Install/Update Certificate
        ('send_CertificateInstallationReq', 'WaitForServicePaymentSelectionRes'): 'WaitForCertificateInstallationRes',
        ('send_CertificateUpdateReq', 'WaitForServicePaymentSelectionRes'): 'WaitForCertificateUpdateRes',
        ('send_PaymentDetailsReq',['WaitForCertificateUpdateRes', 'WaitForCertificateInstallationRes']): 'WaitforPaymentDetailsRes',

        # Certificate Installed
        ('send_PaymentDetailsReq', 'WaitForServicePaymentSelectionRes'): 'WaitforPaymentDetailsRes',

        # EIM
        ('send_AuthorizationReq', 'WaitForServicePaymentSelectionRes'): 'WaitForAuthorizationRes',
        ('send_AuthorizationReq', 'WaitforPaymentDetailsRes'): 'WaitForAuthorizationRes',

        # AuthorizationRes EVSEProcessing=Ongoing, Empty AuthorizationReq
        ('send_AuthorizationReq', 'WaitForAuthorizationRes'): '=',

        # AuthorizationRes EVSEProcessing=Finished
        ('send_ChargeParameterDiscoveryReq', 'WaitForAuthorizationRes'): 'WaitForChargeParameterDiscoveryRes',
        # ChargeParameterDiscoveryRes EVSEProcessing=Ongoing
        ('send_ChargeParameterDiscoveryReq', 'WaitForChargeParameterDiscoveryRes'): '=',

        # AC
        ('send_PowerDeliveryReqAC', 'WaitForChargeParameterDiscoveryRes'): 'WaitForPowerDeliveryRes',
        ('send_ChargingStatusReq', 'WaitForPowerDeliveryRes'): 'WaitForChargingStatusRes',
        ('send_ChargingStatusReq', 'WaitForChargingStatusRes'): '=',
        ('send_PowerDeliveryReq', 'WaitForChargingStatusRes'): 'WaitForPowerDeliveryRes',
        ('send_CableCheckReq', 'WaitForChargeParameterDiscoveryRes'): 'WaitForCableCheckRes',

    # CableCheckRes EVSEProcessing=Ongoing

        # CableCheckRes EVSEProcessing=Ongoing
        ('send_CableCheckReq', 'WaitForCableCheckRes'): '=',
        # CableCheckRes EVSEProcessing=Finished
        ('send_PreChargeReq', 'WaitForCableCheckRes'): 'WaitForPreChargeRes',

        # While value of Parameter EVSEPresentVoltage does not fulfil the voltage threshold requirement of the EV
        ('send_PreChargeReq', 'WaitForPreChargeRes'): '=',
        # EVSEPresentVoltage fulfils the voltage threshold requirement of the EV
        ('send_PowerDeliveryReq', 'WaitForPreChargeRes'): 'WaitForPowerDeliveryRes',
        ('send_CurrentDemandReq', 'WaitForPowerDeliveryRes'): 'WaitForCurrentDemandRes',
        # ReceiptRequired=False
        ('send_CurrentDemandReq', 'WaitForCurrentDemandRes'): '=',
        # ReceiptRequired=True
        ('send_MeteringReceiptReq', 'WaitForCurrentDemandRes'): 'WaitForMeteringReceiptRes',
        ('send_PowerDeliveryReq', 'WaitForMeteringReceiptRes'): 'WaitForPowerDeliveryRes',

        # Renegotiation: PowerDeliveryReq ChargeProgress=Renegotiate
        # Stop: PowerdeliveryReq ChargeProgress=Stop
        ('send_PowerDeliveryReq', 'WaitForCurrentDemandRes'): 'WaitForPowerDeliveryRes',
        # PowerDeliveryRes ChargeProgress = Stop , if EV wishes to do WeldingDetection
        ('send_WeldingDetectionReq', 'WaitForPowerDeliveryRes'): 'WaitForWeldingDetectionRes',
        # While WD is not finished on on EV Side
        ('send_WeldingDetectionReq', 'WaitForWeldingDetectionRes'): '=',
        # WD Finished
        ('send_SessionStopReq', 'WaitForWeldingDetectionRes'): 'WaitForSessionStopRes',
        ('send_SessionStopReq', 'WaitForPowerDeliveryRes'): 'WaitForSessionStopRes',

        ('terminate_communication', 'WaitForSessionStopRes'): 'StopSession_NoError',
        ('timeout_error', '*'): 'Error'
    }

    class State:
        def __init__(self, name):
            self.name = name

        def enter(self):
            pass

        def handle_input(self, input):
            pass

        def exit(self):
            pass

    class InitialState(State):
        def __init__(self):
            super().__init__("Initial")

        def enter(self):
            print("Entering Initial state")

        def handle_input(self, input):
            if input == "send_supportedAppProtocolReq":
                return ControlPilot.WaitForsupportedAppProtocolResState()
            return self

    class WaitForsupportedAppProtocolResState(State):
        def __init__(self):
            super().__init__("WaitForsupportedAppProtocolRes")

        def enter(self):
            print("Entering WaitForsupportedAppProtocolRes state")

        def handle_input(self, input):
            if input == "send_SessionSetupReq":
                return ControlPilot.WaitForSessionSetupResState()
            return self

    # Define other state classes similarly...

    def __init__(self):
        self.current_state = ControlPilot.InitialState()

    def handle_input(self, input):
        transition = (input, self.current_state.name)
        next_state_name = ControlPilot.transitions.get(transition)
        if next_state_name == '=':
            return self.current_state
        elif next_state_name:
            next_state = getattr(ControlPilot, next_state_name)()
            if next_state != self.current_state:
                self.current_state.exit()
                self.current_state = next_state
                self.current_state.enter()


# Usage example:
pilot = ControlPilot()
pilot.handle_input("send_supportedAppProtocolReq")  # Enters WaitForsupportedAppProtocolRes state
pilot.handle_input("send_SessionSetupReq")  # Transitions to WaitForSessionSetupRes state
