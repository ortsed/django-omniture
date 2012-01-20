from suds.client import Client
from suds.wsse import *
import base64
import hashlib
import cStringIO
import random
import datetime

OWS_USERNAME = 'lhinkesjones:Atlantic Media'
OWS_SECRET = '3eedbd1e56abf554702ff620b357cc01'

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.transport').setLevel(logging.DEBUG)
#logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
#logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)



string = cStringIO.StringIO ()
for i in random.sample('abcdefghijklmnopqrstuvwxyz0123456789',32):
	string.write (i)
nonce = string.getvalue ()
string.close ()

created = datetime.datetime.today ()
soap_date = created.strftime("%Y-%m-%d %H:%M:%S")
password = base64.b64encode(hashlib.sha1(nonce + soap_date + OWS_SECRET).hexdigest())






token = UsernameToken(OWS_USERNAME, password)
token.setnonce(nonce)
token.setcreated (soap_date)

security = Security()
security.tokens.append(token)

client = Client('OmnitureAdminServices.wsdl', cache=None,wsse=security )
client.set_options(wsse=security)
client.factory.separator('/')

# Queue the report
reportDescription = {}
reportDescription['reportSuiteID'] = 'atlanticprod'
reportDescription['dateFrom'] = '2011-01-01'
reportDescription['dateTo'] = '2011-01-02'
#reportDescription[('metrics','id')] = 'visits'
#reportDescription[('elements','id')] = 'page'
#reportDescription[('elements','startswith')] = 1
#reportDescription[('top','id')] = 60

#method = getattr(client.service, 'Company.GetTokenCount')
#result = method()

method = getattr(client.service, 'Report.QueueRanked')
result = method(reportDescription)

#result = client.service.ReportQueueRanked(reportDescription)

# Check make sure it got called

#put the ID in an array 
reportID = {"reportID" : result["reportID"]}
# Get the Report
report = client.service.ReportGetReport(reportID)

