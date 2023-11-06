# ./_v2gci_t.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1a6f87f6c5848c6b8455764e827cf4d80795af8e
# Generated 2021-07-04 00:14:40.049505 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace urn:iso:15118:2:2013:MsgDataTypes [xmlns:v2gci_t]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0f4a3f92-dc4c-11eb-996d-6c626d5e3387')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _xmlsig as _ImportedBinding__xmlsig

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:iso:15118:2:2013:MsgDataTypes', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 218, 0)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(0))
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(16777214))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 226, 0)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.unsignedInt(0))
STD_ANON_._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.unsignedInt(86400))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive,
   STD_ANON_._CF_maxInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}percentValueType
class percentValueType (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentValueType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 408, 0)
    _Documentation = None
percentValueType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=percentValueType, value=pyxb.binding.datatypes.byte(0))
percentValueType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=percentValueType, value=pyxb.binding.datatypes.byte(100))
percentValueType._InitializeFacetMap(percentValueType._CF_minInclusive,
   percentValueType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'percentValueType', percentValueType)
_module_typeBindings.percentValueType = percentValueType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}faultMsgType
class faultMsgType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'faultMsgType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 414, 0)
    _Documentation = None
faultMsgType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
faultMsgType._InitializeFacetMap(faultMsgType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'faultMsgType', faultMsgType)
_module_typeBindings.faultMsgType = faultMsgType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}EVSEProcessingType
class EVSEProcessingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessingType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 419, 0)
    _Documentation = None
EVSEProcessingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EVSEProcessingType, enum_prefix=None)
EVSEProcessingType.Finished = EVSEProcessingType._CF_enumeration.addEnumeration(unicode_value='Finished', tag='Finished')
EVSEProcessingType.Ongoing = EVSEProcessingType._CF_enumeration.addEnumeration(unicode_value='Ongoing', tag='Ongoing')
EVSEProcessingType.Ongoing_WaitingForCustomerInteraction = EVSEProcessingType._CF_enumeration.addEnumeration(unicode_value='Ongoing_WaitingForCustomerInteraction', tag='Ongoing_WaitingForCustomerInteraction')
EVSEProcessingType._InitializeFacetMap(EVSEProcessingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EVSEProcessingType', EVSEProcessingType)
_module_typeBindings.EVSEProcessingType = EVSEProcessingType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}EVSENotificationType
class EVSENotificationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVSENotificationType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 426, 0)
    _Documentation = None
EVSENotificationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EVSENotificationType, enum_prefix=None)
EVSENotificationType.None_ = EVSENotificationType._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
EVSENotificationType.StopCharging = EVSENotificationType._CF_enumeration.addEnumeration(unicode_value='StopCharging', tag='StopCharging')
EVSENotificationType.ReNegotiation = EVSENotificationType._CF_enumeration.addEnumeration(unicode_value='ReNegotiation', tag='ReNegotiation')
EVSENotificationType._InitializeFacetMap(EVSENotificationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EVSENotificationType', EVSENotificationType)
_module_typeBindings.EVSENotificationType = EVSENotificationType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}chargeProgressType
class chargeProgressType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'chargeProgressType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 433, 0)
    _Documentation = None
chargeProgressType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=chargeProgressType, enum_prefix=None)
chargeProgressType.Start = chargeProgressType._CF_enumeration.addEnumeration(unicode_value='Start', tag='Start')
chargeProgressType.Stop = chargeProgressType._CF_enumeration.addEnumeration(unicode_value='Stop', tag='Stop')
chargeProgressType.Renegotiate = chargeProgressType._CF_enumeration.addEnumeration(unicode_value='Renegotiate', tag='Renegotiate')
chargeProgressType._InitializeFacetMap(chargeProgressType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'chargeProgressType', chargeProgressType)
_module_typeBindings.chargeProgressType = chargeProgressType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}chargingSessionType
class chargingSessionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'chargingSessionType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 440, 0)
    _Documentation = None
chargingSessionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=chargingSessionType, enum_prefix=None)
chargingSessionType.Terminate = chargingSessionType._CF_enumeration.addEnumeration(unicode_value='Terminate', tag='Terminate')
chargingSessionType.Pause = chargingSessionType._CF_enumeration.addEnumeration(unicode_value='Pause', tag='Pause')
chargingSessionType._InitializeFacetMap(chargingSessionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'chargingSessionType', chargingSessionType)
_module_typeBindings.chargingSessionType = chargingSessionType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}serviceNameType
class serviceNameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceNameType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 446, 0)
    _Documentation = None
serviceNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
serviceNameType._InitializeFacetMap(serviceNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'serviceNameType', serviceNameType)
_module_typeBindings.serviceNameType = serviceNameType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}serviceCategoryType
class serviceCategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceCategoryType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 451, 0)
    _Documentation = None
serviceCategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=serviceCategoryType, enum_prefix=None)
serviceCategoryType.EVCharging = serviceCategoryType._CF_enumeration.addEnumeration(unicode_value='EVCharging', tag='EVCharging')
serviceCategoryType.Internet = serviceCategoryType._CF_enumeration.addEnumeration(unicode_value='Internet', tag='Internet')
serviceCategoryType.ContractCertificate = serviceCategoryType._CF_enumeration.addEnumeration(unicode_value='ContractCertificate', tag='ContractCertificate')
serviceCategoryType.OtherCustom = serviceCategoryType._CF_enumeration.addEnumeration(unicode_value='OtherCustom', tag='OtherCustom')
serviceCategoryType._InitializeFacetMap(serviceCategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'serviceCategoryType', serviceCategoryType)
_module_typeBindings.serviceCategoryType = serviceCategoryType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}serviceScopeType
class serviceScopeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceScopeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 459, 0)
    _Documentation = None
serviceScopeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
serviceScopeType._InitializeFacetMap(serviceScopeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'serviceScopeType', serviceScopeType)
_module_typeBindings.serviceScopeType = serviceScopeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}maxNumPhasesType
class maxNumPhasesType (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'maxNumPhasesType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 464, 0)
    _Documentation = None
maxNumPhasesType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=maxNumPhasesType, value=pyxb.binding.datatypes.byte(1))
maxNumPhasesType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=maxNumPhasesType, value=pyxb.binding.datatypes.byte(3))
maxNumPhasesType._InitializeFacetMap(maxNumPhasesType._CF_minInclusive,
   maxNumPhasesType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'maxNumPhasesType', maxNumPhasesType)
_module_typeBindings.maxNumPhasesType = maxNumPhasesType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}valueType
class valueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'valueType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 470, 0)
    _Documentation = None
valueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=valueType, enum_prefix=None)
valueType.bool = valueType._CF_enumeration.addEnumeration(unicode_value='bool', tag='bool')
valueType.byte = valueType._CF_enumeration.addEnumeration(unicode_value='byte', tag='byte')
valueType.short = valueType._CF_enumeration.addEnumeration(unicode_value='short', tag='short')
valueType.int = valueType._CF_enumeration.addEnumeration(unicode_value='int', tag='int')
valueType.physicalValue = valueType._CF_enumeration.addEnumeration(unicode_value='physicalValue', tag='physicalValue')
valueType.string = valueType._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
valueType._InitializeFacetMap(valueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'valueType', valueType)
_module_typeBindings.valueType = valueType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}meterStatusType
class meterStatusType (pyxb.binding.datatypes.short):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 480, 0)
    _Documentation = None
meterStatusType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'meterStatusType', meterStatusType)
_module_typeBindings.meterStatusType = meterStatusType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}EnergyTransferModeType
class EnergyTransferModeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnergyTransferModeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 486, 0)
    _Documentation = None
EnergyTransferModeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EnergyTransferModeType, enum_prefix=None)
EnergyTransferModeType.AC_single_phase_core = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='AC_single_phase_core', tag='AC_single_phase_core')
EnergyTransferModeType.AC_three_phase_core = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='AC_three_phase_core', tag='AC_three_phase_core')
EnergyTransferModeType.DC_core = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='DC_core', tag='DC_core')
EnergyTransferModeType.DC_extended = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='DC_extended', tag='DC_extended')
EnergyTransferModeType.DC_combo_core = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='DC_combo_core', tag='DC_combo_core')
EnergyTransferModeType.DC_unique = EnergyTransferModeType._CF_enumeration.addEnumeration(unicode_value='DC_unique', tag='DC_unique')
EnergyTransferModeType._InitializeFacetMap(EnergyTransferModeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EnergyTransferModeType', EnergyTransferModeType)
_module_typeBindings.EnergyTransferModeType = EnergyTransferModeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}genChallengeType
class genChallengeType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genChallengeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 499, 0)
    _Documentation = None
genChallengeType._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(16))
genChallengeType._InitializeFacetMap(genChallengeType._CF_length)
Namespace.addCategoryObject('typeBinding', 'genChallengeType', genChallengeType)
_module_typeBindings.genChallengeType = genChallengeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}certificateType
class certificateType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'certificateType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 504, 0)
    _Documentation = None
certificateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(800))
certificateType._InitializeFacetMap(certificateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'certificateType', certificateType)
_module_typeBindings.certificateType = certificateType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}dHpublickeyType
class dHpublickeyType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dHpublickeyType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 509, 0)
    _Documentation = None
dHpublickeyType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(65))
dHpublickeyType._InitializeFacetMap(dHpublickeyType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'dHpublickeyType', dHpublickeyType)
_module_typeBindings.dHpublickeyType = dHpublickeyType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}privateKeyType
class privateKeyType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'privateKeyType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 514, 0)
    _Documentation = None
privateKeyType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(48))
privateKeyType._InitializeFacetMap(privateKeyType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'privateKeyType', privateKeyType)
_module_typeBindings.privateKeyType = privateKeyType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}sigMeterReadingType
class sigMeterReadingType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sigMeterReadingType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 519, 0)
    _Documentation = None
sigMeterReadingType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(64))
sigMeterReadingType._InitializeFacetMap(sigMeterReadingType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'sigMeterReadingType', sigMeterReadingType)
_module_typeBindings.sigMeterReadingType = sigMeterReadingType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}sessionIDType
class sessionIDType (pyxb.binding.datatypes.hexBinary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sessionIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 527, 0)
    _Documentation = None
sessionIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
sessionIDType._InitializeFacetMap(sessionIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'sessionIDType', sessionIDType)
_module_typeBindings.sessionIDType = sessionIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}evccIDType
class evccIDType (pyxb.binding.datatypes.hexBinary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'evccIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 532, 0)
    _Documentation = None
evccIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6))
evccIDType._InitializeFacetMap(evccIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'evccIDType', evccIDType)
_module_typeBindings.evccIDType = evccIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}evseIDType
class evseIDType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'evseIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 537, 0)
    _Documentation = None
evseIDType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
evseIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(37))
evseIDType._InitializeFacetMap(evseIDType._CF_minLength,
   evseIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'evseIDType', evseIDType)
_module_typeBindings.evseIDType = evseIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}serviceIDType
class serviceIDType (pyxb.binding.datatypes.unsignedShort):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 543, 0)
    _Documentation = None
serviceIDType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'serviceIDType', serviceIDType)
_module_typeBindings.serviceIDType = serviceIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}eMAIDType
class eMAIDType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eMAIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 546, 0)
    _Documentation = None
eMAIDType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(14))
eMAIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
eMAIDType._InitializeFacetMap(eMAIDType._CF_minLength,
   eMAIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'eMAIDType', eMAIDType)
_module_typeBindings.eMAIDType = eMAIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}meterIDType
class meterIDType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 552, 0)
    _Documentation = None
meterIDType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
meterIDType._InitializeFacetMap(meterIDType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'meterIDType', meterIDType)
_module_typeBindings.meterIDType = meterIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}SAIDType
class SAIDType (pyxb.binding.datatypes.unsignedByte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SAIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 560, 0)
    _Documentation = None
SAIDType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=SAIDType, value=pyxb.binding.datatypes.unsignedByte(1))
SAIDType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=SAIDType, value=pyxb.binding.datatypes.unsignedByte(255))
SAIDType._InitializeFacetMap(SAIDType._CF_minInclusive,
   SAIDType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'SAIDType', SAIDType)
_module_typeBindings.SAIDType = SAIDType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}tariffDescriptionType
class tariffDescriptionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tariffDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 566, 0)
    _Documentation = None
tariffDescriptionType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
tariffDescriptionType._InitializeFacetMap(tariffDescriptionType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tariffDescriptionType', tariffDescriptionType)
_module_typeBindings.tariffDescriptionType = tariffDescriptionType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}costKindType
class costKindType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'costKindType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 571, 0)
    _Documentation = None
costKindType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=costKindType, enum_prefix=None)
costKindType.relativePricePercentage = costKindType._CF_enumeration.addEnumeration(unicode_value='relativePricePercentage', tag='relativePricePercentage')
costKindType.RenewableGenerationPercentage = costKindType._CF_enumeration.addEnumeration(unicode_value='RenewableGenerationPercentage', tag='RenewableGenerationPercentage')
costKindType.CarbonDioxideEmission = costKindType._CF_enumeration.addEnumeration(unicode_value='CarbonDioxideEmission', tag='CarbonDioxideEmission')
costKindType._InitializeFacetMap(costKindType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'costKindType', costKindType)
_module_typeBindings.costKindType = costKindType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}paymentOptionType
class paymentOptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paymentOptionType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 583, 0)
    _Documentation = None
paymentOptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=paymentOptionType, enum_prefix=None)
paymentOptionType.Contract = paymentOptionType._CF_enumeration.addEnumeration(unicode_value='Contract', tag='Contract')
paymentOptionType.ExternalPayment = paymentOptionType._CF_enumeration.addEnumeration(unicode_value='ExternalPayment', tag='ExternalPayment')
paymentOptionType._InitializeFacetMap(paymentOptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'paymentOptionType', paymentOptionType)
_module_typeBindings.paymentOptionType = paymentOptionType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}faultCodeType
class faultCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'faultCodeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 592, 0)
    _Documentation = None
faultCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=faultCodeType, enum_prefix=None)
faultCodeType.ParsingError = faultCodeType._CF_enumeration.addEnumeration(unicode_value='ParsingError', tag='ParsingError')
faultCodeType.NoTLSRootCertificatAvailable = faultCodeType._CF_enumeration.addEnumeration(unicode_value='NoTLSRootCertificatAvailable', tag='NoTLSRootCertificatAvailable')
faultCodeType.UnknownError = faultCodeType._CF_enumeration.addEnumeration(unicode_value='UnknownError', tag='UnknownError')
faultCodeType._InitializeFacetMap(faultCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'faultCodeType', faultCodeType)
_module_typeBindings.faultCodeType = faultCodeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}responseCodeType
class responseCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'responseCodeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 599, 0)
    _Documentation = None
responseCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=responseCodeType, enum_prefix=None)
responseCodeType.OK = responseCodeType._CF_enumeration.addEnumeration(unicode_value='OK', tag='OK')
responseCodeType.OK_NewSessionEstablished = responseCodeType._CF_enumeration.addEnumeration(unicode_value='OK_NewSessionEstablished', tag='OK_NewSessionEstablished')
responseCodeType.OK_OldSessionJoined = responseCodeType._CF_enumeration.addEnumeration(unicode_value='OK_OldSessionJoined', tag='OK_OldSessionJoined')
responseCodeType.OK_CertificateExpiresSoon = responseCodeType._CF_enumeration.addEnumeration(unicode_value='OK_CertificateExpiresSoon', tag='OK_CertificateExpiresSoon')
responseCodeType.FAILED = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED', tag='FAILED')
responseCodeType.FAILED_SequenceError = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_SequenceError', tag='FAILED_SequenceError')
responseCodeType.FAILED_ServiceIDInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ServiceIDInvalid', tag='FAILED_ServiceIDInvalid')
responseCodeType.FAILED_UnknownSession = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_UnknownSession', tag='FAILED_UnknownSession')
responseCodeType.FAILED_ServiceSelectionInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ServiceSelectionInvalid', tag='FAILED_ServiceSelectionInvalid')
responseCodeType.FAILED_PaymentSelectionInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_PaymentSelectionInvalid', tag='FAILED_PaymentSelectionInvalid')
responseCodeType.FAILED_CertificateExpired = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_CertificateExpired', tag='FAILED_CertificateExpired')
responseCodeType.FAILED_SignatureError = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_SignatureError', tag='FAILED_SignatureError')
responseCodeType.FAILED_NoCertificateAvailable = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_NoCertificateAvailable', tag='FAILED_NoCertificateAvailable')
responseCodeType.FAILED_CertChainError = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_CertChainError', tag='FAILED_CertChainError')
responseCodeType.FAILED_ChallengeInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChallengeInvalid', tag='FAILED_ChallengeInvalid')
responseCodeType.FAILED_ContractCanceled = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ContractCanceled', tag='FAILED_ContractCanceled')
responseCodeType.FAILED_WrongChargeParameter = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_WrongChargeParameter', tag='FAILED_WrongChargeParameter')
responseCodeType.FAILED_PowerDeliveryNotApplied = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_PowerDeliveryNotApplied', tag='FAILED_PowerDeliveryNotApplied')
responseCodeType.FAILED_TariffSelectionInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_TariffSelectionInvalid', tag='FAILED_TariffSelectionInvalid')
responseCodeType.FAILED_ChargingProfileInvalid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChargingProfileInvalid', tag='FAILED_ChargingProfileInvalid')
responseCodeType.FAILED_MeteringSignatureNotValid = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_MeteringSignatureNotValid', tag='FAILED_MeteringSignatureNotValid')
responseCodeType.FAILED_NoChargeServiceSelected = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_NoChargeServiceSelected', tag='FAILED_NoChargeServiceSelected')
responseCodeType.FAILED_WrongEnergyTransferMode = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_WrongEnergyTransferMode', tag='FAILED_WrongEnergyTransferMode')
responseCodeType.FAILED_ContactorError = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ContactorError', tag='FAILED_ContactorError')
responseCodeType.FAILED_CertificateNotAllowedAtThisEVSE = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_CertificateNotAllowedAtThisEVSE', tag='FAILED_CertificateNotAllowedAtThisEVSE')
responseCodeType.FAILED_CertificateRevoked = responseCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_CertificateRevoked', tag='FAILED_CertificateRevoked')
responseCodeType._InitializeFacetMap(responseCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'responseCodeType', responseCodeType)
_module_typeBindings.responseCodeType = responseCodeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}unitMultiplierType
class unitMultiplierType (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitMultiplierType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 632, 0)
    _Documentation = None
unitMultiplierType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=unitMultiplierType, value=pyxb.binding.datatypes.byte(-3))
unitMultiplierType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=unitMultiplierType, value=pyxb.binding.datatypes.byte(3))
unitMultiplierType._InitializeFacetMap(unitMultiplierType._CF_minInclusive,
   unitMultiplierType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'unitMultiplierType', unitMultiplierType)
_module_typeBindings.unitMultiplierType = unitMultiplierType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}unitSymbolType
class unitSymbolType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitSymbolType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 638, 0)
    _Documentation = None
unitSymbolType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=unitSymbolType, enum_prefix=None)
unitSymbolType.h = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='h', tag='h')
unitSymbolType.m = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
unitSymbolType.s = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='s', tag='s')
unitSymbolType.A = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
unitSymbolType.V = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
unitSymbolType.W = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
unitSymbolType.Wh = unitSymbolType._CF_enumeration.addEnumeration(unicode_value='Wh', tag='Wh')
unitSymbolType._InitializeFacetMap(unitSymbolType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'unitSymbolType', unitSymbolType)
_module_typeBindings.unitSymbolType = unitSymbolType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEStatusCodeType
class DC_EVSEStatusCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatusCodeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 680, 0)
    _Documentation = None
DC_EVSEStatusCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DC_EVSEStatusCodeType, enum_prefix=None)
DC_EVSEStatusCodeType.EVSE_NotReady = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_NotReady', tag='EVSE_NotReady')
DC_EVSEStatusCodeType.EVSE_Ready = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_Ready', tag='EVSE_Ready')
DC_EVSEStatusCodeType.EVSE_Shutdown = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_Shutdown', tag='EVSE_Shutdown')
DC_EVSEStatusCodeType.EVSE_UtilityInterruptEvent = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_UtilityInterruptEvent', tag='EVSE_UtilityInterruptEvent')
DC_EVSEStatusCodeType.EVSE_IsolationMonitoringActive = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_IsolationMonitoringActive', tag='EVSE_IsolationMonitoringActive')
DC_EVSEStatusCodeType.EVSE_EmergencyShutdown = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_EmergencyShutdown', tag='EVSE_EmergencyShutdown')
DC_EVSEStatusCodeType.EVSE_Malfunction = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='EVSE_Malfunction', tag='EVSE_Malfunction')
DC_EVSEStatusCodeType.Reserved_8 = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_8', tag='Reserved_8')
DC_EVSEStatusCodeType.Reserved_9 = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_9', tag='Reserved_9')
DC_EVSEStatusCodeType.Reserved_A = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_A', tag='Reserved_A')
DC_EVSEStatusCodeType.Reserved_B = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_B', tag='Reserved_B')
DC_EVSEStatusCodeType.Reserved_C = DC_EVSEStatusCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_C', tag='Reserved_C')
DC_EVSEStatusCodeType._InitializeFacetMap(DC_EVSEStatusCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DC_EVSEStatusCodeType', DC_EVSEStatusCodeType)
_module_typeBindings.DC_EVSEStatusCodeType = DC_EVSEStatusCodeType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}isolationLevelType
class isolationLevelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'isolationLevelType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 696, 0)
    _Documentation = None
isolationLevelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=isolationLevelType, enum_prefix=None)
isolationLevelType.Invalid = isolationLevelType._CF_enumeration.addEnumeration(unicode_value='Invalid', tag='Invalid')
isolationLevelType.Valid = isolationLevelType._CF_enumeration.addEnumeration(unicode_value='Valid', tag='Valid')
isolationLevelType.Warning = isolationLevelType._CF_enumeration.addEnumeration(unicode_value='Warning', tag='Warning')
isolationLevelType.Fault = isolationLevelType._CF_enumeration.addEnumeration(unicode_value='Fault', tag='Fault')
isolationLevelType.No_IMD = isolationLevelType._CF_enumeration.addEnumeration(unicode_value='No_IMD', tag='No_IMD')
isolationLevelType._InitializeFacetMap(isolationLevelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'isolationLevelType', isolationLevelType)
_module_typeBindings.isolationLevelType = isolationLevelType

# Atomic simple type: {urn:iso:15118:2:2013:MsgDataTypes}DC_EVErrorCodeType
class DC_EVErrorCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVErrorCodeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 705, 0)
    _Documentation = None
DC_EVErrorCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DC_EVErrorCodeType, enum_prefix=None)
DC_EVErrorCodeType.NO_ERROR = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='NO_ERROR', tag='NO_ERROR')
DC_EVErrorCodeType.FAILED_RESSTemperatureInhibit = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_RESSTemperatureInhibit', tag='FAILED_RESSTemperatureInhibit')
DC_EVErrorCodeType.FAILED_EVShiftPosition = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_EVShiftPosition', tag='FAILED_EVShiftPosition')
DC_EVErrorCodeType.FAILED_ChargerConnectorLockFault = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChargerConnectorLockFault', tag='FAILED_ChargerConnectorLockFault')
DC_EVErrorCodeType.FAILED_EVRESSMalfunction = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_EVRESSMalfunction', tag='FAILED_EVRESSMalfunction')
DC_EVErrorCodeType.FAILED_ChargingCurrentdifferential = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChargingCurrentdifferential', tag='FAILED_ChargingCurrentdifferential')
DC_EVErrorCodeType.FAILED_ChargingVoltageOutOfRange = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChargingVoltageOutOfRange', tag='FAILED_ChargingVoltageOutOfRange')
DC_EVErrorCodeType.Reserved_A = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_A', tag='Reserved_A')
DC_EVErrorCodeType.Reserved_B = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_B', tag='Reserved_B')
DC_EVErrorCodeType.Reserved_C = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='Reserved_C', tag='Reserved_C')
DC_EVErrorCodeType.FAILED_ChargingSystemIncompatibility = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='FAILED_ChargingSystemIncompatibility', tag='FAILED_ChargingSystemIncompatibility')
DC_EVErrorCodeType.NoData = DC_EVErrorCodeType._CF_enumeration.addEnumeration(unicode_value='NoData', tag='NoData')
DC_EVErrorCodeType._InitializeFacetMap(DC_EVErrorCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DC_EVErrorCodeType', DC_EVErrorCodeType)
_module_typeBindings.DC_EVErrorCodeType = DC_EVErrorCodeType

# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceType with content type ELEMENT_ONLY
class ServiceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 14, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ServiceID uses Python identifier ServiceID
    __ServiceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), 'ServiceID', '__urniso1511822013MsgDataTypes_ServiceType_urniso1511822013MsgDataTypesServiceID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 16, 0), )

    
    ServiceID = property(__ServiceID.value, __ServiceID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ServiceName uses Python identifier ServiceName
    __ServiceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceName'), 'ServiceName', '__urniso1511822013MsgDataTypes_ServiceType_urniso1511822013MsgDataTypesServiceName', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0), )

    
    ServiceName = property(__ServiceName.value, __ServiceName.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ServiceCategory uses Python identifier ServiceCategory
    __ServiceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory'), 'ServiceCategory', '__urniso1511822013MsgDataTypes_ServiceType_urniso1511822013MsgDataTypesServiceCategory', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 18, 0), )

    
    ServiceCategory = property(__ServiceCategory.value, __ServiceCategory.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ServiceScope uses Python identifier ServiceScope
    __ServiceScope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope'), 'ServiceScope', '__urniso1511822013MsgDataTypes_ServiceType_urniso1511822013MsgDataTypesServiceScope', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0), )

    
    ServiceScope = property(__ServiceScope.value, __ServiceScope.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}FreeService uses Python identifier FreeService
    __FreeService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FreeService'), 'FreeService', '__urniso1511822013MsgDataTypes_ServiceType_urniso1511822013MsgDataTypesFreeService', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 20, 0), )

    
    FreeService = property(__FreeService.value, __FreeService.set, None, None)

    _ElementMap.update({
        __ServiceID.name() : __ServiceID,
        __ServiceName.name() : __ServiceName,
        __ServiceCategory.name() : __ServiceCategory,
        __ServiceScope.name() : __ServiceScope,
        __FreeService.name() : __FreeService
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceType = ServiceType
Namespace.addCategoryObject('typeBinding', 'ServiceType', ServiceType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceListType with content type ELEMENT_ONLY
class ServiceListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceListType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 23, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Service'), 'Service', '__urniso1511822013MsgDataTypes_ServiceListType_urniso1511822013MsgDataTypesService', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 25, 0), )

    
    Service = property(__Service.value, __Service.set, None, None)

    _ElementMap.update({
        __Service.name() : __Service
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceListType = ServiceListType
Namespace.addCategoryObject('typeBinding', 'ServiceListType', ServiceListType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SelectedServiceListType with content type ELEMENT_ONLY
class SelectedServiceListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SelectedServiceListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SelectedServiceListType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 28, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SelectedService uses Python identifier SelectedService
    __SelectedService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SelectedService'), 'SelectedService', '__urniso1511822013MsgDataTypes_SelectedServiceListType_urniso1511822013MsgDataTypesSelectedService', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 30, 0), )

    
    SelectedService = property(__SelectedService.value, __SelectedService.set, None, None)

    _ElementMap.update({
        __SelectedService.name() : __SelectedService
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SelectedServiceListType = SelectedServiceListType
Namespace.addCategoryObject('typeBinding', 'SelectedServiceListType', SelectedServiceListType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SelectedServiceType with content type ELEMENT_ONLY
class SelectedServiceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SelectedServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SelectedServiceType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 33, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ServiceID uses Python identifier ServiceID
    __ServiceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), 'ServiceID', '__urniso1511822013MsgDataTypes_SelectedServiceType_urniso1511822013MsgDataTypesServiceID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 35, 0), )

    
    ServiceID = property(__ServiceID.value, __ServiceID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ParameterSetID uses Python identifier ParameterSetID
    __ParameterSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID'), 'ParameterSetID', '__urniso1511822013MsgDataTypes_SelectedServiceType_urniso1511822013MsgDataTypesParameterSetID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 36, 0), )

    
    ParameterSetID = property(__ParameterSetID.value, __ParameterSetID.set, None, None)

    _ElementMap.update({
        __ServiceID.name() : __ServiceID,
        __ParameterSetID.name() : __ParameterSetID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SelectedServiceType = SelectedServiceType
Namespace.addCategoryObject('typeBinding', 'SelectedServiceType', SelectedServiceType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceParameterListType with content type ELEMENT_ONLY
class ServiceParameterListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ServiceParameterListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceParameterListType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 39, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ParameterSet uses Python identifier ParameterSet
    __ParameterSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterSet'), 'ParameterSet', '__urniso1511822013MsgDataTypes_ServiceParameterListType_urniso1511822013MsgDataTypesParameterSet', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 41, 0), )

    
    ParameterSet = property(__ParameterSet.value, __ParameterSet.set, None, None)

    _ElementMap.update({
        __ParameterSet.name() : __ParameterSet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceParameterListType = ServiceParameterListType
Namespace.addCategoryObject('typeBinding', 'ServiceParameterListType', ServiceParameterListType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ParameterSetType with content type ELEMENT_ONLY
class ParameterSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ParameterSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterSetType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 44, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ParameterSetID uses Python identifier ParameterSetID
    __ParameterSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID'), 'ParameterSetID', '__urniso1511822013MsgDataTypes_ParameterSetType_urniso1511822013MsgDataTypesParameterSetID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 46, 0), )

    
    ParameterSetID = property(__ParameterSetID.value, __ParameterSetID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), 'Parameter', '__urniso1511822013MsgDataTypes_ParameterSetType_urniso1511822013MsgDataTypesParameter', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 47, 0), )

    
    Parameter = property(__Parameter.value, __Parameter.set, None, None)

    _ElementMap.update({
        __ParameterSetID.name() : __ParameterSetID,
        __Parameter.name() : __Parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ParameterSetType = ParameterSetType
Namespace.addCategoryObject('typeBinding', 'ParameterSetType', ParameterSetType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ParameterType with content type ELEMENT_ONLY
class ParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 50, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}boolValue uses Python identifier boolValue
    __boolValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boolValue'), 'boolValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesboolValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 52, 0), )

    
    boolValue = property(__boolValue.value, __boolValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}byteValue uses Python identifier byteValue
    __byteValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'byteValue'), 'byteValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesbyteValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 53, 0), )

    
    byteValue = property(__byteValue.value, __byteValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}shortValue uses Python identifier shortValue
    __shortValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shortValue'), 'shortValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesshortValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 54, 0), )

    
    shortValue = property(__shortValue.value, __shortValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}intValue uses Python identifier intValue
    __intValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intValue'), 'intValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesintValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 55, 0), )

    
    intValue = property(__intValue.value, __intValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}physicalValue uses Python identifier physicalValue
    __physicalValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'physicalValue'), 'physicalValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesphysicalValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 56, 0), )

    
    physicalValue = property(__physicalValue.value, __physicalValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}stringValue uses Python identifier stringValue
    __stringValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stringValue'), 'stringValue', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesstringValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 57, 0), )

    
    stringValue = property(__stringValue.value, __stringValue.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__urniso1511822013MsgDataTypes_ParameterType_urniso1511822013MsgDataTypesName', pyxb.binding.datatypes.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 59, 0)
    __Name._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 59, 0)
    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        __boolValue.name() : __boolValue,
        __byteValue.name() : __byteValue,
        __shortValue.name() : __shortValue,
        __intValue.name() : __intValue,
        __physicalValue.name() : __physicalValue,
        __stringValue.name() : __stringValue
    })
    _AttributeMap.update({
        __Name.name() : __Name
    })
_module_typeBindings.ParameterType = ParameterType
Namespace.addCategoryObject('typeBinding', 'ParameterType', ParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SupportedEnergyTransferModeType with content type ELEMENT_ONLY
class SupportedEnergyTransferModeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SupportedEnergyTransferModeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedEnergyTransferModeType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 70, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EnergyTransferMode uses Python identifier EnergyTransferMode
    __EnergyTransferMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EnergyTransferMode'), 'EnergyTransferMode', '__urniso1511822013MsgDataTypes_SupportedEnergyTransferModeType_urniso1511822013MsgDataTypesEnergyTransferMode', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 72, 0), )

    
    EnergyTransferMode = property(__EnergyTransferMode.value, __EnergyTransferMode.set, None, None)

    _ElementMap.update({
        __EnergyTransferMode.name() : __EnergyTransferMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SupportedEnergyTransferModeType = SupportedEnergyTransferModeType
Namespace.addCategoryObject('typeBinding', 'SupportedEnergyTransferModeType', SupportedEnergyTransferModeType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}CertificateChainType with content type ELEMENT_ONLY
class CertificateChainType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}CertificateChainType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateChainType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 99, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Certificate uses Python identifier Certificate
    __Certificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Certificate'), 'Certificate', '__urniso1511822013MsgDataTypes_CertificateChainType_urniso1511822013MsgDataTypesCertificate', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 101, 0), )

    
    Certificate = property(__Certificate.value, __Certificate.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SubCertificates uses Python identifier SubCertificates
    __SubCertificates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubCertificates'), 'SubCertificates', '__urniso1511822013MsgDataTypes_CertificateChainType_urniso1511822013MsgDataTypesSubCertificates', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 102, 0), )

    
    SubCertificates = property(__SubCertificates.value, __SubCertificates.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgDataTypes_CertificateChainType_urniso1511822013MsgDataTypesId', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 104, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 104, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Certificate.name() : __Certificate,
        __SubCertificates.name() : __SubCertificates
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CertificateChainType = CertificateChainType
Namespace.addCategoryObject('typeBinding', 'CertificateChainType', CertificateChainType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SubCertificatesType with content type ELEMENT_ONLY
class SubCertificatesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SubCertificatesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubCertificatesType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 106, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Certificate uses Python identifier Certificate
    __Certificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Certificate'), 'Certificate', '__urniso1511822013MsgDataTypes_SubCertificatesType_urniso1511822013MsgDataTypesCertificate', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 108, 0), )

    
    Certificate = property(__Certificate.value, __Certificate.set, None, None)

    _ElementMap.update({
        __Certificate.name() : __Certificate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubCertificatesType = SubCertificatesType
Namespace.addCategoryObject('typeBinding', 'SubCertificatesType', SubCertificatesType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ListOfRootCertificateIDsType with content type ELEMENT_ONLY
class ListOfRootCertificateIDsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ListOfRootCertificateIDsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDsType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 111, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}RootCertificateID uses Python identifier RootCertificateID
    __RootCertificateID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RootCertificateID'), 'RootCertificateID', '__urniso1511822013MsgDataTypes_ListOfRootCertificateIDsType_urniso1511822013MsgDataTypesRootCertificateID', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 113, 0), )

    
    RootCertificateID = property(__RootCertificateID.value, __RootCertificateID.set, None, None)

    _ElementMap.update({
        __RootCertificateID.name() : __RootCertificateID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ListOfRootCertificateIDsType = ListOfRootCertificateIDsType
Namespace.addCategoryObject('typeBinding', 'ListOfRootCertificateIDsType', ListOfRootCertificateIDsType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}MeterInfoType with content type ELEMENT_ONLY
class MeterInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}MeterInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeterInfoType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 119, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}MeterID uses Python identifier MeterID
    __MeterID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterID'), 'MeterID', '__urniso1511822013MsgDataTypes_MeterInfoType_urniso1511822013MsgDataTypesMeterID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 121, 0), )

    
    MeterID = property(__MeterID.value, __MeterID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}MeterReading uses Python identifier MeterReading
    __MeterReading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterReading'), 'MeterReading', '__urniso1511822013MsgDataTypes_MeterInfoType_urniso1511822013MsgDataTypesMeterReading', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 122, 0), )

    
    MeterReading = property(__MeterReading.value, __MeterReading.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SigMeterReading uses Python identifier SigMeterReading
    __SigMeterReading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigMeterReading'), 'SigMeterReading', '__urniso1511822013MsgDataTypes_MeterInfoType_urniso1511822013MsgDataTypesSigMeterReading', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 123, 0), )

    
    SigMeterReading = property(__SigMeterReading.value, __SigMeterReading.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}MeterStatus uses Python identifier MeterStatus
    __MeterStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterStatus'), 'MeterStatus', '__urniso1511822013MsgDataTypes_MeterInfoType_urniso1511822013MsgDataTypesMeterStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 124, 0), )

    
    MeterStatus = property(__MeterStatus.value, __MeterStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}TMeter uses Python identifier TMeter
    __TMeter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TMeter'), 'TMeter', '__urniso1511822013MsgDataTypes_MeterInfoType_urniso1511822013MsgDataTypesTMeter', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 125, 0), )

    
    TMeter = property(__TMeter.value, __TMeter.set, None, None)

    _ElementMap.update({
        __MeterID.name() : __MeterID,
        __MeterReading.name() : __MeterReading,
        __SigMeterReading.name() : __SigMeterReading,
        __MeterStatus.name() : __MeterStatus,
        __TMeter.name() : __TMeter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeterInfoType = MeterInfoType
Namespace.addCategoryObject('typeBinding', 'MeterInfoType', MeterInfoType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}PhysicalValueType with content type ELEMENT_ONLY
class PhysicalValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}PhysicalValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalValueType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 131, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Multiplier uses Python identifier Multiplier
    __Multiplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Multiplier'), 'Multiplier', '__urniso1511822013MsgDataTypes_PhysicalValueType_urniso1511822013MsgDataTypesMultiplier', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 133, 0), )

    
    Multiplier = property(__Multiplier.value, __Multiplier.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Unit uses Python identifier Unit
    __Unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Unit'), 'Unit', '__urniso1511822013MsgDataTypes_PhysicalValueType_urniso1511822013MsgDataTypesUnit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 134, 0), )

    
    Unit = property(__Unit.value, __Unit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__urniso1511822013MsgDataTypes_PhysicalValueType_urniso1511822013MsgDataTypesValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 135, 0), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Multiplier.name() : __Multiplier,
        __Unit.name() : __Unit,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PhysicalValueType = PhysicalValueType
Namespace.addCategoryObject('typeBinding', 'PhysicalValueType', PhysicalValueType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}NotificationType with content type ELEMENT_ONLY
class NotificationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}NotificationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NotificationType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 141, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}FaultCode uses Python identifier FaultCode
    __FaultCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FaultCode'), 'FaultCode', '__urniso1511822013MsgDataTypes_NotificationType_urniso1511822013MsgDataTypesFaultCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 143, 0), )

    
    FaultCode = property(__FaultCode.value, __FaultCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}FaultMsg uses Python identifier FaultMsg
    __FaultMsg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FaultMsg'), 'FaultMsg', '__urniso1511822013MsgDataTypes_NotificationType_urniso1511822013MsgDataTypesFaultMsg', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 144, 0), )

    
    FaultMsg = property(__FaultMsg.value, __FaultMsg.set, None, None)

    _ElementMap.update({
        __FaultCode.name() : __FaultCode,
        __FaultMsg.name() : __FaultMsg
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NotificationType = NotificationType
Namespace.addCategoryObject('typeBinding', 'NotificationType', NotificationType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SASchedulesType with content type EMPTY
class SASchedulesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SASchedulesType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SASchedulesType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 150, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SASchedulesType = SASchedulesType
Namespace.addCategoryObject('typeBinding', 'SASchedulesType', SASchedulesType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleTupleType with content type ELEMENT_ONLY
class SAScheduleTupleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleTupleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 162, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleTupleID uses Python identifier SAScheduleTupleID
    __SAScheduleTupleID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), 'SAScheduleTupleID', '__urniso1511822013MsgDataTypes_SAScheduleTupleType_urniso1511822013MsgDataTypesSAScheduleTupleID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 164, 0), )

    
    SAScheduleTupleID = property(__SAScheduleTupleID.value, __SAScheduleTupleID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}PMaxSchedule uses Python identifier PMaxSchedule
    __PMaxSchedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PMaxSchedule'), 'PMaxSchedule', '__urniso1511822013MsgDataTypes_SAScheduleTupleType_urniso1511822013MsgDataTypesPMaxSchedule', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 165, 0), )

    
    PMaxSchedule = property(__PMaxSchedule.value, __PMaxSchedule.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SalesTariff uses Python identifier SalesTariff
    __SalesTariff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SalesTariff'), 'SalesTariff', '__urniso1511822013MsgDataTypes_SAScheduleTupleType_urniso1511822013MsgDataTypesSalesTariff', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 166, 0), )

    
    SalesTariff = property(__SalesTariff.value, __SalesTariff.set, None, None)

    _ElementMap.update({
        __SAScheduleTupleID.name() : __SAScheduleTupleID,
        __PMaxSchedule.name() : __PMaxSchedule,
        __SalesTariff.name() : __SalesTariff
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SAScheduleTupleType = SAScheduleTupleType
Namespace.addCategoryObject('typeBinding', 'SAScheduleTupleType', SAScheduleTupleType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffType with content type ELEMENT_ONLY
class SalesTariffType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SalesTariffType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 169, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffID uses Python identifier SalesTariffID
    __SalesTariffID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffID'), 'SalesTariffID', '__urniso1511822013MsgDataTypes_SalesTariffType_urniso1511822013MsgDataTypesSalesTariffID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 171, 0), )

    
    SalesTariffID = property(__SalesTariffID.value, __SalesTariffID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffDescription uses Python identifier SalesTariffDescription
    __SalesTariffDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffDescription'), 'SalesTariffDescription', '__urniso1511822013MsgDataTypes_SalesTariffType_urniso1511822013MsgDataTypesSalesTariffDescription', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 172, 0), )

    
    SalesTariffDescription = property(__SalesTariffDescription.value, __SalesTariffDescription.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}NumEPriceLevels uses Python identifier NumEPriceLevels
    __NumEPriceLevels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumEPriceLevels'), 'NumEPriceLevels', '__urniso1511822013MsgDataTypes_SalesTariffType_urniso1511822013MsgDataTypesNumEPriceLevels', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 173, 0), )

    
    NumEPriceLevels = property(__NumEPriceLevels.value, __NumEPriceLevels.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffEntry uses Python identifier SalesTariffEntry
    __SalesTariffEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffEntry'), 'SalesTariffEntry', '__urniso1511822013MsgDataTypes_SalesTariffType_urniso1511822013MsgDataTypesSalesTariffEntry', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 189, 0), )

    
    SalesTariffEntry = property(__SalesTariffEntry.value, __SalesTariffEntry.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgDataTypes_SalesTariffType_urniso1511822013MsgDataTypesId', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 176, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 176, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SalesTariffID.name() : __SalesTariffID,
        __SalesTariffDescription.name() : __SalesTariffDescription,
        __NumEPriceLevels.name() : __NumEPriceLevels,
        __SalesTariffEntry.name() : __SalesTariffEntry
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.SalesTariffType = SalesTariffType
Namespace.addCategoryObject('typeBinding', 'SalesTariffType', SalesTariffType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}PMaxScheduleType with content type ELEMENT_ONLY
class PMaxScheduleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}PMaxScheduleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 178, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}PMaxScheduleEntry uses Python identifier PMaxScheduleEntry
    __PMaxScheduleEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleEntry'), 'PMaxScheduleEntry', '__urniso1511822013MsgDataTypes_PMaxScheduleType_urniso1511822013MsgDataTypesPMaxScheduleEntry', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 200, 0), )

    
    PMaxScheduleEntry = property(__PMaxScheduleEntry.value, __PMaxScheduleEntry.set, None, None)

    _ElementMap.update({
        __PMaxScheduleEntry.name() : __PMaxScheduleEntry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PMaxScheduleType = PMaxScheduleType
Namespace.addCategoryObject('typeBinding', 'PMaxScheduleType', PMaxScheduleType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EntryType with content type ELEMENT_ONLY
class EntryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EntryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EntryType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 184, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}TimeInterval uses Python identifier TimeInterval
    __TimeInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval'), 'TimeInterval', '__urniso1511822013MsgDataTypes_EntryType_urniso1511822013MsgDataTypesTimeInterval', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 211, 0), )

    
    TimeInterval = property(__TimeInterval.value, __TimeInterval.set, None, None)

    _ElementMap.update({
        __TimeInterval.name() : __TimeInterval
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EntryType = EntryType
Namespace.addCategoryObject('typeBinding', 'EntryType', EntryType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}IntervalType with content type EMPTY
class IntervalType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}IntervalType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntervalType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 210, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IntervalType = IntervalType
Namespace.addCategoryObject('typeBinding', 'IntervalType', IntervalType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ConsumptionCostType with content type ELEMENT_ONLY
class ConsumptionCostType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ConsumptionCostType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConsumptionCostType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 237, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}startValue uses Python identifier startValue
    __startValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startValue'), 'startValue', '__urniso1511822013MsgDataTypes_ConsumptionCostType_urniso1511822013MsgDataTypesstartValue', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 239, 0), )

    
    startValue = property(__startValue.value, __startValue.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}Cost uses Python identifier Cost
    __Cost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cost'), 'Cost', '__urniso1511822013MsgDataTypes_ConsumptionCostType_urniso1511822013MsgDataTypesCost', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 240, 0), )

    
    Cost = property(__Cost.value, __Cost.set, None, None)

    _ElementMap.update({
        __startValue.name() : __startValue,
        __Cost.name() : __Cost
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConsumptionCostType = ConsumptionCostType
Namespace.addCategoryObject('typeBinding', 'ConsumptionCostType', ConsumptionCostType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}CostType with content type ELEMENT_ONLY
class CostType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}CostType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CostType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 243, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}costKind uses Python identifier costKind
    __costKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'costKind'), 'costKind', '__urniso1511822013MsgDataTypes_CostType_urniso1511822013MsgDataTypescostKind', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 245, 0), )

    
    costKind = property(__costKind.value, __costKind.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amount'), 'amount', '__urniso1511822013MsgDataTypes_CostType_urniso1511822013MsgDataTypesamount', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 246, 0), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}amountMultiplier uses Python identifier amountMultiplier
    __amountMultiplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amountMultiplier'), 'amountMultiplier', '__urniso1511822013MsgDataTypes_CostType_urniso1511822013MsgDataTypesamountMultiplier', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 247, 0), )

    
    amountMultiplier = property(__amountMultiplier.value, __amountMultiplier.set, None, None)

    _ElementMap.update({
        __costKind.name() : __costKind,
        __amount.name() : __amount,
        __amountMultiplier.name() : __amountMultiplier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CostType = CostType
Namespace.addCategoryObject('typeBinding', 'CostType', CostType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType with content type ELEMENT_ONLY
class EVSEStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVSEStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 253, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}NotificationMaxDelay uses Python identifier NotificationMaxDelay
    __NotificationMaxDelay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotificationMaxDelay'), 'NotificationMaxDelay', '__urniso1511822013MsgDataTypes_EVSEStatusType_urniso1511822013MsgDataTypesNotificationMaxDelay', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 255, 0), )

    
    NotificationMaxDelay = property(__NotificationMaxDelay.value, __NotificationMaxDelay.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSENotification uses Python identifier EVSENotification
    __EVSENotification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSENotification'), 'EVSENotification', '__urniso1511822013MsgDataTypes_EVSEStatusType_urniso1511822013MsgDataTypesEVSENotification', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 256, 0), )

    
    EVSENotification = property(__EVSENotification.value, __EVSENotification.set, None, None)

    _ElementMap.update({
        __NotificationMaxDelay.name() : __NotificationMaxDelay,
        __EVSENotification.name() : __EVSENotification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EVSEStatusType = EVSEStatusType
Namespace.addCategoryObject('typeBinding', 'EVSEStatusType', EVSEStatusType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVStatusType with content type EMPTY
class EVStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVStatusType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 270, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EVStatusType = EVStatusType
Namespace.addCategoryObject('typeBinding', 'EVStatusType', EVStatusType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVChargeParameterType with content type ELEMENT_ONLY
class EVChargeParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVChargeParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 298, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}DepartureTime uses Python identifier DepartureTime
    __DepartureTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DepartureTime'), 'DepartureTime', '__urniso1511822013MsgDataTypes_EVChargeParameterType_urniso1511822013MsgDataTypesDepartureTime', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0), )

    
    DepartureTime = property(__DepartureTime.value, __DepartureTime.set, None, None)

    _ElementMap.update({
        __DepartureTime.name() : __DepartureTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EVChargeParameterType = EVChargeParameterType
Namespace.addCategoryObject('typeBinding', 'EVChargeParameterType', EVChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVSEChargeParameterType with content type EMPTY
class EVSEChargeParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVSEChargeParameterType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVSEChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 334, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EVSEChargeParameterType = EVSEChargeParameterType
Namespace.addCategoryObject('typeBinding', 'EVSEChargeParameterType', EVSEChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVPowerDeliveryParameterType with content type EMPTY
class EVPowerDeliveryParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EVPowerDeliveryParameterType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EVPowerDeliveryParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 370, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EVPowerDeliveryParameterType = EVPowerDeliveryParameterType
Namespace.addCategoryObject('typeBinding', 'EVPowerDeliveryParameterType', EVPowerDeliveryParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ChargingProfileType with content type ELEMENT_ONLY
class ChargingProfileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ChargingProfileType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 387, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ProfileEntry uses Python identifier ProfileEntry
    __ProfileEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProfileEntry'), 'ProfileEntry', '__urniso1511822013MsgDataTypes_ChargingProfileType_urniso1511822013MsgDataTypesProfileEntry', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 389, 0), )

    
    ProfileEntry = property(__ProfileEntry.value, __ProfileEntry.set, None, None)

    _ElementMap.update({
        __ProfileEntry.name() : __ProfileEntry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargingProfileType = ChargingProfileType
Namespace.addCategoryObject('typeBinding', 'ChargingProfileType', ChargingProfileType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ProfileEntryType with content type ELEMENT_ONLY
class ProfileEntryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ProfileEntryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProfileEntryType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 392, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ChargingProfileEntryStart uses Python identifier ChargingProfileEntryStart
    __ChargingProfileEntryStart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryStart'), 'ChargingProfileEntryStart', '__urniso1511822013MsgDataTypes_ProfileEntryType_urniso1511822013MsgDataTypesChargingProfileEntryStart', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 394, 0), )

    
    ChargingProfileEntryStart = property(__ChargingProfileEntryStart.value, __ChargingProfileEntryStart.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ChargingProfileEntryMaxPower uses Python identifier ChargingProfileEntryMaxPower
    __ChargingProfileEntryMaxPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxPower'), 'ChargingProfileEntryMaxPower', '__urniso1511822013MsgDataTypes_ProfileEntryType_urniso1511822013MsgDataTypesChargingProfileEntryMaxPower', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 396, 0), )

    
    ChargingProfileEntryMaxPower = property(__ChargingProfileEntryMaxPower.value, __ChargingProfileEntryMaxPower.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ChargingProfileEntryMaxNumberOfPhasesInUse uses Python identifier ChargingProfileEntryMaxNumberOfPhasesInUse
    __ChargingProfileEntryMaxNumberOfPhasesInUse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxNumberOfPhasesInUse'), 'ChargingProfileEntryMaxNumberOfPhasesInUse', '__urniso1511822013MsgDataTypes_ProfileEntryType_urniso1511822013MsgDataTypesChargingProfileEntryMaxNumberOfPhasesInUse', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 398, 0), )

    
    ChargingProfileEntryMaxNumberOfPhasesInUse = property(__ChargingProfileEntryMaxNumberOfPhasesInUse.value, __ChargingProfileEntryMaxNumberOfPhasesInUse.set, None, None)

    _ElementMap.update({
        __ChargingProfileEntryStart.name() : __ChargingProfileEntryStart,
        __ChargingProfileEntryMaxPower.name() : __ChargingProfileEntryMaxPower,
        __ChargingProfileEntryMaxNumberOfPhasesInUse.name() : __ChargingProfileEntryMaxNumberOfPhasesInUse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProfileEntryType = ProfileEntryType
Namespace.addCategoryObject('typeBinding', 'ProfileEntryType', ProfileEntryType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}PaymentOptionListType with content type ELEMENT_ONLY
class PaymentOptionListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}PaymentOptionListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionListType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 578, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}PaymentOption uses Python identifier PaymentOption
    __PaymentOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PaymentOption'), 'PaymentOption', '__urniso1511822013MsgDataTypes_PaymentOptionListType_urniso1511822013MsgDataTypesPaymentOption', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 580, 0), )

    
    PaymentOption = property(__PaymentOption.value, __PaymentOption.set, None, None)

    _ElementMap.update({
        __PaymentOption.name() : __PaymentOption
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentOptionListType = PaymentOptionListType
Namespace.addCategoryObject('typeBinding', 'PaymentOptionListType', PaymentOptionListType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ChargeServiceType with content type ELEMENT_ONLY
class ChargeServiceType (ServiceType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ChargeServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargeServiceType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 61, 0)
    _ElementMap = ServiceType._ElementMap.copy()
    _AttributeMap = ServiceType._AttributeMap.copy()
    # Base type is ServiceType
    
    # Element ServiceID ({urn:iso:15118:2:2013:MsgDataTypes}ServiceID) inherited from {urn:iso:15118:2:2013:MsgDataTypes}ServiceType
    
    # Element ServiceName ({urn:iso:15118:2:2013:MsgDataTypes}ServiceName) inherited from {urn:iso:15118:2:2013:MsgDataTypes}ServiceType
    
    # Element ServiceCategory ({urn:iso:15118:2:2013:MsgDataTypes}ServiceCategory) inherited from {urn:iso:15118:2:2013:MsgDataTypes}ServiceType
    
    # Element ServiceScope ({urn:iso:15118:2:2013:MsgDataTypes}ServiceScope) inherited from {urn:iso:15118:2:2013:MsgDataTypes}ServiceType
    
    # Element FreeService ({urn:iso:15118:2:2013:MsgDataTypes}FreeService) inherited from {urn:iso:15118:2:2013:MsgDataTypes}ServiceType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SupportedEnergyTransferMode uses Python identifier SupportedEnergyTransferMode
    __SupportedEnergyTransferMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedEnergyTransferMode'), 'SupportedEnergyTransferMode', '__urniso1511822013MsgDataTypes_ChargeServiceType_urniso1511822013MsgDataTypesSupportedEnergyTransferMode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 65, 0), )

    
    SupportedEnergyTransferMode = property(__SupportedEnergyTransferMode.value, __SupportedEnergyTransferMode.set, None, None)

    _ElementMap.update({
        __SupportedEnergyTransferMode.name() : __SupportedEnergyTransferMode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargeServiceType = ChargeServiceType
Namespace.addCategoryObject('typeBinding', 'ChargeServiceType', ChargeServiceType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}ContractSignatureEncryptedPrivateKeyType with content type SIMPLE
class ContractSignatureEncryptedPrivateKeyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}ContractSignatureEncryptedPrivateKeyType with content type SIMPLE"""
    _TypeDefinition = privateKeyType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKeyType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 78, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is privateKeyType
    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgDataTypes_ContractSignatureEncryptedPrivateKeyType_urniso1511822013MsgDataTypesId', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 81, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 81, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.ContractSignatureEncryptedPrivateKeyType = ContractSignatureEncryptedPrivateKeyType
Namespace.addCategoryObject('typeBinding', 'ContractSignatureEncryptedPrivateKeyType', ContractSignatureEncryptedPrivateKeyType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DiffieHellmanPublickeyType with content type SIMPLE
class DiffieHellmanPublickeyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DiffieHellmanPublickeyType with content type SIMPLE"""
    _TypeDefinition = dHpublickeyType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DiffieHellmanPublickeyType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 85, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is dHpublickeyType
    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgDataTypes_DiffieHellmanPublickeyType_urniso1511822013MsgDataTypesId', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 88, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 88, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.DiffieHellmanPublickeyType = DiffieHellmanPublickeyType
Namespace.addCategoryObject('typeBinding', 'DiffieHellmanPublickeyType', DiffieHellmanPublickeyType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}EMAIDType with content type SIMPLE
class EMAIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}EMAIDType with content type SIMPLE"""
    _TypeDefinition = eMAIDType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EMAIDType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 92, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is eMAIDType
    
    # Attribute {urn:iso:15118:2:2013:MsgDataTypes}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgDataTypes_EMAIDType_urniso1511822013MsgDataTypesId', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 95, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 95, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.EMAIDType = EMAIDType
Namespace.addCategoryObject('typeBinding', 'EMAIDType', EMAIDType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleListType with content type ELEMENT_ONLY
class SAScheduleListType (SASchedulesType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SAScheduleListType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 153, 0)
    _ElementMap = SASchedulesType._ElementMap.copy()
    _AttributeMap = SASchedulesType._AttributeMap.copy()
    # Base type is SASchedulesType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SAScheduleTuple uses Python identifier SAScheduleTuple
    __SAScheduleTuple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTuple'), 'SAScheduleTuple', '__urniso1511822013MsgDataTypes_SAScheduleListType_urniso1511822013MsgDataTypesSAScheduleTuple', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 157, 0), )

    
    SAScheduleTuple = property(__SAScheduleTuple.value, __SAScheduleTuple.set, None, None)

    _ElementMap.update({
        __SAScheduleTuple.name() : __SAScheduleTuple
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SAScheduleListType = SAScheduleListType
Namespace.addCategoryObject('typeBinding', 'SAScheduleListType', SAScheduleListType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffEntryType with content type ELEMENT_ONLY
class SalesTariffEntryType (EntryType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}SalesTariffEntryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SalesTariffEntryType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 190, 0)
    _ElementMap = EntryType._ElementMap.copy()
    _AttributeMap = EntryType._AttributeMap.copy()
    # Base type is EntryType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EPriceLevel uses Python identifier EPriceLevel
    __EPriceLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EPriceLevel'), 'EPriceLevel', '__urniso1511822013MsgDataTypes_SalesTariffEntryType_urniso1511822013MsgDataTypesEPriceLevel', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 194, 0), )

    
    EPriceLevel = property(__EPriceLevel.value, __EPriceLevel.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ConsumptionCost uses Python identifier ConsumptionCost
    __ConsumptionCost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConsumptionCost'), 'ConsumptionCost', '__urniso1511822013MsgDataTypes_SalesTariffEntryType_urniso1511822013MsgDataTypesConsumptionCost', True, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 195, 0), )

    
    ConsumptionCost = property(__ConsumptionCost.value, __ConsumptionCost.set, None, None)

    
    # Element TimeInterval ({urn:iso:15118:2:2013:MsgDataTypes}TimeInterval) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EntryType
    _ElementMap.update({
        __EPriceLevel.name() : __EPriceLevel,
        __ConsumptionCost.name() : __ConsumptionCost
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SalesTariffEntryType = SalesTariffEntryType
Namespace.addCategoryObject('typeBinding', 'SalesTariffEntryType', SalesTariffEntryType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}PMaxScheduleEntryType with content type ELEMENT_ONLY
class PMaxScheduleEntryType (EntryType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}PMaxScheduleEntryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleEntryType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 201, 0)
    _ElementMap = EntryType._ElementMap.copy()
    _AttributeMap = EntryType._AttributeMap.copy()
    # Base type is EntryType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}PMax uses Python identifier PMax
    __PMax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PMax'), 'PMax', '__urniso1511822013MsgDataTypes_PMaxScheduleEntryType_urniso1511822013MsgDataTypesPMax', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 205, 0), )

    
    PMax = property(__PMax.value, __PMax.set, None, None)

    
    # Element TimeInterval ({urn:iso:15118:2:2013:MsgDataTypes}TimeInterval) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EntryType
    _ElementMap.update({
        __PMax.name() : __PMax
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PMaxScheduleEntryType = PMaxScheduleEntryType
Namespace.addCategoryObject('typeBinding', 'PMaxScheduleEntryType', PMaxScheduleEntryType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}RelativeTimeIntervalType with content type ELEMENT_ONLY
class RelativeTimeIntervalType (IntervalType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}RelativeTimeIntervalType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelativeTimeIntervalType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 213, 0)
    _ElementMap = IntervalType._ElementMap.copy()
    _AttributeMap = IntervalType._AttributeMap.copy()
    # Base type is IntervalType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__urniso1511822013MsgDataTypes_RelativeTimeIntervalType_urniso1511822013MsgDataTypesstart', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 217, 0), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'duration'), 'duration', '__urniso1511822013MsgDataTypes_RelativeTimeIntervalType_urniso1511822013MsgDataTypesduration', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 225, 0), )

    
    duration = property(__duration.value, __duration.set, None, None)

    _ElementMap.update({
        __start.name() : __start,
        __duration.name() : __duration
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RelativeTimeIntervalType = RelativeTimeIntervalType
Namespace.addCategoryObject('typeBinding', 'RelativeTimeIntervalType', RelativeTimeIntervalType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVSEStatusType with content type ELEMENT_ONLY
class AC_EVSEStatusType (EVSEStatusType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVSEStatusType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 261, 0)
    _ElementMap = EVSEStatusType._ElementMap.copy()
    _AttributeMap = EVSEStatusType._AttributeMap.copy()
    # Base type is EVSEStatusType
    
    # Element NotificationMaxDelay ({urn:iso:15118:2:2013:MsgDataTypes}NotificationMaxDelay) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType
    
    # Element EVSENotification ({urn:iso:15118:2:2013:MsgDataTypes}EVSENotification) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}RCD uses Python identifier RCD
    __RCD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RCD'), 'RCD', '__urniso1511822013MsgDataTypes_AC_EVSEStatusType_urniso1511822013MsgDataTypesRCD', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 265, 0), )

    
    RCD = property(__RCD.value, __RCD.set, None, None)

    _ElementMap.update({
        __RCD.name() : __RCD
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AC_EVSEStatusType = AC_EVSEStatusType
Namespace.addCategoryObject('typeBinding', 'AC_EVSEStatusType', AC_EVSEStatusType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEStatusType with content type ELEMENT_ONLY
class DC_EVSEStatusType (EVSEStatusType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEStatusType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 273, 0)
    _ElementMap = EVSEStatusType._ElementMap.copy()
    _AttributeMap = EVSEStatusType._AttributeMap.copy()
    # Base type is EVSEStatusType
    
    # Element NotificationMaxDelay ({urn:iso:15118:2:2013:MsgDataTypes}NotificationMaxDelay) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType
    
    # Element EVSENotification ({urn:iso:15118:2:2013:MsgDataTypes}EVSENotification) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEIsolationStatus uses Python identifier EVSEIsolationStatus
    __EVSEIsolationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEIsolationStatus'), 'EVSEIsolationStatus', '__urniso1511822013MsgDataTypes_DC_EVSEStatusType_urniso1511822013MsgDataTypesEVSEIsolationStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 277, 0), )

    
    EVSEIsolationStatus = property(__EVSEIsolationStatus.value, __EVSEIsolationStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatusCode uses Python identifier EVSEStatusCode
    __EVSEStatusCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEStatusCode'), 'EVSEStatusCode', '__urniso1511822013MsgDataTypes_DC_EVSEStatusType_urniso1511822013MsgDataTypesEVSEStatusCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 278, 0), )

    
    EVSEStatusCode = property(__EVSEStatusCode.value, __EVSEStatusCode.set, None, None)

    _ElementMap.update({
        __EVSEIsolationStatus.name() : __EVSEIsolationStatus,
        __EVSEStatusCode.name() : __EVSEStatusCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DC_EVSEStatusType = DC_EVSEStatusType
Namespace.addCategoryObject('typeBinding', 'DC_EVSEStatusType', DC_EVSEStatusType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVStatusType with content type ELEMENT_ONLY
class DC_EVStatusType (EVStatusType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVStatusType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatusType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 284, 0)
    _ElementMap = EVStatusType._ElementMap.copy()
    _AttributeMap = EVStatusType._AttributeMap.copy()
    # Base type is EVStatusType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVReady uses Python identifier EVReady
    __EVReady = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVReady'), 'EVReady', '__urniso1511822013MsgDataTypes_DC_EVStatusType_urniso1511822013MsgDataTypesEVReady', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 288, 0), )

    
    EVReady = property(__EVReady.value, __EVReady.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVErrorCode uses Python identifier EVErrorCode
    __EVErrorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVErrorCode'), 'EVErrorCode', '__urniso1511822013MsgDataTypes_DC_EVStatusType_urniso1511822013MsgDataTypesEVErrorCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 289, 0), )

    
    EVErrorCode = property(__EVErrorCode.value, __EVErrorCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVRESSSOC uses Python identifier EVRESSSOC
    __EVRESSSOC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVRESSSOC'), 'EVRESSSOC', '__urniso1511822013MsgDataTypes_DC_EVStatusType_urniso1511822013MsgDataTypesEVRESSSOC', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 290, 0), )

    
    EVRESSSOC = property(__EVRESSSOC.value, __EVRESSSOC.set, None, None)

    _ElementMap.update({
        __EVReady.name() : __EVReady,
        __EVErrorCode.name() : __EVErrorCode,
        __EVRESSSOC.name() : __EVRESSSOC
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DC_EVStatusType = DC_EVStatusType
Namespace.addCategoryObject('typeBinding', 'DC_EVStatusType', DC_EVStatusType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVChargeParameterType with content type ELEMENT_ONLY
class AC_EVChargeParameterType (EVChargeParameterType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVChargeParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AC_EVChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 305, 0)
    _ElementMap = EVChargeParameterType._ElementMap.copy()
    _AttributeMap = EVChargeParameterType._AttributeMap.copy()
    # Base type is EVChargeParameterType
    
    # Element DepartureTime ({urn:iso:15118:2:2013:MsgDataTypes}DepartureTime) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVChargeParameterType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EAmount uses Python identifier EAmount
    __EAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EAmount'), 'EAmount', '__urniso1511822013MsgDataTypes_AC_EVChargeParameterType_urniso1511822013MsgDataTypesEAmount', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 309, 0), )

    
    EAmount = property(__EAmount.value, __EAmount.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMaxVoltage uses Python identifier EVMaxVoltage
    __EVMaxVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaxVoltage'), 'EVMaxVoltage', '__urniso1511822013MsgDataTypes_AC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMaxVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 310, 0), )

    
    EVMaxVoltage = property(__EVMaxVoltage.value, __EVMaxVoltage.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMaxCurrent uses Python identifier EVMaxCurrent
    __EVMaxCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaxCurrent'), 'EVMaxCurrent', '__urniso1511822013MsgDataTypes_AC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMaxCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 311, 0), )

    
    EVMaxCurrent = property(__EVMaxCurrent.value, __EVMaxCurrent.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMinCurrent uses Python identifier EVMinCurrent
    __EVMinCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMinCurrent'), 'EVMinCurrent', '__urniso1511822013MsgDataTypes_AC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMinCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 312, 0), )

    
    EVMinCurrent = property(__EVMinCurrent.value, __EVMinCurrent.set, None, None)

    _ElementMap.update({
        __EAmount.name() : __EAmount,
        __EVMaxVoltage.name() : __EVMaxVoltage,
        __EVMaxCurrent.name() : __EVMaxCurrent,
        __EVMinCurrent.name() : __EVMinCurrent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AC_EVChargeParameterType = AC_EVChargeParameterType
Namespace.addCategoryObject('typeBinding', 'AC_EVChargeParameterType', AC_EVChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVChargeParameterType with content type ELEMENT_ONLY
class DC_EVChargeParameterType (EVChargeParameterType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVChargeParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 318, 0)
    _ElementMap = EVChargeParameterType._ElementMap.copy()
    _AttributeMap = EVChargeParameterType._AttributeMap.copy()
    # Base type is EVChargeParameterType
    
    # Element DepartureTime ({urn:iso:15118:2:2013:MsgDataTypes}DepartureTime) inherited from {urn:iso:15118:2:2013:MsgDataTypes}EVChargeParameterType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 322, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMaximumCurrentLimit uses Python identifier EVMaximumCurrentLimit
    __EVMaximumCurrentLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit'), 'EVMaximumCurrentLimit', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMaximumCurrentLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 323, 0), )

    
    EVMaximumCurrentLimit = property(__EVMaximumCurrentLimit.value, __EVMaximumCurrentLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMaximumPowerLimit uses Python identifier EVMaximumPowerLimit
    __EVMaximumPowerLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit'), 'EVMaximumPowerLimit', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMaximumPowerLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 324, 0), )

    
    EVMaximumPowerLimit = property(__EVMaximumPowerLimit.value, __EVMaximumPowerLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVMaximumVoltageLimit uses Python identifier EVMaximumVoltageLimit
    __EVMaximumVoltageLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit'), 'EVMaximumVoltageLimit', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesEVMaximumVoltageLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 325, 0), )

    
    EVMaximumVoltageLimit = property(__EVMaximumVoltageLimit.value, __EVMaximumVoltageLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVEnergyCapacity uses Python identifier EVEnergyCapacity
    __EVEnergyCapacity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyCapacity'), 'EVEnergyCapacity', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesEVEnergyCapacity', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 326, 0), )

    
    EVEnergyCapacity = property(__EVEnergyCapacity.value, __EVEnergyCapacity.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVEnergyRequest uses Python identifier EVEnergyRequest
    __EVEnergyRequest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyRequest'), 'EVEnergyRequest', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesEVEnergyRequest', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 327, 0), )

    
    EVEnergyRequest = property(__EVEnergyRequest.value, __EVEnergyRequest.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}FullSOC uses Python identifier FullSOC
    __FullSOC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullSOC'), 'FullSOC', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesFullSOC', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 328, 0), )

    
    FullSOC = property(__FullSOC.value, __FullSOC.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}BulkSOC uses Python identifier BulkSOC
    __BulkSOC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BulkSOC'), 'BulkSOC', '__urniso1511822013MsgDataTypes_DC_EVChargeParameterType_urniso1511822013MsgDataTypesBulkSOC', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 329, 0), )

    
    BulkSOC = property(__BulkSOC.value, __BulkSOC.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus,
        __EVMaximumCurrentLimit.name() : __EVMaximumCurrentLimit,
        __EVMaximumPowerLimit.name() : __EVMaximumPowerLimit,
        __EVMaximumVoltageLimit.name() : __EVMaximumVoltageLimit,
        __EVEnergyCapacity.name() : __EVEnergyCapacity,
        __EVEnergyRequest.name() : __EVEnergyRequest,
        __FullSOC.name() : __FullSOC,
        __BulkSOC.name() : __BulkSOC
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DC_EVChargeParameterType = DC_EVChargeParameterType
Namespace.addCategoryObject('typeBinding', 'DC_EVChargeParameterType', DC_EVChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVSEChargeParameterType with content type ELEMENT_ONLY
class AC_EVSEChargeParameterType (EVSEChargeParameterType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}AC_EVSEChargeParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 337, 0)
    _ElementMap = EVSEChargeParameterType._ElementMap.copy()
    _AttributeMap = EVSEChargeParameterType._AttributeMap.copy()
    # Base type is EVSEChargeParameterType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}AC_EVSEStatus uses Python identifier AC_EVSEStatus
    __AC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus'), 'AC_EVSEStatus', '__urniso1511822013MsgDataTypes_AC_EVSEChargeParameterType_urniso1511822013MsgDataTypesAC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 341, 0), )

    
    AC_EVSEStatus = property(__AC_EVSEStatus.value, __AC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSENominalVoltage uses Python identifier EVSENominalVoltage
    __EVSENominalVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSENominalVoltage'), 'EVSENominalVoltage', '__urniso1511822013MsgDataTypes_AC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSENominalVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 343, 0), )

    
    EVSENominalVoltage = property(__EVSENominalVoltage.value, __EVSENominalVoltage.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMaxCurrent uses Python identifier EVSEMaxCurrent
    __EVSEMaxCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent'), 'EVSEMaxCurrent', '__urniso1511822013MsgDataTypes_AC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMaxCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 344, 0), )

    
    EVSEMaxCurrent = property(__EVSEMaxCurrent.value, __EVSEMaxCurrent.set, None, None)

    _ElementMap.update({
        __AC_EVSEStatus.name() : __AC_EVSEStatus,
        __EVSENominalVoltage.name() : __EVSENominalVoltage,
        __EVSEMaxCurrent.name() : __EVSEMaxCurrent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AC_EVSEChargeParameterType = AC_EVSEChargeParameterType
Namespace.addCategoryObject('typeBinding', 'AC_EVSEChargeParameterType', AC_EVSEChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEChargeParameterType with content type ELEMENT_ONLY
class DC_EVSEChargeParameterType (EVSEChargeParameterType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEChargeParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEChargeParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 350, 0)
    _ElementMap = EVSEChargeParameterType._ElementMap.copy()
    _AttributeMap = EVSEChargeParameterType._AttributeMap.copy()
    # Base type is EVSEChargeParameterType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}DC_EVSEStatus uses Python identifier DC_EVSEStatus
    __DC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), 'DC_EVSEStatus', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesDC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 354, 0), )

    
    DC_EVSEStatus = property(__DC_EVSEStatus.value, __DC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMaximumCurrentLimit uses Python identifier EVSEMaximumCurrentLimit
    __EVSEMaximumCurrentLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit'), 'EVSEMaximumCurrentLimit', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMaximumCurrentLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 355, 0), )

    
    EVSEMaximumCurrentLimit = property(__EVSEMaximumCurrentLimit.value, __EVSEMaximumCurrentLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMaximumPowerLimit uses Python identifier EVSEMaximumPowerLimit
    __EVSEMaximumPowerLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit'), 'EVSEMaximumPowerLimit', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMaximumPowerLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 356, 0), )

    
    EVSEMaximumPowerLimit = property(__EVSEMaximumPowerLimit.value, __EVSEMaximumPowerLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMaximumVoltageLimit uses Python identifier EVSEMaximumVoltageLimit
    __EVSEMaximumVoltageLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit'), 'EVSEMaximumVoltageLimit', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMaximumVoltageLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 357, 0), )

    
    EVSEMaximumVoltageLimit = property(__EVSEMaximumVoltageLimit.value, __EVSEMaximumVoltageLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMinimumCurrentLimit uses Python identifier EVSEMinimumCurrentLimit
    __EVSEMinimumCurrentLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumCurrentLimit'), 'EVSEMinimumCurrentLimit', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMinimumCurrentLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 358, 0), )

    
    EVSEMinimumCurrentLimit = property(__EVSEMinimumCurrentLimit.value, __EVSEMinimumCurrentLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEMinimumVoltageLimit uses Python identifier EVSEMinimumVoltageLimit
    __EVSEMinimumVoltageLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumVoltageLimit'), 'EVSEMinimumVoltageLimit', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEMinimumVoltageLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 359, 0), )

    
    EVSEMinimumVoltageLimit = property(__EVSEMinimumVoltageLimit.value, __EVSEMinimumVoltageLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSECurrentRegulationTolerance uses Python identifier EVSECurrentRegulationTolerance
    __EVSECurrentRegulationTolerance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentRegulationTolerance'), 'EVSECurrentRegulationTolerance', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSECurrentRegulationTolerance', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 360, 0), )

    
    EVSECurrentRegulationTolerance = property(__EVSECurrentRegulationTolerance.value, __EVSECurrentRegulationTolerance.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEPeakCurrentRipple uses Python identifier EVSEPeakCurrentRipple
    __EVSEPeakCurrentRipple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPeakCurrentRipple'), 'EVSEPeakCurrentRipple', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEPeakCurrentRipple', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 361, 0), )

    
    EVSEPeakCurrentRipple = property(__EVSEPeakCurrentRipple.value, __EVSEPeakCurrentRipple.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEEnergyToBeDelivered uses Python identifier EVSEEnergyToBeDelivered
    __EVSEEnergyToBeDelivered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEEnergyToBeDelivered'), 'EVSEEnergyToBeDelivered', '__urniso1511822013MsgDataTypes_DC_EVSEChargeParameterType_urniso1511822013MsgDataTypesEVSEEnergyToBeDelivered', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 362, 0), )

    
    EVSEEnergyToBeDelivered = property(__EVSEEnergyToBeDelivered.value, __EVSEEnergyToBeDelivered.set, None, None)

    _ElementMap.update({
        __DC_EVSEStatus.name() : __DC_EVSEStatus,
        __EVSEMaximumCurrentLimit.name() : __EVSEMaximumCurrentLimit,
        __EVSEMaximumPowerLimit.name() : __EVSEMaximumPowerLimit,
        __EVSEMaximumVoltageLimit.name() : __EVSEMaximumVoltageLimit,
        __EVSEMinimumCurrentLimit.name() : __EVSEMinimumCurrentLimit,
        __EVSEMinimumVoltageLimit.name() : __EVSEMinimumVoltageLimit,
        __EVSECurrentRegulationTolerance.name() : __EVSECurrentRegulationTolerance,
        __EVSEPeakCurrentRipple.name() : __EVSEPeakCurrentRipple,
        __EVSEEnergyToBeDelivered.name() : __EVSEEnergyToBeDelivered
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DC_EVSEChargeParameterType = DC_EVSEChargeParameterType
Namespace.addCategoryObject('typeBinding', 'DC_EVSEChargeParameterType', DC_EVSEChargeParameterType)


# Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVPowerDeliveryParameterType with content type ELEMENT_ONLY
class DC_EVPowerDeliveryParameterType (EVPowerDeliveryParameterType):
    """Complex type {urn:iso:15118:2:2013:MsgDataTypes}DC_EVPowerDeliveryParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DC_EVPowerDeliveryParameterType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 373, 0)
    _ElementMap = EVPowerDeliveryParameterType._ElementMap.copy()
    _AttributeMap = EVPowerDeliveryParameterType._AttributeMap.copy()
    # Base type is EVPowerDeliveryParameterType
    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgDataTypes_DC_EVPowerDeliveryParameterType_urniso1511822013MsgDataTypesDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 377, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}BulkChargingComplete uses Python identifier BulkChargingComplete
    __BulkChargingComplete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete'), 'BulkChargingComplete', '__urniso1511822013MsgDataTypes_DC_EVPowerDeliveryParameterType_urniso1511822013MsgDataTypesBulkChargingComplete', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 378, 0), )

    
    BulkChargingComplete = property(__BulkChargingComplete.value, __BulkChargingComplete.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}ChargingComplete uses Python identifier ChargingComplete
    __ChargingComplete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete'), 'ChargingComplete', '__urniso1511822013MsgDataTypes_DC_EVPowerDeliveryParameterType_urniso1511822013MsgDataTypesChargingComplete', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 379, 0), )

    
    ChargingComplete = property(__ChargingComplete.value, __ChargingComplete.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus,
        __BulkChargingComplete.name() : __BulkChargingComplete,
        __ChargingComplete.name() : __ChargingComplete
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DC_EVPowerDeliveryParameterType = DC_EVPowerDeliveryParameterType
Namespace.addCategoryObject('typeBinding', 'DC_EVPowerDeliveryParameterType', DC_EVPowerDeliveryParameterType)


SASchedules = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SASchedules'), SASchedulesType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 151, 0))
Namespace.addCategoryObject('elementBinding', SASchedules.name().localName(), SASchedules)

Entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Entry'), EntryType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 183, 0))
Namespace.addCategoryObject('elementBinding', Entry.name().localName(), Entry)

TimeInterval = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval'), IntervalType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 211, 0))
Namespace.addCategoryObject('elementBinding', TimeInterval.name().localName(), TimeInterval)

EVSEStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEStatus'), EVSEStatusType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 259, 0))
Namespace.addCategoryObject('elementBinding', EVSEStatus.name().localName(), EVSEStatus)

EVStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVStatus'), EVStatusType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 271, 0))
Namespace.addCategoryObject('elementBinding', EVStatus.name().localName(), EVStatus)

EVChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVChargeParameter'), EVChargeParameterType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 303, 0))
Namespace.addCategoryObject('elementBinding', EVChargeParameter.name().localName(), EVChargeParameter)

EVSEChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEChargeParameter'), EVSEChargeParameterType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 335, 0))
Namespace.addCategoryObject('elementBinding', EVSEChargeParameter.name().localName(), EVSEChargeParameter)

EVPowerDeliveryParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVPowerDeliveryParameter'), EVPowerDeliveryParameterType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 371, 0))
Namespace.addCategoryObject('elementBinding', EVPowerDeliveryParameter.name().localName(), EVPowerDeliveryParameter)

SAScheduleList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleList'), SAScheduleListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 152, 0))
Namespace.addCategoryObject('elementBinding', SAScheduleList.name().localName(), SAScheduleList)

SalesTariffEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffEntry'), SalesTariffEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 189, 0))
Namespace.addCategoryObject('elementBinding', SalesTariffEntry.name().localName(), SalesTariffEntry)

PMaxScheduleEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleEntry'), PMaxScheduleEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 200, 0))
Namespace.addCategoryObject('elementBinding', PMaxScheduleEntry.name().localName(), PMaxScheduleEntry)

RelativeTimeInterval = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelativeTimeInterval'), RelativeTimeIntervalType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 212, 0))
Namespace.addCategoryObject('elementBinding', RelativeTimeInterval.name().localName(), RelativeTimeInterval)

AC_EVSEStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus'), AC_EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 260, 0))
Namespace.addCategoryObject('elementBinding', AC_EVSEStatus.name().localName(), AC_EVSEStatus)

DC_EVSEStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), DC_EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 272, 0))
Namespace.addCategoryObject('elementBinding', DC_EVSEStatus.name().localName(), DC_EVSEStatus)

DC_EVStatus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), DC_EVStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 283, 0))
Namespace.addCategoryObject('elementBinding', DC_EVStatus.name().localName(), DC_EVStatus)

AC_EVChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AC_EVChargeParameter'), AC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 304, 0))
Namespace.addCategoryObject('elementBinding', AC_EVChargeParameter.name().localName(), AC_EVChargeParameter)

DC_EVChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVChargeParameter'), DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 317, 0))
Namespace.addCategoryObject('elementBinding', DC_EVChargeParameter.name().localName(), DC_EVChargeParameter)

AC_EVSEChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEChargeParameter'), AC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 336, 0))
Namespace.addCategoryObject('elementBinding', AC_EVSEChargeParameter.name().localName(), AC_EVSEChargeParameter)

DC_EVSEChargeParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEChargeParameter'), DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 349, 0))
Namespace.addCategoryObject('elementBinding', DC_EVSEChargeParameter.name().localName(), DC_EVSEChargeParameter)

DC_EVPowerDeliveryParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVPowerDeliveryParameter'), DC_EVPowerDeliveryParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 372, 0))
Namespace.addCategoryObject('elementBinding', DC_EVPowerDeliveryParameter.name().localName(), DC_EVPowerDeliveryParameter)



ServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), serviceIDType, scope=ServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 16, 0)))

ServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceName'), serviceNameType, scope=ServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0)))

ServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory'), serviceCategoryType, scope=ServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 18, 0)))

ServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope'), serviceScopeType, scope=ServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0)))

ServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FreeService'), pyxb.binding.datatypes.boolean, scope=ServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 20, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 16, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceName')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 18, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FreeService')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 20, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceType._Automaton = _BuildAutomaton()




ServiceListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), ServiceType, scope=ServiceListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 25, 0)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=8, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 25, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ServiceListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Service')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 25, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceListType._Automaton = _BuildAutomaton_()




SelectedServiceListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SelectedService'), SelectedServiceType, scope=SelectedServiceListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 30, 0)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=16, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 30, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SelectedServiceListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SelectedService')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 30, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SelectedServiceListType._Automaton = _BuildAutomaton_2()




SelectedServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), serviceIDType, scope=SelectedServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 35, 0)))

SelectedServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID'), pyxb.binding.datatypes.short, scope=SelectedServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 36, 0)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 36, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SelectedServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 35, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SelectedServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 36, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SelectedServiceType._Automaton = _BuildAutomaton_3()




ServiceParameterListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterSet'), ParameterSetType, scope=ServiceParameterListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 41, 0)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=255, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 41, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ServiceParameterListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterSet')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 41, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceParameterListType._Automaton = _BuildAutomaton_4()




ParameterSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID'), pyxb.binding.datatypes.short, scope=ParameterSetType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 46, 0)))

ParameterSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), ParameterType, scope=ParameterSetType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 47, 0)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=16, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 47, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ParameterSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParameterSetID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 46, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParameterSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Parameter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 47, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ParameterSetType._Automaton = _BuildAutomaton_5()




ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boolValue'), pyxb.binding.datatypes.boolean, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 52, 0)))

ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'byteValue'), pyxb.binding.datatypes.byte, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 53, 0)))

ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shortValue'), pyxb.binding.datatypes.short, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 54, 0)))

ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intValue'), pyxb.binding.datatypes.int, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 55, 0)))

ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'physicalValue'), PhysicalValueType, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 56, 0)))

ParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stringValue'), pyxb.binding.datatypes.string, scope=ParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 57, 0)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boolValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 52, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'byteValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 53, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shortValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 54, 0))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 55, 0))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'physicalValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 56, 0))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stringValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 57, 0))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ParameterType._Automaton = _BuildAutomaton_6()




SupportedEnergyTransferModeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnergyTransferMode'), EnergyTransferModeType, scope=SupportedEnergyTransferModeType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 72, 0)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=6, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 72, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupportedEnergyTransferModeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EnergyTransferMode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 72, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SupportedEnergyTransferModeType._Automaton = _BuildAutomaton_7()




CertificateChainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Certificate'), certificateType, scope=CertificateChainType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 101, 0)))

CertificateChainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubCertificates'), SubCertificatesType, scope=CertificateChainType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 102, 0)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 102, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertificateChainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Certificate')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 101, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CertificateChainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubCertificates')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 102, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertificateChainType._Automaton = _BuildAutomaton_8()




SubCertificatesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Certificate'), certificateType, scope=SubCertificatesType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 108, 0)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=4, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 108, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubCertificatesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Certificate')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 108, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubCertificatesType._Automaton = _BuildAutomaton_9()




ListOfRootCertificateIDsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RootCertificateID'), _ImportedBinding__xmlsig.X509IssuerSerialType, scope=ListOfRootCertificateIDsType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 113, 0)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=20, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 113, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ListOfRootCertificateIDsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RootCertificateID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 113, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ListOfRootCertificateIDsType._Automaton = _BuildAutomaton_10()




MeterInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterID'), meterIDType, scope=MeterInfoType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 121, 0)))

MeterInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterReading'), pyxb.binding.datatypes.unsignedLong, scope=MeterInfoType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 122, 0)))

MeterInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigMeterReading'), sigMeterReadingType, scope=MeterInfoType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 123, 0)))

MeterInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterStatus'), meterStatusType, scope=MeterInfoType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 124, 0)))

MeterInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TMeter'), pyxb.binding.datatypes.long, scope=MeterInfoType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 125, 0)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 122, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 123, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 124, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 125, 0))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeterInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 121, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeterInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterReading')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 122, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeterInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigMeterReading')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 123, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeterInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 124, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeterInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TMeter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 125, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeterInfoType._Automaton = _BuildAutomaton_11()




PhysicalValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Multiplier'), unitMultiplierType, scope=PhysicalValueType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 133, 0)))

PhysicalValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Unit'), unitSymbolType, scope=PhysicalValueType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 134, 0)))

PhysicalValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.short, scope=PhysicalValueType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 135, 0)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PhysicalValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Multiplier')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 133, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PhysicalValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Unit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 134, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PhysicalValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 135, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PhysicalValueType._Automaton = _BuildAutomaton_12()




NotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FaultCode'), faultCodeType, scope=NotificationType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 143, 0)))

NotificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FaultMsg'), faultMsgType, scope=NotificationType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 144, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 144, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FaultCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 143, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NotificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FaultMsg')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 144, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NotificationType._Automaton = _BuildAutomaton_13()




SAScheduleTupleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), SAIDType, scope=SAScheduleTupleType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 164, 0)))

SAScheduleTupleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PMaxSchedule'), PMaxScheduleType, scope=SAScheduleTupleType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 165, 0)))

SAScheduleTupleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SalesTariff'), SalesTariffType, scope=SAScheduleTupleType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 166, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 166, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SAScheduleTupleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 164, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SAScheduleTupleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PMaxSchedule')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 165, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SAScheduleTupleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SalesTariff')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 166, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SAScheduleTupleType._Automaton = _BuildAutomaton_14()




SalesTariffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffID'), SAIDType, scope=SalesTariffType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 171, 0)))

SalesTariffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffDescription'), tariffDescriptionType, scope=SalesTariffType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 172, 0)))

SalesTariffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumEPriceLevels'), pyxb.binding.datatypes.unsignedByte, scope=SalesTariffType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 173, 0)))

SalesTariffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffEntry'), SalesTariffEntryType, scope=SalesTariffType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 189, 0)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 172, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 173, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=1, max=1024, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 174, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SalesTariffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 171, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SalesTariffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffDescription')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 172, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SalesTariffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumEPriceLevels')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 173, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SalesTariffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SalesTariffEntry')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 174, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SalesTariffType._Automaton = _BuildAutomaton_15()




PMaxScheduleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleEntry'), PMaxScheduleEntryType, scope=PMaxScheduleType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 200, 0)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=1024, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 180, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PMaxScheduleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PMaxScheduleEntry')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 180, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PMaxScheduleType._Automaton = _BuildAutomaton_16()




EntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval'), IntervalType, abstract=pyxb.binding.datatypes.boolean(1), scope=EntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 211, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 186, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EntryType._Automaton = _BuildAutomaton_17()




ConsumptionCostType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startValue'), PhysicalValueType, scope=ConsumptionCostType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 239, 0)))

ConsumptionCostType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cost'), CostType, scope=ConsumptionCostType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 240, 0)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=3, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 240, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConsumptionCostType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startValue')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 239, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConsumptionCostType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cost')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 240, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConsumptionCostType._Automaton = _BuildAutomaton_18()




CostType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'costKind'), costKindType, scope=CostType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 245, 0)))

CostType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amount'), pyxb.binding.datatypes.unsignedInt, scope=CostType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 246, 0)))

CostType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amountMultiplier'), unitMultiplierType, scope=CostType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 247, 0)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 247, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CostType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'costKind')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 245, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CostType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amount')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 246, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CostType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amountMultiplier')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 247, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CostType._Automaton = _BuildAutomaton_19()




EVSEStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotificationMaxDelay'), pyxb.binding.datatypes.unsignedShort, scope=EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 255, 0)))

EVSEStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSENotification'), EVSENotificationType, scope=EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 256, 0)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotificationMaxDelay')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 255, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSENotification')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 256, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EVSEStatusType._Automaton = _BuildAutomaton_20()




EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DepartureTime'), pyxb.binding.datatypes.unsignedInt, scope=EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DepartureTime')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EVChargeParameterType._Automaton = _BuildAutomaton_21()




ChargingProfileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProfileEntry'), ProfileEntryType, scope=ChargingProfileType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 389, 0)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=24, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 389, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChargingProfileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProfileEntry')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 389, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChargingProfileType._Automaton = _BuildAutomaton_22()




ProfileEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryStart'), pyxb.binding.datatypes.unsignedInt, scope=ProfileEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 394, 0)))

ProfileEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxPower'), PhysicalValueType, scope=ProfileEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 396, 0)))

ProfileEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxNumberOfPhasesInUse'), maxNumPhasesType, scope=ProfileEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 398, 0)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 398, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProfileEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryStart')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 394, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProfileEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxPower')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 396, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProfileEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfileEntryMaxNumberOfPhasesInUse')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 398, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProfileEntryType._Automaton = _BuildAutomaton_23()




PaymentOptionListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentOption'), paymentOptionType, scope=PaymentOptionListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 580, 0)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 580, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PaymentOptionListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PaymentOption')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 580, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentOptionListType._Automaton = _BuildAutomaton_24()




ChargeServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedEnergyTransferMode'), SupportedEnergyTransferModeType, scope=ChargeServiceType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 65, 0)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 16, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceName')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 17, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 18, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 19, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FreeService')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 20, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChargeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedEnergyTransferMode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 65, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChargeServiceType._Automaton = _BuildAutomaton_25()




SAScheduleListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTuple'), SAScheduleTupleType, scope=SAScheduleListType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 157, 0)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=3, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 157, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SAScheduleListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTuple')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 157, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SAScheduleListType._Automaton = _BuildAutomaton_26()




SalesTariffEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EPriceLevel'), pyxb.binding.datatypes.unsignedByte, scope=SalesTariffEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 194, 0)))

SalesTariffEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsumptionCost'), ConsumptionCostType, scope=SalesTariffEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 195, 0)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 194, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 195, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SalesTariffEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 186, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SalesTariffEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EPriceLevel')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 194, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SalesTariffEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConsumptionCost')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 195, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SalesTariffEntryType._Automaton = _BuildAutomaton_27()




PMaxScheduleEntryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PMax'), PhysicalValueType, scope=PMaxScheduleEntryType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 205, 0)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PMaxScheduleEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeInterval')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 186, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PMaxScheduleEntryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PMax')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 205, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PMaxScheduleEntryType._Automaton = _BuildAutomaton_28()




RelativeTimeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), STD_ANON, scope=RelativeTimeIntervalType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 217, 0)))

RelativeTimeIntervalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'duration'), STD_ANON_, scope=RelativeTimeIntervalType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 225, 0)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 225, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RelativeTimeIntervalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 217, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelativeTimeIntervalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'duration')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 225, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RelativeTimeIntervalType._Automaton = _BuildAutomaton_29()




AC_EVSEStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RCD'), pyxb.binding.datatypes.boolean, scope=AC_EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 265, 0)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotificationMaxDelay')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 255, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSENotification')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 256, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RCD')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 265, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AC_EVSEStatusType._Automaton = _BuildAutomaton_30()




DC_EVSEStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEIsolationStatus'), isolationLevelType, scope=DC_EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 277, 0)))

DC_EVSEStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEStatusCode'), DC_EVSEStatusCodeType, scope=DC_EVSEStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 278, 0)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 277, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotificationMaxDelay')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 255, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSENotification')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 256, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEIsolationStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 277, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DC_EVSEStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEStatusCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 278, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DC_EVSEStatusType._Automaton = _BuildAutomaton_31()




DC_EVStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVReady'), pyxb.binding.datatypes.boolean, scope=DC_EVStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 288, 0)))

DC_EVStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVErrorCode'), DC_EVErrorCodeType, scope=DC_EVStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 289, 0)))

DC_EVStatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVRESSSOC'), percentValueType, scope=DC_EVStatusType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 290, 0)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVReady')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 288, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVErrorCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 289, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DC_EVStatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVRESSSOC')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 290, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DC_EVStatusType._Automaton = _BuildAutomaton_32()




AC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EAmount'), PhysicalValueType, scope=AC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 309, 0)))

AC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaxVoltage'), PhysicalValueType, scope=AC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 310, 0)))

AC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaxCurrent'), PhysicalValueType, scope=AC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 311, 0)))

AC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMinCurrent'), PhysicalValueType, scope=AC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 312, 0)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DepartureTime')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EAmount')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 309, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaxVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 310, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaxCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 311, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMinCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 312, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AC_EVChargeParameterType._Automaton = _BuildAutomaton_33()




DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), DC_EVStatusType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 322, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit'), PhysicalValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 323, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit'), PhysicalValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 324, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit'), PhysicalValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 325, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyCapacity'), PhysicalValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 326, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyRequest'), PhysicalValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 327, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullSOC'), percentValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 328, 0)))

DC_EVChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BulkSOC'), percentValueType, scope=DC_EVChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 329, 0)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 324, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 326, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 327, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 328, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 329, 0))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DepartureTime')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 300, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 322, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 323, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 324, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 325, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyCapacity')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 326, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVEnergyRequest')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 327, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullSOC')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 328, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DC_EVChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BulkSOC')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 329, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DC_EVChargeParameterType._Automaton = _BuildAutomaton_34()




AC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus'), AC_EVSEStatusType, scope=AC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 341, 0)))

AC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSENominalVoltage'), PhysicalValueType, scope=AC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 343, 0)))

AC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent'), PhysicalValueType, scope=AC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 344, 0)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 341, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSENominalVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 343, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 344, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AC_EVSEChargeParameterType._Automaton = _BuildAutomaton_35()




DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), DC_EVSEStatusType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 354, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 355, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 356, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 357, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumCurrentLimit'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 358, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumVoltageLimit'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 359, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentRegulationTolerance'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 360, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPeakCurrentRipple'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 361, 0)))

DC_EVSEChargeParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEEnergyToBeDelivered'), PhysicalValueType, scope=DC_EVSEChargeParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 362, 0)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 360, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 362, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 354, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 355, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 356, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 357, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumCurrentLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 358, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMinimumVoltageLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 359, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentRegulationTolerance')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 360, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPeakCurrentRipple')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 361, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DC_EVSEChargeParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEEnergyToBeDelivered')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 362, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DC_EVSEChargeParameterType._Automaton = _BuildAutomaton_36()




DC_EVPowerDeliveryParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), DC_EVStatusType, scope=DC_EVPowerDeliveryParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 377, 0)))

DC_EVPowerDeliveryParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete'), pyxb.binding.datatypes.boolean, scope=DC_EVPowerDeliveryParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 378, 0)))

DC_EVPowerDeliveryParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete'), pyxb.binding.datatypes.boolean, scope=DC_EVPowerDeliveryParameterType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 379, 0)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 378, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVPowerDeliveryParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 377, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DC_EVPowerDeliveryParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 378, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DC_EVPowerDeliveryParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 379, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DC_EVPowerDeliveryParameterType._Automaton = _BuildAutomaton_37()


SAScheduleList._setSubstitutionGroup(SASchedules)

SalesTariffEntry._setSubstitutionGroup(Entry)

PMaxScheduleEntry._setSubstitutionGroup(Entry)

RelativeTimeInterval._setSubstitutionGroup(TimeInterval)

AC_EVSEStatus._setSubstitutionGroup(EVSEStatus)

DC_EVSEStatus._setSubstitutionGroup(EVSEStatus)

DC_EVStatus._setSubstitutionGroup(EVStatus)

AC_EVChargeParameter._setSubstitutionGroup(EVChargeParameter)

DC_EVChargeParameter._setSubstitutionGroup(EVChargeParameter)

AC_EVSEChargeParameter._setSubstitutionGroup(EVSEChargeParameter)

DC_EVSEChargeParameter._setSubstitutionGroup(EVSEChargeParameter)

DC_EVPowerDeliveryParameter._setSubstitutionGroup(EVPowerDeliveryParameter)
