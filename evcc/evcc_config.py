import os
#Before starting, set the enviroment path to the current directory!
#e.g export PYTHONPATH=$PYTHONPATH:/home/yourusername/Desktop/

TLS = True
TCP = True
HOST = "127.0.0.1"
PORT = 8080
SLOW_MODE = False
slow_mode_custom = {
    "supportedAppProtocolReq": False,
    "SessionSetupReq": False,
    "ServiceDiscoveryReq": False,
    "ServiceDetailReq": False,
    "PaymentServiceSelectionReq": False,
    "CertificateInstallationReq": False,
    "PaymentDetailsReq": False,
    "AuthorizationReq": False,
    "ChargeParameterDiscoveryReq": False,
    "CableCheckReq": False,
    "PreChargeReq": False,
    "PowerDeliveryReq": False,
    "ChargingStatusReq": False,
    "CurrentDemandReq": False,
    "MeteringReceiptReq": False,
    "WeldingDetectionReq" : False,
    "SessionStopReq": False
}
# Protocol namespace, version minor, version major, schema id, priority
appprotocols = [['15118:2:2010', 1, 1, 9, 2], ['15118:2:2013', 1, 2, 10, 1]]

#Chargint method, for AC case switch to AC
#CHARGING = 'DC_combo_core'
CHARGING = 'AC_three_phase_core'
#CHARGING_MODE = 'DC'
CHARGING_MODE = 'AC'

#Interface 
interfacename = ""


SELECTEDPAYMENTOPTION = 'Contract'
#SELECTEDPAYMENTOPTION = 'ExternalPayment'

# This will get you the directory of the current file (secc.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# This will get you the parent directory of the current_dir, which should be the project root
BASE_DIR = os.path.dirname(current_dir)




# Define the paths to the certificates relative to the parent directory
V2GROOTPATH = os.path.join(BASE_DIR,'common' ,'PKI', 'EVCC', 'v2gRootCACert.pem')
OEMPATH = os.path.join(BASE_DIR,'common' ,'PKI', 'EVCC', 'oemProvCert.pem')
OEMPROV_PRIV_KEY = os.path.join(BASE_DIR,'common' ,'PKI', 'EVCC', 'oemProv.key')

#Contract Certificate Not Installed -> Will be Installed with with ContractInstallationRes