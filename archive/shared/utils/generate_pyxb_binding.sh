#!/bin/bash

SELFDIR=$(dirname $(realpath $0))
(cd ../v2gMessages ; pyxbgen -u ../schemas/V2G_CI_MsgDef.xsd -m _v2gci_d)
