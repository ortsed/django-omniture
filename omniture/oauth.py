import uuid
import hashlib
import base64
from datetime import datetime, timedelta

class OAuth():
	def __init__(self, username, secret):
		self.username = username
		self.secret = secret
		self.nonce = hashlib.md5(str(uuid.uuid1())).hexdigest()
		
		self.created = (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
	
		self.digest = base64.b64encode(hashlib.sha1(self.nonce + self.created + self.secret).digest())

		self.header =  {
			'X-WSSE': 'UsernameToken Username="' + self.username + '", PasswordDigest="' + self.digest + '", Nonce="' + base64.b64encode(self.nonce) + '", Created="' + self.created
		}