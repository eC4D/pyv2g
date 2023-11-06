# ./_v2gci_h.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b8afe9ee122f351f84b24d0a7db48b41fff65c20
# Generated 2021-07-04 00:14:40.050406 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace urn:iso:15118:2:2013:MsgHeader [xmlns:v2gci_h]

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
import _v2gci_t as _ImportedBinding__v2gci_t

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:iso:15118:2:2013:MsgHeader', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xmlsig = _ImportedBinding__xmlsig.Namespace
_Namespace_xmlsig.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {urn:iso:15118:2:2013:MsgHeader}MessageHeaderType with content type ELEMENT_ONLY
class MessageHeaderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:iso:15118:2:2013:MsgHeader}MessageHeaderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageHeaderType')
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 11, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xmlsig, 'Signature'), 'Signature', '__urniso1511822013MsgHeader_MessageHeaderType_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('../shared/schemas/xmldsig-core-schema.xsd', 7, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgHeader}SessionID uses Python identifier SessionID
    __SessionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SessionID'), 'SessionID', '__urniso1511822013MsgHeader_MessageHeaderType_urniso1511822013MsgHeaderSessionID', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 13, 0), )

    
    SessionID = property(__SessionID.value, __SessionID.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgHeader}Notification uses Python identifier Notification
    __Notification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Notification'), 'Notification', '__urniso1511822013MsgHeader_MessageHeaderType_urniso1511822013MsgHeaderNotification', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 14, 0), )

    
    Notification = property(__Notification.value, __Notification.set, None, None)

    _ElementMap.update({
        __Signature.name() : __Signature,
        __SessionID.name() : __SessionID,
        __Notification.name() : __Notification
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MessageHeaderType = MessageHeaderType
Namespace.addCategoryObject('typeBinding', 'MessageHeaderType', MessageHeaderType)




MessageHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xmlsig, 'Signature'), _ImportedBinding__xmlsig.SignatureType, scope=MessageHeaderType, location=pyxb.utils.utility.Location('../shared/schemas/xmldsig-core-schema.xsd', 7, 0)))

MessageHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SessionID'), _ImportedBinding__v2gci_t.sessionIDType, scope=MessageHeaderType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 13, 0)))

MessageHeaderType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Notification'), _ImportedBinding__v2gci_t.NotificationType, scope=MessageHeaderType, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 14, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 14, 0))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 15, 0))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MessageHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SessionID')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 13, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MessageHeaderType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Notification')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 14, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MessageHeaderType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xmlsig, 'Signature')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgHeader.xsd', 15, 0))
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
MessageHeaderType._Automaton = _BuildAutomaton()

