from enum import Enum, auto

class EStates(Enum):
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

#class ControlPilot:




