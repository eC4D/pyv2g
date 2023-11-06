# ./_v2gci_b.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b966a802f2314e93c388cfabe68106502ccc20fa
# Generated 2021-07-04 00:14:40.051363 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace urn:iso:15118:2:2013:MsgBody [xmlns:v2gci_b]

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
import _v2gci_t as _ImportedBinding__v2gci_t

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:iso:15118:2:2013:MsgBody', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_v2gci_t = _ImportedBinding__v2gci_t.Namespace
_Namespace_v2gci_t.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:iso:15118:2:2013:MsgBody}BodyType with content type ELEMENT_ONLY
class BodyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgBody}BodyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BodyType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 10, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgBody}BodyElement uses Python identifier BodyElement
    __BodyElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BodyElement'), 'BodyElement', '__urniso1511822013MsgBody_BodyType_urniso1511822013MsgBodyBodyElement', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 15, 0), )

    
    BodyElement = property(__BodyElement.value, __BodyElement.set, None, None)

    _ElementMap.update({
        __BodyElement.name() : __BodyElement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BodyType = BodyType
Namespace.addCategoryObject('typeBinding', 'BodyType', BodyType)


# Complex type {urn:iso:15118:2:2013:MsgBody}BodyBaseType with content type EMPTY
class BodyBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgBody}BodyBaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BodyBaseType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 16, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BodyBaseType = BodyBaseType
Namespace.addCategoryObject('typeBinding', 'BodyBaseType', BodyBaseType)


# Complex type {urn:iso:15118:2:2013:MsgBody}SessionSetupReqType with content type ELEMENT_ONLY
class SessionSetupReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}SessionSetupReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SessionSetupReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 24, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}EVCCID uses Python identifier EVCCID
    __EVCCID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVCCID'), 'EVCCID', '__urniso1511822013MsgBody_SessionSetupReqType_urniso1511822013MsgBodyEVCCID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 28, 0), )

    
    EVCCID = property(__EVCCID.value, __EVCCID.set, None, None)

    _ElementMap.update({
        __EVCCID.name() : __EVCCID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SessionSetupReqType = SessionSetupReqType
Namespace.addCategoryObject('typeBinding', 'SessionSetupReqType', SessionSetupReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}SessionSetupResType with content type ELEMENT_ONLY
class SessionSetupResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}SessionSetupResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SessionSetupResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 34, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_SessionSetupResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 38, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEID uses Python identifier EVSEID
    __EVSEID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), 'EVSEID', '__urniso1511822013MsgBody_SessionSetupResType_urniso1511822013MsgBodyEVSEID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 39, 0), )

    
    EVSEID = property(__EVSEID.value, __EVSEID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSETimeStamp uses Python identifier EVSETimeStamp
    __EVSETimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp'), 'EVSETimeStamp', '__urniso1511822013MsgBody_SessionSetupResType_urniso1511822013MsgBodyEVSETimeStamp', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 40, 0), )

    
    EVSETimeStamp = property(__EVSETimeStamp.value, __EVSETimeStamp.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEID.name() : __EVSEID,
        __EVSETimeStamp.name() : __EVSETimeStamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SessionSetupResType = SessionSetupResType
Namespace.addCategoryObject('typeBinding', 'SessionSetupResType', SessionSetupResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDiscoveryReqType with content type ELEMENT_ONLY
class ServiceDiscoveryReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDiscoveryReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceDiscoveryReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 49, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceScope uses Python identifier ServiceScope
    __ServiceScope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope'), 'ServiceScope', '__urniso1511822013MsgBody_ServiceDiscoveryReqType_urniso1511822013MsgBodyServiceScope', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 53, 0), )

    
    ServiceScope = property(__ServiceScope.value, __ServiceScope.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceCategory uses Python identifier ServiceCategory
    __ServiceCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory'), 'ServiceCategory', '__urniso1511822013MsgBody_ServiceDiscoveryReqType_urniso1511822013MsgBodyServiceCategory', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 54, 0), )

    
    ServiceCategory = property(__ServiceCategory.value, __ServiceCategory.set, None, None)

    _ElementMap.update({
        __ServiceScope.name() : __ServiceScope,
        __ServiceCategory.name() : __ServiceCategory
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceDiscoveryReqType = ServiceDiscoveryReqType
Namespace.addCategoryObject('typeBinding', 'ServiceDiscoveryReqType', ServiceDiscoveryReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDiscoveryResType with content type ELEMENT_ONLY
class ServiceDiscoveryResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDiscoveryResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceDiscoveryResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 60, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_ServiceDiscoveryResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 64, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}PaymentOptionList uses Python identifier PaymentOptionList
    __PaymentOptionList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionList'), 'PaymentOptionList', '__urniso1511822013MsgBody_ServiceDiscoveryResType_urniso1511822013MsgBodyPaymentOptionList', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 65, 0), )

    
    PaymentOptionList = property(__PaymentOptionList.value, __PaymentOptionList.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ChargeService uses Python identifier ChargeService
    __ChargeService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargeService'), 'ChargeService', '__urniso1511822013MsgBody_ServiceDiscoveryResType_urniso1511822013MsgBodyChargeService', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 66, 0), )

    
    ChargeService = property(__ChargeService.value, __ChargeService.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceList uses Python identifier ServiceList
    __ServiceList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceList'), 'ServiceList', '__urniso1511822013MsgBody_ServiceDiscoveryResType_urniso1511822013MsgBodyServiceList', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 68, 0), )

    
    ServiceList = property(__ServiceList.value, __ServiceList.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __PaymentOptionList.name() : __PaymentOptionList,
        __ChargeService.name() : __ChargeService,
        __ServiceList.name() : __ServiceList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceDiscoveryResType = ServiceDiscoveryResType
Namespace.addCategoryObject('typeBinding', 'ServiceDiscoveryResType', ServiceDiscoveryResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDetailReqType with content type ELEMENT_ONLY
class ServiceDetailReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDetailReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceDetailReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 77, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceID uses Python identifier ServiceID
    __ServiceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), 'ServiceID', '__urniso1511822013MsgBody_ServiceDetailReqType_urniso1511822013MsgBodyServiceID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 81, 0), )

    
    ServiceID = property(__ServiceID.value, __ServiceID.set, None, None)

    _ElementMap.update({
        __ServiceID.name() : __ServiceID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceDetailReqType = ServiceDetailReqType
Namespace.addCategoryObject('typeBinding', 'ServiceDetailReqType', ServiceDetailReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDetailResType with content type ELEMENT_ONLY
class ServiceDetailResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ServiceDetailResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceDetailResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 87, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_ServiceDetailResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 91, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceID uses Python identifier ServiceID
    __ServiceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), 'ServiceID', '__urniso1511822013MsgBody_ServiceDetailResType_urniso1511822013MsgBodyServiceID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 92, 0), )

    
    ServiceID = property(__ServiceID.value, __ServiceID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ServiceParameterList uses Python identifier ServiceParameterList
    __ServiceParameterList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ServiceParameterList'), 'ServiceParameterList', '__urniso1511822013MsgBody_ServiceDetailResType_urniso1511822013MsgBodyServiceParameterList', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 93, 0), )

    
    ServiceParameterList = property(__ServiceParameterList.value, __ServiceParameterList.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __ServiceID.name() : __ServiceID,
        __ServiceParameterList.name() : __ServiceParameterList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ServiceDetailResType = ServiceDetailResType
Namespace.addCategoryObject('typeBinding', 'ServiceDetailResType', ServiceDetailResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PaymentServiceSelectionReqType with content type ELEMENT_ONLY
class PaymentServiceSelectionReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PaymentServiceSelectionReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentServiceSelectionReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 102, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}SelectedPaymentOption uses Python identifier SelectedPaymentOption
    __SelectedPaymentOption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SelectedPaymentOption'), 'SelectedPaymentOption', '__urniso1511822013MsgBody_PaymentServiceSelectionReqType_urniso1511822013MsgBodySelectedPaymentOption', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 106, 0), )

    
    SelectedPaymentOption = property(__SelectedPaymentOption.value, __SelectedPaymentOption.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SelectedServiceList uses Python identifier SelectedServiceList
    __SelectedServiceList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SelectedServiceList'), 'SelectedServiceList', '__urniso1511822013MsgBody_PaymentServiceSelectionReqType_urniso1511822013MsgBodySelectedServiceList', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 107, 0), )

    
    SelectedServiceList = property(__SelectedServiceList.value, __SelectedServiceList.set, None, None)

    _ElementMap.update({
        __SelectedPaymentOption.name() : __SelectedPaymentOption,
        __SelectedServiceList.name() : __SelectedServiceList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentServiceSelectionReqType = PaymentServiceSelectionReqType
Namespace.addCategoryObject('typeBinding', 'PaymentServiceSelectionReqType', PaymentServiceSelectionReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PaymentServiceSelectionResType with content type ELEMENT_ONLY
class PaymentServiceSelectionResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PaymentServiceSelectionResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentServiceSelectionResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 113, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_PaymentServiceSelectionResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 117, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentServiceSelectionResType = PaymentServiceSelectionResType
Namespace.addCategoryObject('typeBinding', 'PaymentServiceSelectionResType', PaymentServiceSelectionResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PaymentDetailsReqType with content type ELEMENT_ONLY
class PaymentDetailsReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PaymentDetailsReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentDetailsReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 126, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}eMAID uses Python identifier eMAID
    __eMAID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), 'eMAID', '__urniso1511822013MsgBody_PaymentDetailsReqType_urniso1511822013MsgBodyeMAID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 130, 0), )

    
    eMAID = property(__eMAID.value, __eMAID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureCertChain uses Python identifier ContractSignatureCertChain
    __ContractSignatureCertChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), 'ContractSignatureCertChain', '__urniso1511822013MsgBody_PaymentDetailsReqType_urniso1511822013MsgBodyContractSignatureCertChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 131, 0), )

    
    ContractSignatureCertChain = property(__ContractSignatureCertChain.value, __ContractSignatureCertChain.set, None, None)

    _ElementMap.update({
        __eMAID.name() : __eMAID,
        __ContractSignatureCertChain.name() : __ContractSignatureCertChain
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentDetailsReqType = PaymentDetailsReqType
Namespace.addCategoryObject('typeBinding', 'PaymentDetailsReqType', PaymentDetailsReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PaymentDetailsResType with content type ELEMENT_ONLY
class PaymentDetailsResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PaymentDetailsResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentDetailsResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 137, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_PaymentDetailsResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 141, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}GenChallenge uses Python identifier GenChallenge
    __GenChallenge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge'), 'GenChallenge', '__urniso1511822013MsgBody_PaymentDetailsResType_urniso1511822013MsgBodyGenChallenge', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 142, 0), )

    
    GenChallenge = property(__GenChallenge.value, __GenChallenge.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSETimeStamp uses Python identifier EVSETimeStamp
    __EVSETimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp'), 'EVSETimeStamp', '__urniso1511822013MsgBody_PaymentDetailsResType_urniso1511822013MsgBodyEVSETimeStamp', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 143, 0), )

    
    EVSETimeStamp = property(__EVSETimeStamp.value, __EVSETimeStamp.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __GenChallenge.name() : __GenChallenge,
        __EVSETimeStamp.name() : __EVSETimeStamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentDetailsResType = PaymentDetailsResType
Namespace.addCategoryObject('typeBinding', 'PaymentDetailsResType', PaymentDetailsResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}AuthorizationReqType with content type ELEMENT_ONLY
class AuthorizationReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}AuthorizationReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuthorizationReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 152, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}GenChallenge uses Python identifier GenChallenge
    __GenChallenge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge'), 'GenChallenge', '__urniso1511822013MsgBody_AuthorizationReqType_urniso1511822013MsgBodyGenChallenge', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 156, 0), )

    
    GenChallenge = property(__GenChallenge.value, __GenChallenge.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgBody}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgBody_AuthorizationReqType_urniso1511822013MsgBodyId', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 158, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 158, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __GenChallenge.name() : __GenChallenge
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.AuthorizationReqType = AuthorizationReqType
Namespace.addCategoryObject('typeBinding', 'AuthorizationReqType', AuthorizationReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}AuthorizationResType with content type ELEMENT_ONLY
class AuthorizationResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}AuthorizationResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AuthorizationResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 163, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_AuthorizationResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 167, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEProcessing uses Python identifier EVSEProcessing
    __EVSEProcessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), 'EVSEProcessing', '__urniso1511822013MsgBody_AuthorizationResType_urniso1511822013MsgBodyEVSEProcessing', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 168, 0), )

    
    EVSEProcessing = property(__EVSEProcessing.value, __EVSEProcessing.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEProcessing.name() : __EVSEProcessing
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AuthorizationResType = AuthorizationResType
Namespace.addCategoryObject('typeBinding', 'AuthorizationResType', AuthorizationResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ChargeParameterDiscoveryReqType with content type ELEMENT_ONLY
class ChargeParameterDiscoveryReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ChargeParameterDiscoveryReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargeParameterDiscoveryReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 177, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}MaxEntriesSAScheduleTuple uses Python identifier MaxEntriesSAScheduleTuple
    __MaxEntriesSAScheduleTuple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxEntriesSAScheduleTuple'), 'MaxEntriesSAScheduleTuple', '__urniso1511822013MsgBody_ChargeParameterDiscoveryReqType_urniso1511822013MsgBodyMaxEntriesSAScheduleTuple', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 181, 0), )

    
    MaxEntriesSAScheduleTuple = property(__MaxEntriesSAScheduleTuple.value, __MaxEntriesSAScheduleTuple.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}RequestedEnergyTransferMode uses Python identifier RequestedEnergyTransferMode
    __RequestedEnergyTransferMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestedEnergyTransferMode'), 'RequestedEnergyTransferMode', '__urniso1511822013MsgBody_ChargeParameterDiscoveryReqType_urniso1511822013MsgBodyRequestedEnergyTransferMode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 183, 0), )

    
    RequestedEnergyTransferMode = property(__RequestedEnergyTransferMode.value, __RequestedEnergyTransferMode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVChargeParameter uses Python identifier EVChargeParameter
    __EVChargeParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVChargeParameter'), 'EVChargeParameter', '__urniso1511822013MsgBody_ChargeParameterDiscoveryReqType_urniso1511822013MsgDataTypesEVChargeParameter', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 303, 0), )

    
    EVChargeParameter = property(__EVChargeParameter.value, __EVChargeParameter.set, None, None)

    _ElementMap.update({
        __MaxEntriesSAScheduleTuple.name() : __MaxEntriesSAScheduleTuple,
        __RequestedEnergyTransferMode.name() : __RequestedEnergyTransferMode,
        __EVChargeParameter.name() : __EVChargeParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargeParameterDiscoveryReqType = ChargeParameterDiscoveryReqType
Namespace.addCategoryObject('typeBinding', 'ChargeParameterDiscoveryReqType', ChargeParameterDiscoveryReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ChargeParameterDiscoveryResType with content type ELEMENT_ONLY
class ChargeParameterDiscoveryResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ChargeParameterDiscoveryResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargeParameterDiscoveryResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 190, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_ChargeParameterDiscoveryResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 194, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEProcessing uses Python identifier EVSEProcessing
    __EVSEProcessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), 'EVSEProcessing', '__urniso1511822013MsgBody_ChargeParameterDiscoveryResType_urniso1511822013MsgBodyEVSEProcessing', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 195, 0), )

    
    EVSEProcessing = property(__EVSEProcessing.value, __EVSEProcessing.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}SASchedules uses Python identifier SASchedules
    __SASchedules = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'SASchedules'), 'SASchedules', '__urniso1511822013MsgBody_ChargeParameterDiscoveryResType_urniso1511822013MsgDataTypesSASchedules', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 151, 0), )

    
    SASchedules = property(__SASchedules.value, __SASchedules.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEChargeParameter uses Python identifier EVSEChargeParameter
    __EVSEChargeParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEChargeParameter'), 'EVSEChargeParameter', '__urniso1511822013MsgBody_ChargeParameterDiscoveryResType_urniso1511822013MsgDataTypesEVSEChargeParameter', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 335, 0), )

    
    EVSEChargeParameter = property(__EVSEChargeParameter.value, __EVSEChargeParameter.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEProcessing.name() : __EVSEProcessing,
        __SASchedules.name() : __SASchedules,
        __EVSEChargeParameter.name() : __EVSEChargeParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargeParameterDiscoveryResType = ChargeParameterDiscoveryResType
Namespace.addCategoryObject('typeBinding', 'ChargeParameterDiscoveryResType', ChargeParameterDiscoveryResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PowerDeliveryReqType with content type ELEMENT_ONLY
class PowerDeliveryReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PowerDeliveryReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerDeliveryReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 206, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ChargeProgress uses Python identifier ChargeProgress
    __ChargeProgress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargeProgress'), 'ChargeProgress', '__urniso1511822013MsgBody_PowerDeliveryReqType_urniso1511822013MsgBodyChargeProgress', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 210, 0), )

    
    ChargeProgress = property(__ChargeProgress.value, __ChargeProgress.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAScheduleTupleID uses Python identifier SAScheduleTupleID
    __SAScheduleTupleID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), 'SAScheduleTupleID', '__urniso1511822013MsgBody_PowerDeliveryReqType_urniso1511822013MsgBodySAScheduleTupleID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 211, 0), )

    
    SAScheduleTupleID = property(__SAScheduleTupleID.value, __SAScheduleTupleID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ChargingProfile uses Python identifier ChargingProfile
    __ChargingProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfile'), 'ChargingProfile', '__urniso1511822013MsgBody_PowerDeliveryReqType_urniso1511822013MsgBodyChargingProfile', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 212, 0), )

    
    ChargingProfile = property(__ChargingProfile.value, __ChargingProfile.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVPowerDeliveryParameter uses Python identifier EVPowerDeliveryParameter
    __EVPowerDeliveryParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVPowerDeliveryParameter'), 'EVPowerDeliveryParameter', '__urniso1511822013MsgBody_PowerDeliveryReqType_urniso1511822013MsgDataTypesEVPowerDeliveryParameter', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 371, 0), )

    
    EVPowerDeliveryParameter = property(__EVPowerDeliveryParameter.value, __EVPowerDeliveryParameter.set, None, None)

    _ElementMap.update({
        __ChargeProgress.name() : __ChargeProgress,
        __SAScheduleTupleID.name() : __SAScheduleTupleID,
        __ChargingProfile.name() : __ChargingProfile,
        __EVPowerDeliveryParameter.name() : __EVPowerDeliveryParameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PowerDeliveryReqType = PowerDeliveryReqType
Namespace.addCategoryObject('typeBinding', 'PowerDeliveryReqType', PowerDeliveryReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PowerDeliveryResType with content type ELEMENT_ONLY
class PowerDeliveryResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PowerDeliveryResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerDeliveryResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 219, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_PowerDeliveryResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 223, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatus uses Python identifier EVSEStatus
    __EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus'), 'EVSEStatus', '__urniso1511822013MsgBody_PowerDeliveryResType_urniso1511822013MsgDataTypesEVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 259, 0), )

    
    EVSEStatus = property(__EVSEStatus.value, __EVSEStatus.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEStatus.name() : __EVSEStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PowerDeliveryResType = PowerDeliveryResType
Namespace.addCategoryObject('typeBinding', 'PowerDeliveryResType', PowerDeliveryResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}MeteringReceiptReqType with content type ELEMENT_ONLY
class MeteringReceiptReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}MeteringReceiptReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeteringReceiptReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 233, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}SessionID uses Python identifier SessionID
    __SessionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SessionID'), 'SessionID', '__urniso1511822013MsgBody_MeteringReceiptReqType_urniso1511822013MsgBodySessionID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 237, 0), )

    
    SessionID = property(__SessionID.value, __SessionID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAScheduleTupleID uses Python identifier SAScheduleTupleID
    __SAScheduleTupleID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), 'SAScheduleTupleID', '__urniso1511822013MsgBody_MeteringReceiptReqType_urniso1511822013MsgBodySAScheduleTupleID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 238, 0), )

    
    SAScheduleTupleID = property(__SAScheduleTupleID.value, __SAScheduleTupleID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}MeterInfo uses Python identifier MeterInfo
    __MeterInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), 'MeterInfo', '__urniso1511822013MsgBody_MeteringReceiptReqType_urniso1511822013MsgBodyMeterInfo', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 239, 0), )

    
    MeterInfo = property(__MeterInfo.value, __MeterInfo.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgBody}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgBody_MeteringReceiptReqType_urniso1511822013MsgBodyId', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 241, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 241, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __SessionID.name() : __SessionID,
        __SAScheduleTupleID.name() : __SAScheduleTupleID,
        __MeterInfo.name() : __MeterInfo
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.MeteringReceiptReqType = MeteringReceiptReqType
Namespace.addCategoryObject('typeBinding', 'MeteringReceiptReqType', MeteringReceiptReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}MeteringReceiptResType with content type ELEMENT_ONLY
class MeteringReceiptResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}MeteringReceiptResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeteringReceiptResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 246, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_MeteringReceiptResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 250, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDataTypes}EVSEStatus uses Python identifier EVSEStatus
    __EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus'), 'EVSEStatus', '__urniso1511822013MsgBody_MeteringReceiptResType_urniso1511822013MsgDataTypesEVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 259, 0), )

    
    EVSEStatus = property(__EVSEStatus.value, __EVSEStatus.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEStatus.name() : __EVSEStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MeteringReceiptResType = MeteringReceiptResType
Namespace.addCategoryObject('typeBinding', 'MeteringReceiptResType', MeteringReceiptResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}SessionStopReqType with content type ELEMENT_ONLY
class SessionStopReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}SessionStopReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SessionStopReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 260, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ChargingSession uses Python identifier ChargingSession
    __ChargingSession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingSession'), 'ChargingSession', '__urniso1511822013MsgBody_SessionStopReqType_urniso1511822013MsgBodyChargingSession', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 264, 0), )

    
    ChargingSession = property(__ChargingSession.value, __ChargingSession.set, None, None)

    _ElementMap.update({
        __ChargingSession.name() : __ChargingSession
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SessionStopReqType = SessionStopReqType
Namespace.addCategoryObject('typeBinding', 'SessionStopReqType', SessionStopReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}SessionStopResType with content type ELEMENT_ONLY
class SessionStopResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}SessionStopResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SessionStopResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 270, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_SessionStopResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 274, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SessionStopResType = SessionStopResType
Namespace.addCategoryObject('typeBinding', 'SessionStopResType', SessionStopResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CertificateUpdateReqType with content type ELEMENT_ONLY
class CertificateUpdateReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CertificateUpdateReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateUpdateReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 283, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureCertChain uses Python identifier ContractSignatureCertChain
    __ContractSignatureCertChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), 'ContractSignatureCertChain', '__urniso1511822013MsgBody_CertificateUpdateReqType_urniso1511822013MsgBodyContractSignatureCertChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 287, 0), )

    
    ContractSignatureCertChain = property(__ContractSignatureCertChain.value, __ContractSignatureCertChain.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}eMAID uses Python identifier eMAID
    __eMAID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), 'eMAID', '__urniso1511822013MsgBody_CertificateUpdateReqType_urniso1511822013MsgBodyeMAID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 288, 0), )

    
    eMAID = property(__eMAID.value, __eMAID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ListOfRootCertificateIDs uses Python identifier ListOfRootCertificateIDs
    __ListOfRootCertificateIDs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs'), 'ListOfRootCertificateIDs', '__urniso1511822013MsgBody_CertificateUpdateReqType_urniso1511822013MsgBodyListOfRootCertificateIDs', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 289, 0), )

    
    ListOfRootCertificateIDs = property(__ListOfRootCertificateIDs.value, __ListOfRootCertificateIDs.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgBody}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgBody_CertificateUpdateReqType_urniso1511822013MsgBodyId', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 291, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 291, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __ContractSignatureCertChain.name() : __ContractSignatureCertChain,
        __eMAID.name() : __eMAID,
        __ListOfRootCertificateIDs.name() : __ListOfRootCertificateIDs
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CertificateUpdateReqType = CertificateUpdateReqType
Namespace.addCategoryObject('typeBinding', 'CertificateUpdateReqType', CertificateUpdateReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CertificateUpdateResType with content type ELEMENT_ONLY
class CertificateUpdateResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CertificateUpdateResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateUpdateResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 296, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 300, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAProvisioningCertificateChain uses Python identifier SAProvisioningCertificateChain
    __SAProvisioningCertificateChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain'), 'SAProvisioningCertificateChain', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodySAProvisioningCertificateChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 301, 0), )

    
    SAProvisioningCertificateChain = property(__SAProvisioningCertificateChain.value, __SAProvisioningCertificateChain.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureCertChain uses Python identifier ContractSignatureCertChain
    __ContractSignatureCertChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), 'ContractSignatureCertChain', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyContractSignatureCertChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 302, 0), )

    
    ContractSignatureCertChain = property(__ContractSignatureCertChain.value, __ContractSignatureCertChain.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureEncryptedPrivateKey uses Python identifier ContractSignatureEncryptedPrivateKey
    __ContractSignatureEncryptedPrivateKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey'), 'ContractSignatureEncryptedPrivateKey', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyContractSignatureEncryptedPrivateKey', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 303, 0), )

    
    ContractSignatureEncryptedPrivateKey = property(__ContractSignatureEncryptedPrivateKey.value, __ContractSignatureEncryptedPrivateKey.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DHpublickey uses Python identifier DHpublickey
    __DHpublickey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey'), 'DHpublickey', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyDHpublickey', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 304, 0), )

    
    DHpublickey = property(__DHpublickey.value, __DHpublickey.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}eMAID uses Python identifier eMAID
    __eMAID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), 'eMAID', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyeMAID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 305, 0), )

    
    eMAID = property(__eMAID.value, __eMAID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}RetryCounter uses Python identifier RetryCounter
    __RetryCounter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RetryCounter'), 'RetryCounter', '__urniso1511822013MsgBody_CertificateUpdateResType_urniso1511822013MsgBodyRetryCounter', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 306, 0), )

    
    RetryCounter = property(__RetryCounter.value, __RetryCounter.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __SAProvisioningCertificateChain.name() : __SAProvisioningCertificateChain,
        __ContractSignatureCertChain.name() : __ContractSignatureCertChain,
        __ContractSignatureEncryptedPrivateKey.name() : __ContractSignatureEncryptedPrivateKey,
        __DHpublickey.name() : __DHpublickey,
        __eMAID.name() : __eMAID,
        __RetryCounter.name() : __RetryCounter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CertificateUpdateResType = CertificateUpdateResType
Namespace.addCategoryObject('typeBinding', 'CertificateUpdateResType', CertificateUpdateResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CertificateInstallationReqType with content type ELEMENT_ONLY
class CertificateInstallationReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CertificateInstallationReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateInstallationReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 315, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}OEMProvisioningCert uses Python identifier OEMProvisioningCert
    __OEMProvisioningCert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OEMProvisioningCert'), 'OEMProvisioningCert', '__urniso1511822013MsgBody_CertificateInstallationReqType_urniso1511822013MsgBodyOEMProvisioningCert', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 319, 0), )

    
    OEMProvisioningCert = property(__OEMProvisioningCert.value, __OEMProvisioningCert.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ListOfRootCertificateIDs uses Python identifier ListOfRootCertificateIDs
    __ListOfRootCertificateIDs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs'), 'ListOfRootCertificateIDs', '__urniso1511822013MsgBody_CertificateInstallationReqType_urniso1511822013MsgBodyListOfRootCertificateIDs', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 320, 0), )

    
    ListOfRootCertificateIDs = property(__ListOfRootCertificateIDs.value, __ListOfRootCertificateIDs.set, None, None)

    
    # Attribute {urn:iso:15118:2:2013:MsgBody}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urniso1511822013MsgBody_CertificateInstallationReqType_urniso1511822013MsgBodyId', pyxb.binding.datatypes.ID, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 322, 0)
    __Id._UseLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 322, 0)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __OEMProvisioningCert.name() : __OEMProvisioningCert,
        __ListOfRootCertificateIDs.name() : __ListOfRootCertificateIDs
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.CertificateInstallationReqType = CertificateInstallationReqType
Namespace.addCategoryObject('typeBinding', 'CertificateInstallationReqType', CertificateInstallationReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CertificateInstallationResType with content type ELEMENT_ONLY
class CertificateInstallationResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CertificateInstallationResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CertificateInstallationResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 327, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 331, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAProvisioningCertificateChain uses Python identifier SAProvisioningCertificateChain
    __SAProvisioningCertificateChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain'), 'SAProvisioningCertificateChain', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodySAProvisioningCertificateChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 332, 0), )

    
    SAProvisioningCertificateChain = property(__SAProvisioningCertificateChain.value, __SAProvisioningCertificateChain.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureCertChain uses Python identifier ContractSignatureCertChain
    __ContractSignatureCertChain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), 'ContractSignatureCertChain', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodyContractSignatureCertChain', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 334, 0), )

    
    ContractSignatureCertChain = property(__ContractSignatureCertChain.value, __ContractSignatureCertChain.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ContractSignatureEncryptedPrivateKey uses Python identifier ContractSignatureEncryptedPrivateKey
    __ContractSignatureEncryptedPrivateKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey'), 'ContractSignatureEncryptedPrivateKey', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodyContractSignatureEncryptedPrivateKey', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 335, 0), )

    
    ContractSignatureEncryptedPrivateKey = property(__ContractSignatureEncryptedPrivateKey.value, __ContractSignatureEncryptedPrivateKey.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DHpublickey uses Python identifier DHpublickey
    __DHpublickey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey'), 'DHpublickey', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodyDHpublickey', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 336, 0), )

    
    DHpublickey = property(__DHpublickey.value, __DHpublickey.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}eMAID uses Python identifier eMAID
    __eMAID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), 'eMAID', '__urniso1511822013MsgBody_CertificateInstallationResType_urniso1511822013MsgBodyeMAID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 337, 0), )

    
    eMAID = property(__eMAID.value, __eMAID.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __SAProvisioningCertificateChain.name() : __SAProvisioningCertificateChain,
        __ContractSignatureCertChain.name() : __ContractSignatureCertChain,
        __ContractSignatureEncryptedPrivateKey.name() : __ContractSignatureEncryptedPrivateKey,
        __DHpublickey.name() : __DHpublickey,
        __eMAID.name() : __eMAID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CertificateInstallationResType = CertificateInstallationResType
Namespace.addCategoryObject('typeBinding', 'CertificateInstallationResType', CertificateInstallationResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ChargingStatusReqType with content type EMPTY
class ChargingStatusReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ChargingStatusReqType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargingStatusReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 349, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargingStatusReqType = ChargingStatusReqType
Namespace.addCategoryObject('typeBinding', 'ChargingStatusReqType', ChargingStatusReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}ChargingStatusResType with content type ELEMENT_ONLY
class ChargingStatusResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}ChargingStatusResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChargingStatusResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 357, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 361, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEID uses Python identifier EVSEID
    __EVSEID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), 'EVSEID', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyEVSEID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 362, 0), )

    
    EVSEID = property(__EVSEID.value, __EVSEID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAScheduleTupleID uses Python identifier SAScheduleTupleID
    __SAScheduleTupleID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), 'SAScheduleTupleID', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodySAScheduleTupleID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 363, 0), )

    
    SAScheduleTupleID = property(__SAScheduleTupleID.value, __SAScheduleTupleID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEMaxCurrent uses Python identifier EVSEMaxCurrent
    __EVSEMaxCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent'), 'EVSEMaxCurrent', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyEVSEMaxCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 364, 0), )

    
    EVSEMaxCurrent = property(__EVSEMaxCurrent.value, __EVSEMaxCurrent.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}MeterInfo uses Python identifier MeterInfo
    __MeterInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), 'MeterInfo', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyMeterInfo', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 365, 0), )

    
    MeterInfo = property(__MeterInfo.value, __MeterInfo.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ReceiptRequired uses Python identifier ReceiptRequired
    __ReceiptRequired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired'), 'ReceiptRequired', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyReceiptRequired', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 366, 0), )

    
    ReceiptRequired = property(__ReceiptRequired.value, __ReceiptRequired.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}AC_EVSEStatus uses Python identifier AC_EVSEStatus
    __AC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus'), 'AC_EVSEStatus', '__urniso1511822013MsgBody_ChargingStatusResType_urniso1511822013MsgBodyAC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 367, 0), )

    
    AC_EVSEStatus = property(__AC_EVSEStatus.value, __AC_EVSEStatus.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __EVSEID.name() : __EVSEID,
        __SAScheduleTupleID.name() : __SAScheduleTupleID,
        __EVSEMaxCurrent.name() : __EVSEMaxCurrent,
        __MeterInfo.name() : __MeterInfo,
        __ReceiptRequired.name() : __ReceiptRequired,
        __AC_EVSEStatus.name() : __AC_EVSEStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChargingStatusResType = ChargingStatusResType
Namespace.addCategoryObject('typeBinding', 'ChargingStatusResType', ChargingStatusResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CableCheckReqType with content type ELEMENT_ONLY
class CableCheckReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CableCheckReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CableCheckReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 379, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgBody_CableCheckReqType_urniso1511822013MsgBodyDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 383, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CableCheckReqType = CableCheckReqType
Namespace.addCategoryObject('typeBinding', 'CableCheckReqType', CableCheckReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CableCheckResType with content type ELEMENT_ONLY
class CableCheckResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CableCheckResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CableCheckResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 389, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_CableCheckResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 393, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVSEStatus uses Python identifier DC_EVSEStatus
    __DC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), 'DC_EVSEStatus', '__urniso1511822013MsgBody_CableCheckResType_urniso1511822013MsgBodyDC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 394, 0), )

    
    DC_EVSEStatus = property(__DC_EVSEStatus.value, __DC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEProcessing uses Python identifier EVSEProcessing
    __EVSEProcessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), 'EVSEProcessing', '__urniso1511822013MsgBody_CableCheckResType_urniso1511822013MsgBodyEVSEProcessing', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 395, 0), )

    
    EVSEProcessing = property(__EVSEProcessing.value, __EVSEProcessing.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __DC_EVSEStatus.name() : __DC_EVSEStatus,
        __EVSEProcessing.name() : __EVSEProcessing
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CableCheckResType = CableCheckResType
Namespace.addCategoryObject('typeBinding', 'CableCheckResType', CableCheckResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PreChargeReqType with content type ELEMENT_ONLY
class PreChargeReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PreChargeReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PreChargeReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 404, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgBody_PreChargeReqType_urniso1511822013MsgBodyDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 408, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVTargetVoltage uses Python identifier EVTargetVoltage
    __EVTargetVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage'), 'EVTargetVoltage', '__urniso1511822013MsgBody_PreChargeReqType_urniso1511822013MsgBodyEVTargetVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 409, 0), )

    
    EVTargetVoltage = property(__EVTargetVoltage.value, __EVTargetVoltage.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVTargetCurrent uses Python identifier EVTargetCurrent
    __EVTargetCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent'), 'EVTargetCurrent', '__urniso1511822013MsgBody_PreChargeReqType_urniso1511822013MsgBodyEVTargetCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 410, 0), )

    
    EVTargetCurrent = property(__EVTargetCurrent.value, __EVTargetCurrent.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus,
        __EVTargetVoltage.name() : __EVTargetVoltage,
        __EVTargetCurrent.name() : __EVTargetCurrent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PreChargeReqType = PreChargeReqType
Namespace.addCategoryObject('typeBinding', 'PreChargeReqType', PreChargeReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}PreChargeResType with content type ELEMENT_ONLY
class PreChargeResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}PreChargeResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PreChargeResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 416, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_PreChargeResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 420, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVSEStatus uses Python identifier DC_EVSEStatus
    __DC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), 'DC_EVSEStatus', '__urniso1511822013MsgBody_PreChargeResType_urniso1511822013MsgBodyDC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 421, 0), )

    
    DC_EVSEStatus = property(__DC_EVSEStatus.value, __DC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEPresentVoltage uses Python identifier EVSEPresentVoltage
    __EVSEPresentVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), 'EVSEPresentVoltage', '__urniso1511822013MsgBody_PreChargeResType_urniso1511822013MsgBodyEVSEPresentVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 422, 0), )

    
    EVSEPresentVoltage = property(__EVSEPresentVoltage.value, __EVSEPresentVoltage.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __DC_EVSEStatus.name() : __DC_EVSEStatus,
        __EVSEPresentVoltage.name() : __EVSEPresentVoltage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PreChargeResType = PreChargeResType
Namespace.addCategoryObject('typeBinding', 'PreChargeResType', PreChargeResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CurrentDemandReqType with content type ELEMENT_ONLY
class CurrentDemandReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CurrentDemandReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrentDemandReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 431, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 435, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVTargetCurrent uses Python identifier EVTargetCurrent
    __EVTargetCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent'), 'EVTargetCurrent', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyEVTargetCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 436, 0), )

    
    EVTargetCurrent = property(__EVTargetCurrent.value, __EVTargetCurrent.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVMaximumVoltageLimit uses Python identifier EVMaximumVoltageLimit
    __EVMaximumVoltageLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit'), 'EVMaximumVoltageLimit', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyEVMaximumVoltageLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 437, 0), )

    
    EVMaximumVoltageLimit = property(__EVMaximumVoltageLimit.value, __EVMaximumVoltageLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVMaximumCurrentLimit uses Python identifier EVMaximumCurrentLimit
    __EVMaximumCurrentLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit'), 'EVMaximumCurrentLimit', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyEVMaximumCurrentLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 438, 0), )

    
    EVMaximumCurrentLimit = property(__EVMaximumCurrentLimit.value, __EVMaximumCurrentLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVMaximumPowerLimit uses Python identifier EVMaximumPowerLimit
    __EVMaximumPowerLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit'), 'EVMaximumPowerLimit', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyEVMaximumPowerLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 439, 0), )

    
    EVMaximumPowerLimit = property(__EVMaximumPowerLimit.value, __EVMaximumPowerLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}BulkChargingComplete uses Python identifier BulkChargingComplete
    __BulkChargingComplete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete'), 'BulkChargingComplete', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyBulkChargingComplete', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 440, 0), )

    
    BulkChargingComplete = property(__BulkChargingComplete.value, __BulkChargingComplete.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ChargingComplete uses Python identifier ChargingComplete
    __ChargingComplete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete'), 'ChargingComplete', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyChargingComplete', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 441, 0), )

    
    ChargingComplete = property(__ChargingComplete.value, __ChargingComplete.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}RemainingTimeToFullSoC uses Python identifier RemainingTimeToFullSoC
    __RemainingTimeToFullSoC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToFullSoC'), 'RemainingTimeToFullSoC', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyRemainingTimeToFullSoC', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 442, 0), )

    
    RemainingTimeToFullSoC = property(__RemainingTimeToFullSoC.value, __RemainingTimeToFullSoC.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}RemainingTimeToBulkSoC uses Python identifier RemainingTimeToBulkSoC
    __RemainingTimeToBulkSoC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToBulkSoC'), 'RemainingTimeToBulkSoC', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyRemainingTimeToBulkSoC', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 443, 0), )

    
    RemainingTimeToBulkSoC = property(__RemainingTimeToBulkSoC.value, __RemainingTimeToBulkSoC.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVTargetVoltage uses Python identifier EVTargetVoltage
    __EVTargetVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage'), 'EVTargetVoltage', '__urniso1511822013MsgBody_CurrentDemandReqType_urniso1511822013MsgBodyEVTargetVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 444, 0), )

    
    EVTargetVoltage = property(__EVTargetVoltage.value, __EVTargetVoltage.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus,
        __EVTargetCurrent.name() : __EVTargetCurrent,
        __EVMaximumVoltageLimit.name() : __EVMaximumVoltageLimit,
        __EVMaximumCurrentLimit.name() : __EVMaximumCurrentLimit,
        __EVMaximumPowerLimit.name() : __EVMaximumPowerLimit,
        __BulkChargingComplete.name() : __BulkChargingComplete,
        __ChargingComplete.name() : __ChargingComplete,
        __RemainingTimeToFullSoC.name() : __RemainingTimeToFullSoC,
        __RemainingTimeToBulkSoC.name() : __RemainingTimeToBulkSoC,
        __EVTargetVoltage.name() : __EVTargetVoltage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrentDemandReqType = CurrentDemandReqType
Namespace.addCategoryObject('typeBinding', 'CurrentDemandReqType', CurrentDemandReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}CurrentDemandResType with content type ELEMENT_ONLY
class CurrentDemandResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}CurrentDemandResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrentDemandResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 450, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 454, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVSEStatus uses Python identifier DC_EVSEStatus
    __DC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), 'DC_EVSEStatus', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyDC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 455, 0), )

    
    DC_EVSEStatus = property(__DC_EVSEStatus.value, __DC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEPresentVoltage uses Python identifier EVSEPresentVoltage
    __EVSEPresentVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), 'EVSEPresentVoltage', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEPresentVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 456, 0), )

    
    EVSEPresentVoltage = property(__EVSEPresentVoltage.value, __EVSEPresentVoltage.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEPresentCurrent uses Python identifier EVSEPresentCurrent
    __EVSEPresentCurrent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentCurrent'), 'EVSEPresentCurrent', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEPresentCurrent', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 457, 0), )

    
    EVSEPresentCurrent = property(__EVSEPresentCurrent.value, __EVSEPresentCurrent.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSECurrentLimitAchieved uses Python identifier EVSECurrentLimitAchieved
    __EVSECurrentLimitAchieved = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentLimitAchieved'), 'EVSECurrentLimitAchieved', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSECurrentLimitAchieved', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 458, 0), )

    
    EVSECurrentLimitAchieved = property(__EVSECurrentLimitAchieved.value, __EVSECurrentLimitAchieved.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEVoltageLimitAchieved uses Python identifier EVSEVoltageLimitAchieved
    __EVSEVoltageLimitAchieved = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEVoltageLimitAchieved'), 'EVSEVoltageLimitAchieved', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEVoltageLimitAchieved', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 459, 0), )

    
    EVSEVoltageLimitAchieved = property(__EVSEVoltageLimitAchieved.value, __EVSEVoltageLimitAchieved.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEPowerLimitAchieved uses Python identifier EVSEPowerLimitAchieved
    __EVSEPowerLimitAchieved = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPowerLimitAchieved'), 'EVSEPowerLimitAchieved', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEPowerLimitAchieved', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 460, 0), )

    
    EVSEPowerLimitAchieved = property(__EVSEPowerLimitAchieved.value, __EVSEPowerLimitAchieved.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEMaximumVoltageLimit uses Python identifier EVSEMaximumVoltageLimit
    __EVSEMaximumVoltageLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit'), 'EVSEMaximumVoltageLimit', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEMaximumVoltageLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 461, 0), )

    
    EVSEMaximumVoltageLimit = property(__EVSEMaximumVoltageLimit.value, __EVSEMaximumVoltageLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEMaximumCurrentLimit uses Python identifier EVSEMaximumCurrentLimit
    __EVSEMaximumCurrentLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit'), 'EVSEMaximumCurrentLimit', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEMaximumCurrentLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 462, 0), )

    
    EVSEMaximumCurrentLimit = property(__EVSEMaximumCurrentLimit.value, __EVSEMaximumCurrentLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEMaximumPowerLimit uses Python identifier EVSEMaximumPowerLimit
    __EVSEMaximumPowerLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit'), 'EVSEMaximumPowerLimit', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEMaximumPowerLimit', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 463, 0), )

    
    EVSEMaximumPowerLimit = property(__EVSEMaximumPowerLimit.value, __EVSEMaximumPowerLimit.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEID uses Python identifier EVSEID
    __EVSEID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), 'EVSEID', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyEVSEID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 464, 0), )

    
    EVSEID = property(__EVSEID.value, __EVSEID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}SAScheduleTupleID uses Python identifier SAScheduleTupleID
    __SAScheduleTupleID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), 'SAScheduleTupleID', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodySAScheduleTupleID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 465, 0), )

    
    SAScheduleTupleID = property(__SAScheduleTupleID.value, __SAScheduleTupleID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}MeterInfo uses Python identifier MeterInfo
    __MeterInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), 'MeterInfo', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyMeterInfo', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 466, 0), )

    
    MeterInfo = property(__MeterInfo.value, __MeterInfo.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}ReceiptRequired uses Python identifier ReceiptRequired
    __ReceiptRequired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired'), 'ReceiptRequired', '__urniso1511822013MsgBody_CurrentDemandResType_urniso1511822013MsgBodyReceiptRequired', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 467, 0), )

    
    ReceiptRequired = property(__ReceiptRequired.value, __ReceiptRequired.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __DC_EVSEStatus.name() : __DC_EVSEStatus,
        __EVSEPresentVoltage.name() : __EVSEPresentVoltage,
        __EVSEPresentCurrent.name() : __EVSEPresentCurrent,
        __EVSECurrentLimitAchieved.name() : __EVSECurrentLimitAchieved,
        __EVSEVoltageLimitAchieved.name() : __EVSEVoltageLimitAchieved,
        __EVSEPowerLimitAchieved.name() : __EVSEPowerLimitAchieved,
        __EVSEMaximumVoltageLimit.name() : __EVSEMaximumVoltageLimit,
        __EVSEMaximumCurrentLimit.name() : __EVSEMaximumCurrentLimit,
        __EVSEMaximumPowerLimit.name() : __EVSEMaximumPowerLimit,
        __EVSEID.name() : __EVSEID,
        __SAScheduleTupleID.name() : __SAScheduleTupleID,
        __MeterInfo.name() : __MeterInfo,
        __ReceiptRequired.name() : __ReceiptRequired
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CurrentDemandResType = CurrentDemandResType
Namespace.addCategoryObject('typeBinding', 'CurrentDemandResType', CurrentDemandResType)


# Complex type {urn:iso:15118:2:2013:MsgBody}WeldingDetectionReqType with content type ELEMENT_ONLY
class WeldingDetectionReqType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}WeldingDetectionReqType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeldingDetectionReqType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 476, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVStatus uses Python identifier DC_EVStatus
    __DC_EVStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), 'DC_EVStatus', '__urniso1511822013MsgBody_WeldingDetectionReqType_urniso1511822013MsgBodyDC_EVStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 480, 0), )

    
    DC_EVStatus = property(__DC_EVStatus.value, __DC_EVStatus.set, None, None)

    _ElementMap.update({
        __DC_EVStatus.name() : __DC_EVStatus
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WeldingDetectionReqType = WeldingDetectionReqType
Namespace.addCategoryObject('typeBinding', 'WeldingDetectionReqType', WeldingDetectionReqType)


# Complex type {urn:iso:15118:2:2013:MsgBody}WeldingDetectionResType with content type ELEMENT_ONLY
class WeldingDetectionResType (BodyBaseType):
    """Complex type {urn:iso:15118:2:2013:MsgBody}WeldingDetectionResType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WeldingDetectionResType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 486, 0)
    _ElementMap = BodyBaseType._ElementMap.copy()
    _AttributeMap = BodyBaseType._AttributeMap.copy()
    # Base type is BodyBaseType
    
    # Element {urn:iso:15118:2:2013:MsgBody}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__urniso1511822013MsgBody_WeldingDetectionResType_urniso1511822013MsgBodyResponseCode', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 490, 0), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}DC_EVSEStatus uses Python identifier DC_EVSEStatus
    __DC_EVSEStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), 'DC_EVSEStatus', '__urniso1511822013MsgBody_WeldingDetectionResType_urniso1511822013MsgBodyDC_EVSEStatus', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 491, 0), )

    
    DC_EVSEStatus = property(__DC_EVSEStatus.value, __DC_EVSEStatus.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgBody}EVSEPresentVoltage uses Python identifier EVSEPresentVoltage
    __EVSEPresentVoltage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), 'EVSEPresentVoltage', '__urniso1511822013MsgBody_WeldingDetectionResType_urniso1511822013MsgBodyEVSEPresentVoltage', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 492, 0), )

    
    EVSEPresentVoltage = property(__EVSEPresentVoltage.value, __EVSEPresentVoltage.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __DC_EVSEStatus.name() : __DC_EVSEStatus,
        __EVSEPresentVoltage.name() : __EVSEPresentVoltage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WeldingDetectionResType = WeldingDetectionResType
Namespace.addCategoryObject('typeBinding', 'WeldingDetectionResType', WeldingDetectionResType)


BodyElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BodyElement'), BodyBaseType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 15, 0))
Namespace.addCategoryObject('elementBinding', BodyElement.name().localName(), BodyElement)

SessionSetupReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionSetupReq'), SessionSetupReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 23, 0))
Namespace.addCategoryObject('elementBinding', SessionSetupReq.name().localName(), SessionSetupReq)

SessionSetupRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionSetupRes'), SessionSetupResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 33, 0))
Namespace.addCategoryObject('elementBinding', SessionSetupRes.name().localName(), SessionSetupRes)

ServiceDiscoveryReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceDiscoveryReq'), ServiceDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 48, 0))
Namespace.addCategoryObject('elementBinding', ServiceDiscoveryReq.name().localName(), ServiceDiscoveryReq)

ServiceDiscoveryRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceDiscoveryRes'), ServiceDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 59, 0))
Namespace.addCategoryObject('elementBinding', ServiceDiscoveryRes.name().localName(), ServiceDiscoveryRes)

ServiceDetailReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceDetailReq'), ServiceDetailReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 76, 0))
Namespace.addCategoryObject('elementBinding', ServiceDetailReq.name().localName(), ServiceDetailReq)

ServiceDetailRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceDetailRes'), ServiceDetailResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 86, 0))
Namespace.addCategoryObject('elementBinding', ServiceDetailRes.name().localName(), ServiceDetailRes)

PaymentServiceSelectionReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentServiceSelectionReq'), PaymentServiceSelectionReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 101, 0))
Namespace.addCategoryObject('elementBinding', PaymentServiceSelectionReq.name().localName(), PaymentServiceSelectionReq)

PaymentServiceSelectionRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentServiceSelectionRes'), PaymentServiceSelectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 112, 0))
Namespace.addCategoryObject('elementBinding', PaymentServiceSelectionRes.name().localName(), PaymentServiceSelectionRes)

PaymentDetailsReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentDetailsReq'), PaymentDetailsReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 125, 0))
Namespace.addCategoryObject('elementBinding', PaymentDetailsReq.name().localName(), PaymentDetailsReq)

PaymentDetailsRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentDetailsRes'), PaymentDetailsResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 136, 0))
Namespace.addCategoryObject('elementBinding', PaymentDetailsRes.name().localName(), PaymentDetailsRes)

AuthorizationReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuthorizationReq'), AuthorizationReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 151, 0))
Namespace.addCategoryObject('elementBinding', AuthorizationReq.name().localName(), AuthorizationReq)

AuthorizationRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuthorizationRes'), AuthorizationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 162, 0))
Namespace.addCategoryObject('elementBinding', AuthorizationRes.name().localName(), AuthorizationRes)

ChargeParameterDiscoveryReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargeParameterDiscoveryReq'), ChargeParameterDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 176, 0))
Namespace.addCategoryObject('elementBinding', ChargeParameterDiscoveryReq.name().localName(), ChargeParameterDiscoveryReq)

ChargeParameterDiscoveryRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargeParameterDiscoveryRes'), ChargeParameterDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 189, 0))
Namespace.addCategoryObject('elementBinding', ChargeParameterDiscoveryRes.name().localName(), ChargeParameterDiscoveryRes)

PowerDeliveryReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PowerDeliveryReq'), PowerDeliveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 205, 0))
Namespace.addCategoryObject('elementBinding', PowerDeliveryReq.name().localName(), PowerDeliveryReq)

PowerDeliveryRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PowerDeliveryRes'), PowerDeliveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 218, 0))
Namespace.addCategoryObject('elementBinding', PowerDeliveryRes.name().localName(), PowerDeliveryRes)

MeteringReceiptReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeteringReceiptReq'), MeteringReceiptReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 232, 0))
Namespace.addCategoryObject('elementBinding', MeteringReceiptReq.name().localName(), MeteringReceiptReq)

MeteringReceiptRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeteringReceiptRes'), MeteringReceiptResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 245, 0))
Namespace.addCategoryObject('elementBinding', MeteringReceiptRes.name().localName(), MeteringReceiptRes)

SessionStopReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionStopReq'), SessionStopReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 259, 0))
Namespace.addCategoryObject('elementBinding', SessionStopReq.name().localName(), SessionStopReq)

SessionStopRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionStopRes'), SessionStopResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 269, 0))
Namespace.addCategoryObject('elementBinding', SessionStopRes.name().localName(), SessionStopRes)

CertificateUpdateReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateUpdateReq'), CertificateUpdateReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 282, 0))
Namespace.addCategoryObject('elementBinding', CertificateUpdateReq.name().localName(), CertificateUpdateReq)

CertificateUpdateRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateUpdateRes'), CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 295, 0))
Namespace.addCategoryObject('elementBinding', CertificateUpdateRes.name().localName(), CertificateUpdateRes)

CertificateInstallationReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateInstallationReq'), CertificateInstallationReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 314, 0))
Namespace.addCategoryObject('elementBinding', CertificateInstallationReq.name().localName(), CertificateInstallationReq)

CertificateInstallationRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertificateInstallationRes'), CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 326, 0))
Namespace.addCategoryObject('elementBinding', CertificateInstallationRes.name().localName(), CertificateInstallationRes)

ChargingStatusReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingStatusReq'), ChargingStatusReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 348, 0))
Namespace.addCategoryObject('elementBinding', ChargingStatusReq.name().localName(), ChargingStatusReq)

ChargingStatusRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingStatusRes'), ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 356, 0))
Namespace.addCategoryObject('elementBinding', ChargingStatusRes.name().localName(), ChargingStatusRes)

CableCheckReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CableCheckReq'), CableCheckReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 378, 0))
Namespace.addCategoryObject('elementBinding', CableCheckReq.name().localName(), CableCheckReq)

CableCheckRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CableCheckRes'), CableCheckResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 388, 0))
Namespace.addCategoryObject('elementBinding', CableCheckRes.name().localName(), CableCheckRes)

PreChargeReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreChargeReq'), PreChargeReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 403, 0))
Namespace.addCategoryObject('elementBinding', PreChargeReq.name().localName(), PreChargeReq)

PreChargeRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreChargeRes'), PreChargeResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 415, 0))
Namespace.addCategoryObject('elementBinding', PreChargeRes.name().localName(), PreChargeRes)

CurrentDemandReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CurrentDemandReq'), CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 430, 0))
Namespace.addCategoryObject('elementBinding', CurrentDemandReq.name().localName(), CurrentDemandReq)

CurrentDemandRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CurrentDemandRes'), CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 449, 0))
Namespace.addCategoryObject('elementBinding', CurrentDemandRes.name().localName(), CurrentDemandRes)

WeldingDetectionReq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WeldingDetectionReq'), WeldingDetectionReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 475, 0))
Namespace.addCategoryObject('elementBinding', WeldingDetectionReq.name().localName(), WeldingDetectionReq)

WeldingDetectionRes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WeldingDetectionRes'), WeldingDetectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 485, 0))
Namespace.addCategoryObject('elementBinding', WeldingDetectionRes.name().localName(), WeldingDetectionRes)



BodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BodyElement'), BodyBaseType, abstract=pyxb.binding.datatypes.boolean(1), scope=BodyType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 15, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 12, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BodyElement')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 12, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BodyType._Automaton = _BuildAutomaton()




SessionSetupReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVCCID'), _ImportedBinding__v2gci_t.evccIDType, scope=SessionSetupReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 28, 0)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SessionSetupReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVCCID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 28, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SessionSetupReqType._Automaton = _BuildAutomaton_()




SessionSetupResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=SessionSetupResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 38, 0)))

SessionSetupResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), _ImportedBinding__v2gci_t.evseIDType, scope=SessionSetupResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 39, 0)))

SessionSetupResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp'), pyxb.binding.datatypes.long, scope=SessionSetupResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 40, 0)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 40, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SessionSetupResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 38, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SessionSetupResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 39, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SessionSetupResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 40, 0))
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
SessionSetupResType._Automaton = _BuildAutomaton_2()




ServiceDiscoveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope'), _ImportedBinding__v2gci_t.serviceScopeType, scope=ServiceDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 53, 0)))

ServiceDiscoveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory'), _ImportedBinding__v2gci_t.serviceCategoryType, scope=ServiceDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 54, 0)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 53, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 54, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceScope')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 53, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceCategory')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 54, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ServiceDiscoveryReqType._Automaton = _BuildAutomaton_3()




ServiceDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=ServiceDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 64, 0)))

ServiceDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionList'), _ImportedBinding__v2gci_t.PaymentOptionListType, scope=ServiceDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 65, 0)))

ServiceDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargeService'), _ImportedBinding__v2gci_t.ChargeServiceType, scope=ServiceDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 66, 0)))

ServiceDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceList'), _ImportedBinding__v2gci_t.ServiceListType, scope=ServiceDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 68, 0)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 68, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 64, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PaymentOptionList')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 65, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargeService')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 66, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ServiceDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceList')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 68, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceDiscoveryResType._Automaton = _BuildAutomaton_4()




ServiceDetailReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), _ImportedBinding__v2gci_t.serviceIDType, scope=ServiceDetailReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 81, 0)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceDetailReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 81, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ServiceDetailReqType._Automaton = _BuildAutomaton_5()




ServiceDetailResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=ServiceDetailResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 91, 0)))

ServiceDetailResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceID'), _ImportedBinding__v2gci_t.serviceIDType, scope=ServiceDetailResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 92, 0)))

ServiceDetailResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ServiceParameterList'), _ImportedBinding__v2gci_t.ServiceParameterListType, scope=ServiceDetailResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 93, 0)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 93, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ServiceDetailResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 91, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ServiceDetailResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 92, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ServiceDetailResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ServiceParameterList')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 93, 0))
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
ServiceDetailResType._Automaton = _BuildAutomaton_6()




PaymentServiceSelectionReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SelectedPaymentOption'), _ImportedBinding__v2gci_t.paymentOptionType, scope=PaymentServiceSelectionReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 106, 0)))

PaymentServiceSelectionReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SelectedServiceList'), _ImportedBinding__v2gci_t.SelectedServiceListType, scope=PaymentServiceSelectionReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 107, 0)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentServiceSelectionReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SelectedPaymentOption')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 106, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentServiceSelectionReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SelectedServiceList')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 107, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentServiceSelectionReqType._Automaton = _BuildAutomaton_7()




PaymentServiceSelectionResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=PaymentServiceSelectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 117, 0)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentServiceSelectionResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 117, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentServiceSelectionResType._Automaton = _BuildAutomaton_8()




PaymentDetailsReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), _ImportedBinding__v2gci_t.eMAIDType, scope=PaymentDetailsReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 130, 0)))

PaymentDetailsReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=PaymentDetailsReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 131, 0)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentDetailsReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMAID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 130, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentDetailsReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 131, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentDetailsReqType._Automaton = _BuildAutomaton_9()




PaymentDetailsResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=PaymentDetailsResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 141, 0)))

PaymentDetailsResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge'), _ImportedBinding__v2gci_t.genChallengeType, scope=PaymentDetailsResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 142, 0)))

PaymentDetailsResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp'), pyxb.binding.datatypes.long, scope=PaymentDetailsResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 143, 0)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentDetailsResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 141, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentDetailsResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 142, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentDetailsResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSETimeStamp')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 143, 0))
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
PaymentDetailsResType._Automaton = _BuildAutomaton_10()




AuthorizationReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge'), _ImportedBinding__v2gci_t.genChallengeType, scope=AuthorizationReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 156, 0)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 156, 0))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AuthorizationReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GenChallenge')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 156, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AuthorizationReqType._Automaton = _BuildAutomaton_11()




AuthorizationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=AuthorizationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 167, 0)))

AuthorizationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), _ImportedBinding__v2gci_t.EVSEProcessingType, scope=AuthorizationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 168, 0)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AuthorizationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 167, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AuthorizationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 168, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AuthorizationResType._Automaton = _BuildAutomaton_12()




ChargeParameterDiscoveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxEntriesSAScheduleTuple'), pyxb.binding.datatypes.unsignedShort, scope=ChargeParameterDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 181, 0)))

ChargeParameterDiscoveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestedEnergyTransferMode'), _ImportedBinding__v2gci_t.EnergyTransferModeType, scope=ChargeParameterDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 183, 0)))

ChargeParameterDiscoveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVChargeParameter'), _ImportedBinding__v2gci_t.EVChargeParameterType, abstract=pyxb.binding.datatypes.boolean(1), scope=ChargeParameterDiscoveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 303, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 181, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxEntriesSAScheduleTuple')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 181, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestedEnergyTransferMode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 183, 0))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryReqType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVChargeParameter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 184, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChargeParameterDiscoveryReqType._Automaton = _BuildAutomaton_13()




ChargeParameterDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=ChargeParameterDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 194, 0)))

ChargeParameterDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), _ImportedBinding__v2gci_t.EVSEProcessingType, scope=ChargeParameterDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 195, 0)))

ChargeParameterDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'SASchedules'), _ImportedBinding__v2gci_t.SASchedulesType, abstract=pyxb.binding.datatypes.boolean(1), scope=ChargeParameterDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 151, 0)))

ChargeParameterDiscoveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEChargeParameter'), _ImportedBinding__v2gci_t.EVSEChargeParameterType, abstract=pyxb.binding.datatypes.boolean(1), scope=ChargeParameterDiscoveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 335, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 196, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 194, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 195, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'SASchedules')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 196, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChargeParameterDiscoveryResType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEChargeParameter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 197, 0))
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
ChargeParameterDiscoveryResType._Automaton = _BuildAutomaton_14()




PowerDeliveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargeProgress'), _ImportedBinding__v2gci_t.chargeProgressType, scope=PowerDeliveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 210, 0)))

PowerDeliveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), _ImportedBinding__v2gci_t.SAIDType, scope=PowerDeliveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 211, 0)))

PowerDeliveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfile'), _ImportedBinding__v2gci_t.ChargingProfileType, scope=PowerDeliveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 212, 0)))

PowerDeliveryReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVPowerDeliveryParameter'), _ImportedBinding__v2gci_t.EVPowerDeliveryParameterType, abstract=pyxb.binding.datatypes.boolean(1), scope=PowerDeliveryReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 371, 0)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 212, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 213, 0))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargeProgress')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 210, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 211, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingProfile')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 212, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryReqType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVPowerDeliveryParameter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 213, 0))
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PowerDeliveryReqType._Automaton = _BuildAutomaton_15()




PowerDeliveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=PowerDeliveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 223, 0)))

PowerDeliveryResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus'), _ImportedBinding__v2gci_t.EVSEStatusType, abstract=pyxb.binding.datatypes.boolean(1), scope=PowerDeliveryResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 259, 0)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 223, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PowerDeliveryResType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 224, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PowerDeliveryResType._Automaton = _BuildAutomaton_16()




MeteringReceiptReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionID'), _ImportedBinding__v2gci_t.sessionIDType, scope=MeteringReceiptReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 237, 0)))

MeteringReceiptReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), _ImportedBinding__v2gci_t.SAIDType, scope=MeteringReceiptReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 238, 0)))

MeteringReceiptReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), _ImportedBinding__v2gci_t.MeterInfoType, scope=MeteringReceiptReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 239, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 238, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeteringReceiptReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SessionID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 237, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeteringReceiptReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 238, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeteringReceiptReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 239, 0))
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
MeteringReceiptReqType._Automaton = _BuildAutomaton_17()




MeteringReceiptResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=MeteringReceiptResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 250, 0)))

MeteringReceiptResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus'), _ImportedBinding__v2gci_t.EVSEStatusType, abstract=pyxb.binding.datatypes.boolean(1), scope=MeteringReceiptResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDataTypes.xsd', 259, 0)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeteringReceiptResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 250, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeteringReceiptResType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_v2gci_t, 'EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 251, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeteringReceiptResType._Automaton = _BuildAutomaton_18()




SessionStopReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingSession'), _ImportedBinding__v2gci_t.chargingSessionType, scope=SessionStopReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 264, 0)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SessionStopReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingSession')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 264, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SessionStopReqType._Automaton = _BuildAutomaton_19()




SessionStopResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=SessionStopResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 274, 0)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SessionStopResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 274, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SessionStopResType._Automaton = _BuildAutomaton_20()




CertificateUpdateReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=CertificateUpdateReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 287, 0)))

CertificateUpdateReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), _ImportedBinding__v2gci_t.eMAIDType, scope=CertificateUpdateReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 288, 0)))

CertificateUpdateReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs'), _ImportedBinding__v2gci_t.ListOfRootCertificateIDsType, scope=CertificateUpdateReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 289, 0)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 287, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMAID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 288, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 289, 0))
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
CertificateUpdateReqType._Automaton = _BuildAutomaton_21()




CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 300, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 301, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 302, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey'), _ImportedBinding__v2gci_t.ContractSignatureEncryptedPrivateKeyType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 303, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey'), _ImportedBinding__v2gci_t.DiffieHellmanPublickeyType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 304, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), _ImportedBinding__v2gci_t.EMAIDType, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 305, 0)))

CertificateUpdateResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RetryCounter'), pyxb.binding.datatypes.short, scope=CertificateUpdateResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 306, 0)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 306, 0))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 300, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 301, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 302, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 303, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 304, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMAID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 305, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CertificateUpdateResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RetryCounter')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 306, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertificateUpdateResType._Automaton = _BuildAutomaton_22()




CertificateInstallationReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OEMProvisioningCert'), _ImportedBinding__v2gci_t.certificateType, scope=CertificateInstallationReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 319, 0)))

CertificateInstallationReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs'), _ImportedBinding__v2gci_t.ListOfRootCertificateIDsType, scope=CertificateInstallationReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 320, 0)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OEMProvisioningCert')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 319, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListOfRootCertificateIDs')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 320, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertificateInstallationReqType._Automaton = _BuildAutomaton_23()




CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 331, 0)))

CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 332, 0)))

CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain'), _ImportedBinding__v2gci_t.CertificateChainType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 334, 0)))

CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey'), _ImportedBinding__v2gci_t.ContractSignatureEncryptedPrivateKeyType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 335, 0)))

CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey'), _ImportedBinding__v2gci_t.DiffieHellmanPublickeyType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 336, 0)))

CertificateInstallationResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMAID'), _ImportedBinding__v2gci_t.EMAIDType, scope=CertificateInstallationResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 337, 0)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 331, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAProvisioningCertificateChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 332, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureCertChain')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 334, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContractSignatureEncryptedPrivateKey')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 335, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DHpublickey')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 336, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CertificateInstallationResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMAID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 337, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CertificateInstallationResType._Automaton = _BuildAutomaton_24()




ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 361, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), _ImportedBinding__v2gci_t.evseIDType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 362, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), _ImportedBinding__v2gci_t.SAIDType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 363, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 364, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), _ImportedBinding__v2gci_t.MeterInfoType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 365, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired'), pyxb.binding.datatypes.boolean, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 366, 0)))

ChargingStatusResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus'), _ImportedBinding__v2gci_t.AC_EVSEStatusType, scope=ChargingStatusResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 367, 0)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 364, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 365, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 366, 0))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 361, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 362, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 363, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaxCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 364, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 365, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 366, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChargingStatusResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 367, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChargingStatusResType._Automaton = _BuildAutomaton_25()




CableCheckReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), _ImportedBinding__v2gci_t.DC_EVStatusType, scope=CableCheckReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 383, 0)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CableCheckReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 383, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CableCheckReqType._Automaton = _BuildAutomaton_26()




CableCheckResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=CableCheckResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 393, 0)))

CableCheckResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), _ImportedBinding__v2gci_t.DC_EVSEStatusType, scope=CableCheckResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 394, 0)))

CableCheckResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing'), _ImportedBinding__v2gci_t.EVSEProcessingType, scope=CableCheckResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 395, 0)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CableCheckResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 393, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CableCheckResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 394, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CableCheckResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEProcessing')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 395, 0))
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
CableCheckResType._Automaton = _BuildAutomaton_27()




PreChargeReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), _ImportedBinding__v2gci_t.DC_EVStatusType, scope=PreChargeReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 408, 0)))

PreChargeReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=PreChargeReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 409, 0)))

PreChargeReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=PreChargeReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 410, 0)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PreChargeReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 408, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PreChargeReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 409, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PreChargeReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 410, 0))
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
PreChargeReqType._Automaton = _BuildAutomaton_28()




PreChargeResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=PreChargeResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 420, 0)))

PreChargeResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), _ImportedBinding__v2gci_t.DC_EVSEStatusType, scope=PreChargeResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 421, 0)))

PreChargeResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=PreChargeResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 422, 0)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PreChargeResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 420, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PreChargeResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 421, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PreChargeResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 422, 0))
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
PreChargeResType._Automaton = _BuildAutomaton_29()




CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), _ImportedBinding__v2gci_t.DC_EVStatusType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 435, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 436, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 437, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 438, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 439, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete'), pyxb.binding.datatypes.boolean, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 440, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete'), pyxb.binding.datatypes.boolean, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 441, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToFullSoC'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 442, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToBulkSoC'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 443, 0)))

CurrentDemandReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 444, 0)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 437, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 438, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 439, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 440, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 442, 0))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 443, 0))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 435, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVTargetCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 436, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumVoltageLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 437, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumCurrentLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 438, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVMaximumPowerLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 439, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BulkChargingComplete')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 440, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargingComplete')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 441, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToFullSoC')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 442, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RemainingTimeToBulkSoC')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 443, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrentDemandReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVTargetVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 444, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurrentDemandReqType._Automaton = _BuildAutomaton_30()




CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 454, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), _ImportedBinding__v2gci_t.DC_EVSEStatusType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 455, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 456, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentCurrent'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 457, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentLimitAchieved'), pyxb.binding.datatypes.boolean, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 458, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEVoltageLimitAchieved'), pyxb.binding.datatypes.boolean, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 459, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPowerLimitAchieved'), pyxb.binding.datatypes.boolean, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 460, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 461, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 462, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 463, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEID'), _ImportedBinding__v2gci_t.evseIDType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 464, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID'), _ImportedBinding__v2gci_t.SAIDType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 465, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo'), _ImportedBinding__v2gci_t.MeterInfoType, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 466, 0)))

CurrentDemandResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired'), pyxb.binding.datatypes.boolean, scope=CurrentDemandResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 467, 0)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 461, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 462, 0))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 463, 0))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 466, 0))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 467, 0))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 454, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 455, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 456, 0))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentCurrent')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 457, 0))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSECurrentLimitAchieved')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 458, 0))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEVoltageLimitAchieved')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 459, 0))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPowerLimitAchieved')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 460, 0))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumVoltageLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 461, 0))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumCurrentLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 462, 0))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEMaximumPowerLimit')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 463, 0))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 464, 0))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SAScheduleTupleID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 465, 0))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeterInfo')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 466, 0))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CurrentDemandResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReceiptRequired')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 467, 0))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CurrentDemandResType._Automaton = _BuildAutomaton_31()




WeldingDetectionReqType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus'), _ImportedBinding__v2gci_t.DC_EVStatusType, scope=WeldingDetectionReqType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 480, 0)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WeldingDetectionReqType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 480, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WeldingDetectionReqType._Automaton = _BuildAutomaton_32()




WeldingDetectionResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), _ImportedBinding__v2gci_t.responseCodeType, scope=WeldingDetectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 490, 0)))

WeldingDetectionResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus'), _ImportedBinding__v2gci_t.DC_EVSEStatusType, scope=WeldingDetectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 491, 0)))

WeldingDetectionResType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage'), _ImportedBinding__v2gci_t.PhysicalValueType, scope=WeldingDetectionResType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 492, 0)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WeldingDetectionResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 490, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WeldingDetectionResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DC_EVSEStatus')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 491, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WeldingDetectionResType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EVSEPresentVoltage')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgBody.xsd', 492, 0))
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
WeldingDetectionResType._Automaton = _BuildAutomaton_33()


SessionSetupReq._setSubstitutionGroup(BodyElement)

SessionSetupRes._setSubstitutionGroup(BodyElement)

ServiceDiscoveryReq._setSubstitutionGroup(BodyElement)

ServiceDiscoveryRes._setSubstitutionGroup(BodyElement)

ServiceDetailReq._setSubstitutionGroup(BodyElement)

ServiceDetailRes._setSubstitutionGroup(BodyElement)

PaymentServiceSelectionReq._setSubstitutionGroup(BodyElement)

PaymentServiceSelectionRes._setSubstitutionGroup(BodyElement)

PaymentDetailsReq._setSubstitutionGroup(BodyElement)

PaymentDetailsRes._setSubstitutionGroup(BodyElement)

AuthorizationReq._setSubstitutionGroup(BodyElement)

AuthorizationRes._setSubstitutionGroup(BodyElement)

ChargeParameterDiscoveryReq._setSubstitutionGroup(BodyElement)

ChargeParameterDiscoveryRes._setSubstitutionGroup(BodyElement)

PowerDeliveryReq._setSubstitutionGroup(BodyElement)

PowerDeliveryRes._setSubstitutionGroup(BodyElement)

MeteringReceiptReq._setSubstitutionGroup(BodyElement)

MeteringReceiptRes._setSubstitutionGroup(BodyElement)

SessionStopReq._setSubstitutionGroup(BodyElement)

SessionStopRes._setSubstitutionGroup(BodyElement)

CertificateUpdateReq._setSubstitutionGroup(BodyElement)

CertificateUpdateRes._setSubstitutionGroup(BodyElement)

CertificateInstallationReq._setSubstitutionGroup(BodyElement)

CertificateInstallationRes._setSubstitutionGroup(BodyElement)

ChargingStatusReq._setSubstitutionGroup(BodyElement)

ChargingStatusRes._setSubstitutionGroup(BodyElement)

CableCheckReq._setSubstitutionGroup(BodyElement)

CableCheckRes._setSubstitutionGroup(BodyElement)

PreChargeReq._setSubstitutionGroup(BodyElement)

PreChargeRes._setSubstitutionGroup(BodyElement)

CurrentDemandReq._setSubstitutionGroup(BodyElement)

CurrentDemandRes._setSubstitutionGroup(BodyElement)

WeldingDetectionReq._setSubstitutionGroup(BodyElement)

WeldingDetectionRes._setSubstitutionGroup(BodyElement)
