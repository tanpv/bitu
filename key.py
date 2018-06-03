"""
	requirement
		
		main function
		- create private key
		- get public point
		- get public key in compressed format
		- get public key in uncompressed format
		- get address from public key
		
		support wif format
		- import key from wif format
		- export key to wif format
		- from WIF to pure key
		
		support hex format
		- import key from hex format
		- export key to hex format

		support integer format
		- import key from integer number
		- export key to integer

		support pem format
		- import key from pem
		- export key to pem

		support der format
		- import key from der
		- export key to der
"""

import os
import binascii


class Key():

	"""
		support 2 case:
			- if user specify private_key --> create key with this private key
			- if user not specify private_key --> auto create a random 32 bytes number for private key
	"""
	def __init__(self, private_key=None):
		if private_key == None:
			self.private_key = os.urandom(32)
			# convert from byte stream to readable format
			self.private_key_readable = binascii.hexlify(self.private_key)
		else:
			self.private_key_readable = private_key
			self.private_key = binascii.unhexlify(private_key.encode('ascii'))

