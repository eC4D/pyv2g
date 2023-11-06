# ./_v2gci_d.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4376ac69a3ab116bfa11e5f3e1b816126059b34e
# Generated 2021-07-04 00:14:40.052414 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace urn:iso:15118:2:2013:MsgDef

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
import _v2gci_h as _ImportedBinding__v2gci_h
import _v2gci_b as _ImportedBinding__v2gci_b

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:iso:15118:2:2013:MsgDef', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 11, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:iso:15118:2:2013:MsgDef}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__urniso1511822013MsgDef_CTD_ANON_urniso1511822013MsgDefHeader', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 13, 0), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {urn:iso:15118:2:2013:MsgDef}Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Body'), 'Body', '__urniso1511822013MsgDef_CTD_ANON_urniso1511822013MsgDefBody', False, pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 14, 0), )

    
    Body = property(__Body.value, __Body.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header,
        __Body.name() : __Body
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


V2G_Message = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'V2G_Message'), CTD_ANON, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 10, 0))
Namespace.addCategoryObject('elementBinding', V2G_Message.name().localName(), V2G_Message)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), _ImportedBinding__v2gci_h.MessageHeaderType, scope=CTD_ANON, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 13, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Body'), _ImportedBinding__v2gci_b.BodyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 14, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 13, 0))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Body')), pyxb.utils.utility.Location('../shared/schemas/V2G_CI_MsgDef.xsd', 14, 0))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

