# pylint: disable=import-error
from iso15118.common.network import network


import socket
import os


SLOW_MODE = False
slow_mode_custom = {
    "supportedAppProtocolRes" : False,
    "SessionSetupRes": False,
    "ServiceDiscoveryRes" : False,
    "ServiceDetailRes" : False,
    "PaymentServiceSelectionRes": False,
    "CertificateInstallationRes": False,
    "PaymentDetailsRes": False,
    "AuthorizationRes": False,
    "ChargeParameterDiscoveryRes" : False,
    "CableCheckRes": False,
    "PreChargeRes": False,
    "PowerDeliveryRes" : False,
    "CurrentDemandRes" : False,
    "ChargingStatusRes" : False,
    "MeteringReceiptRes" : False,
    "WeldingDetectionRes": False,
    "SessionStopRes" : False
}



UDP_PORT = 15118
TCP_PORT = 8081
TLS_PORT = 8082
#Interface that will be used adjust according to the name of the ethernet interface
#e.g "eth0" (if ethernet connected)
#IP_ADRESS = network.get_ip(interface = "enp4s0f1")
#If local use localhost
IP_ADRESS =socket.gethostbyname(socket.gethostname())



# Get the absolute path of the parent directory of the current working directory
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Define the paths to the certificates relative to the parent directory
SECC_CERTCHAIN_PATH = os.path.join(parent_dir,'common' ,'PKI', 'SECC', 'cpoCertChain.p12')
SECC_PRIVATEKEY_PATH = os.path.join(parent_dir,'common' ,'PKI', 'SECC', 'secc.key')
SECC_CERTCHAIN_PEM_PATH = os.path.join(parent_dir,'common', 'PKI', 'SECC', 'cpoCertChain.pem')



#App Protocols supported
#Protocol namespace, version minor, version major
#SuccessfullNegotiation Example
appprotocols = [['15118:2:2010',1, 1,], ['15118:2:2013',1, 2,]]
#No_Negotiation Example
#appprotocols = ['15118:2:2015',1, 1,], ['15118:2:2018',1, 2,]
#SuccessfulNegotiationWithMinorDeviation Example
#appprotocols = [['15118:2:2010',1, 1,], ['15118:2:2013',2, 3,]]



EVSEID = 'DE*V2G*CLARITY123'

paymentoptions = ['Contract', 'ExternalPayment']

chargeservices = [
    {1: {
        "ServiceName": "EV charging (AC/DC)",
        "ServiceCategory" : "EVCharging",
        "FreeService" : False,
        "SupportedEnergyTransferMode" : ["AC_three_phase_core", "AC_single_phase_core",
                        "DC_core", "DC_extended", "DC_combo_core"]
    }
    }
]

servicelist = [
    {
    2: {
        "ServiceName" : "Contract certificate installation/update",
        "ServiceCategory" : "ContractCertificate",
        "ServiceScope": None,
        "FreeService": False,
        #id, Name, stringValue
        "ParameterList": [[1,"Certificate Installation", "Installation"],
                          [2,"Certificate Update", "Update"]]

    }
    },
    {
    3: {
        "ServiceName" : "InternetAccess",
        "ServiceCategory" : "Internet",
        "ServiceScope" : None,
        "FreeService" : False,
        #id, Name, stringValue
        "ParameterList": [
            [1,"5G Usage", "5G"],
            [2,"4G Usage", "4G"]]
    }
    }

]

evcc_dummy1 = {
    "RequestedEnergyTransferMode" : "DC_combo_core"

}
