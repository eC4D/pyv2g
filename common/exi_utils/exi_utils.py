from iso15118.common import java_caller
from iso15118.common.XML import msgDef1, appprotocol1
from iso15118.secc import secc_config
from termcolor import colored
from iso15118.evcc import evcc_config


def print_colored_green(text):
    """Pring text in green. For Debugging Purpose
    """
    print(colored(text, 'green'))


def print_colored_red(text):
    """Pring text in red. For Debugging Purpose
    """
    print(colored(text, 'red'))


def v2g_to_EXI(v2gmessage):
    """Converts a V2G XML message to EXI bytes

    Args:
        v2gmessage : The V2G message in XML form

    Returns:
        bytes: The EXI byte stream corresponding to the V2G XML message input
    """
    
    with open('common/EXI_Files/testresres.xml', 'w') as outfile:
        v2gmessage.export(outfile=outfile, level=0)
    java_caller.xml_to_binary('common/EXI_Files/testresres.xml',
                              'common/EXI_Files/test1_xml.exi')
    f = open("common/EXI_Files/test1_xml.exi", "rb")
    exi2 = f.read()
    return exi2


def EXI_to_v2g(exibytes):
    """Converts EXI bytes to V2G XML message

    Args:
        exibytes (bytes): EXI byte stream

    Returns:
        XML V2G Message corresponding to EXI Stream
    """
    f = open("common/EXI_Files/exisample.exi", "wb")
    f.write(exibytes)
    f.close()
    java_caller.binary_to_xml('common/EXI_Files/exisample.exi',
                              'common/EXI_Files/v2gxml.xml')
    msg_res = msgDef1.parse('common/EXI_Files/v2gxml.xml', silence=True)
    return msg_res


def appprotocol_to_EXI(appprotocol):
    """Converts an AppProtocol message to EXI bytes 

    Args:
        appprotocol : AppProtocol XML Message

    Returns:
        bytes: The EXI byte stream corresponding to the AppProtocol XML message input
    """
    with open('EXI_Files/testresres.xml', 'w') as outfile:
        appprotocol.export(outfile=outfile, level=0)
    java_caller.xml_to_binary('EXI_Files/testresres.xml',
                              'EXI_Files/test1_xml.exi')
    f = open("EXI_Files/test1_xml.exi", "rb")
    exi2 = f.read()
    return exi2


def EXI_to_appprotocol(exibytes):
    """Converts EXI bytes to AppProtocol XML message

    Args:
        exibytes (bytes): EXI byte stream

    Returns:
        XML AppProtocol Message
    """
    

    f = open("common/EXI_Files/exisample.exi", "wb")
    f.write(exibytes)
    f.close()
    java_caller.binary_to_xml('common/EXI_Files/exisample.exi',
                              'common/EXI_Files/appprotocol.xml')
    msg_res = appprotocol1.parse('common/EXI_Files/appprotocol.xml', silence=True)
    return msg_res


def add_Header_v2gEXI(exibytes, payloadtypename):
    """Prefixes the Header on an EXI or ServiceDiscovery byte stream. The header has the following structure:
    Byte No. |       1         |   2    |   3   |   4   |   5   |   6   |   7   |   8   |
             |Protocol Version||Inverse |  Payload Type |       Payload Length          |
                               |Protocol|
                               |Version |

    Based on the string value of payloadtypename parameter bytes no. 4 and 5 will be adjusted accordingly         

    Args:
        exibytes (bytes): Byte stream containing one of the following:
            EXI encoded V2G Message, SDP request, SDP response, AppProtocol Request, AppProtocol Response
        payloadtypename (string): A string defining the payload type that should be created. Overview:
            EXI encoded V2G Message : 8001
            SECCDiscoveryReq        : 9000
            SECCDiscoveryRes     : 9001
            EXI encoded AppProtocolReq Message: A000
            EXI encoded AppprotocolRes Message: A001

    Returns:
        bytes: The V2GTP Message containing the header and the payload. This message will be communicated
        between SECC and EVCC
    """
    # if payloadtypename == "v2g":
    #     payloadtype = 0x8001.to_bytes(2, "big")
    # elif payloadtypename == "sdpreq":
    #     payloadtype = 0x9000.to_bytes(2, "big")
    # elif payloadtypename == "sdpres":
    #     payloadtype = 0x9001.to_bytes(2, "big")
    # elif payloadtypename == "appprotreq":
    #     payloadtype = 0xA000.to_bytes(2, "big")
    # elif payloadtypename == "appprotres":
    #     payloadtype = 0xA001.to_bytes(2, "big")
    # header = (0x01.to_bytes(1, "big") + 0xFE.to_bytes(1, "big") + payloadtype +
    #           (len(exibytes)).to_bytes(4, "big"))
    # v2gexi = header + exibytes
    # return v2gexi

    """a dictionary payload_type_map is used to map payloadtypename to the corresponding payload type value. 
    The get() method retrieves the payload type value from the dictionary, and if it doesn't exist, it defaults to 0x0000. 
    Then, the code constructs the header and concatenates it with exibytes to form v2gexi."""

    payload_type_map = {
        "v2g": 0x8001,
        "sdpreq": 0x9000,
        "sdpres": 0x9001,
        "appprotreq": 0xA000,
        "appprotres": 0xA001
    }

    payloadtype = payload_type_map.get(payloadtypename, 0x0000).to_bytes(2, "big")
    header = b'\x01\xFE' + payloadtype + len(exibytes).to_bytes(4, "big")
    v2gexi = header + exibytes
    return v2gexi


def receiveAndCheckMessageType(msg):
    """Check the type of the V2GTP message. In case of ServiceDiscovery message returns the message
    type in string format. In case of a EXI encoded V2G or AppProtocol message, return the XML 
    representation of the message.

    Args:
        msg (bytes): The V2GTP byte stream message

    Returns:
        In case of ServiceDiscovery message returns a string describing the type of the message. 
        In case of EXI encoded V2G message returns the python representation of the XML Message 
    """

    

    header = msg[:8]
    payload = msg[8:]

    """convert header[2:4] to an integer once and store the result in a variable."""
    header_value = int.from_bytes(header[2:4], "big")


    if header_value == 0x9000:
        return payload
    elif header_value == 0x9001:
        return payload
    elif header_value == 0x8001:
        message = EXI_to_v2g(payload)
    elif header_value == 0xA000 or header_value == 0xA001:
        message = EXI_to_appprotocol(payload)

    """Avoid if and use dictionary lookup """
    # action_map = {
    #     0x9000: payload,
    #     0x9001: payload,
    #     0x8001: EXI_to_v2g(payload),
    #     0xA000: EXI_to_appprotocol(payload),
    #     0xA001: EXI_to_appprotocol(payload)
    # }
    # message = action_map.get(header_value, None)

    # if int.from_bytes(header[2:4], "big") == 0x9000:
    #     return payload
    # elif int.from_bytes(header[2:4], "big") == 0x9001:
    #     return payload
    # elif int.from_bytes(header[2:4], "big") == 0x8001:
    #     message = EXI_to_v2g(payload)
    # elif (int.from_bytes(header[2:4], "big") == 0xA000
    #       or int.from_bytes(header[2:4], "big") == 0xA001):
    #     message = EXI_to_appprotocol(payload)

    return message


def display_before_send(xmlmessage, v2gpmessage):
    '''Before sending a message, displays the message in XML form
    and in V2GTP form'''
    
    if isinstance(xmlmessage,appprotocol1.supportedAppProtocolReq) or isinstance(xmlmessage,appprotocol1.supportedAppProtocolRes):
        tagname = xmlmessage.original_tagname_
    else:
        tagname = xmlmessage.get_Body().BodyElement.original_tagname_
    if (secc_config.SLOW_MODE and( evcc_config.SLOW_MODE
            or evcc_config.slow_mode_custom[tagname])):
        print(f"Send {tagname} ?")
        print("Message to send:")
        print(xmlmessage)
        print("Message EXI encoded ")
        print(v2gpmessage)
        input("Press Enter to continue...")

def xml_to_v2gtp(xmlmessage,payloadtype):
    exi = v2g_to_EXI(xmlmessage)
    v2gtp = add_Header_v2gEXI(exi,payloadtype)
    return v2gtp

def check_v2g_message_type(xmlmessage):
    if isinstance(xmlmessage, msgDef1.V2G_Message):
        return xmlmessage.get_Body().BodyElement.original_tagname_
    else:
        return xmlmessage.original_tagname_
