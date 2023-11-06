import sys
import pyxb
import datetime
import xml.dom.minidom

sys.path.append('../')
from v2gMessages import msgDef


msg = msgDef.V2G_Message()
msg.Header = pyxb.BIND()#msgDef.MessageHeaderType()
msg.Header.SessionID = bytes.fromhex('123456789abc')
msg.Header.Notification = pyxb.BIND()#v2gci_t.NotificationType()
msg.Header.Notification.FaultCode = 'UnknownError'
msg.Header.Notification.FaultMsg = 'lorem ipsum'
#msg.Header.Signature = msgDef.SignatureType()


msg.Body = pyxb.BIND()#msgDef.BodyType()

msg.Body.BodyElement = msgDef.SessionSetupRes()
msg.Body.BodyElement.EVSEID = 'test-evse-id'
msg.Body.BodyElement.EVSETimeStamp = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
msg.Body.BodyElement.ResponseCode = 'OK'

xmlmsg = xml.dom.minidom.parseString(msg.toxml('utf-8')).toprettyxml()

print(xmlmsg)

print('---')

msg.reset()
msg = msgDef.CreateFromDocument(xmlmsg)
print(f'msg.Header.SessionID               = {msg.Header.SessionID.hex()}')
print(f'msg.Header.Notification.FaultCode  = {msg.Header.Notification.FaultCode}')
print(f'msg.Header.Notification.FaultMsg   = {msg.Header.Notification.FaultMsg}')
print(f'msg.Body.BodyElement.EVSEID        = {msg.Body.BodyElement.EVSEID}')
print(f'msg.Body.BodyElement.EVSETimeStamp = {msg.Body.BodyElement.EVSETimeStamp}')
print(f'msg.Body.BodyElement.ResponseCode  = {msg.Body.BodyElement.ResponseCode}')

