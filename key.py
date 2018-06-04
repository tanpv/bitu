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
import ecdsa
import hashlib


class Key(object):

	def __init__(self, private_key=None):
		if private_key == None:
			# create a 32 bytes random number
			self.private_key = os.urandom(32)
			# convert from byte stream to readable format
			self.private_key_readable = binascii.hexlify(self.private_key)
		else:
			self.private_key_readable = private_key
			self.private_key = binascii.unhexlify(private_key.encode('ascii'))

		self.sk = ecdsa.SigningKey.from_string(self.private_key, curve=ecdsa.SECP256k1)
		self.vk = self.sk.verifying_key
		self.public_key = b'04' + binascii.hexlify(self.vk.to_string())

		ripemd160 = hashlib.new('ripemd160')
		ripemd160.update(hashlib.sha256(binascii.unhexlify(self.public_key)).digest())
		
		self.hashed_public_key = b'00' + binascii.hexlify(ripemd160.digest())
		self.check_sum = self.calculate_check_sum(self.hashed_public_key)

	

	def calculate_check_sum(self, hashed_public_key):
		return binascii.hexlify(self.double_sha256(binascii.unhexlify(hashed_public_key))[:4])

	def double_sha256(self, message):
		return hashlib.sha256(hashlib.sha256(message).digest()).digest()



k = Key()
print(k.public_key)
print(k.hashed_public_key)

