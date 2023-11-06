import pyxb
import pyxb.utils.domutils

import _xmlsig
import _v2gci_d
import _v2gci_t
import _v2gci_h
import _v2gci_b
from _xmlsig import *
from _v2gci_d import *
from _v2gci_t import *
from _v2gci_h import *
from _v2gci_b import *

pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_xmlsig.Namespace, 'xmlsig')
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_v2gci_d.Namespace, 'v2gci_d')
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_v2gci_t.Namespace, 'v2gci_t')
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_v2gci_h.Namespace, 'v2gci_h')
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(_v2gci_b.Namespace, 'v2gci_b')
