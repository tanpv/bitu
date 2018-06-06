"""
	requirement
	
		main function
		- support mainnet and testnet
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


"""
	- private key to address process
	  https://en.bitcoin.it/wiki/Protocol_documentation#Addresses
	- 
"""

import os
import binascii
import ecdsa
import hashlib
import base58

def double_sha256(m):
	return hashlib.sha256(hashlib.sha256(m).digest()).digest()

class Key(object):

	def __init__(self, private_key=None, testnet=True):

		if private_key == None:
			private_key_byte= os.urandom(32)
			self.private_key = self.convert_private_key_from_byte_to_wif_format(private_key_byte, testnet)
		else:
			self.private_key = private_key
			private_key_byte = binascii.unhexlify(private_key.encode('ascii'))

		self.address = self.from_private_key_to_address(private_key_byte, testnet)


	def from_private_key_to_address(self, private_key_byte, testnet):

		sk = ecdsa.SigningKey.from_string(private_key_byte, curve=ecdsa.SECP256k1)
		vk = sk.verifying_key
		public_key = b'04' + binascii.hexlify(vk.to_string())

		public_key_sha256 = hashlib.sha256(binascii.unhexlify(public_key)).digest()
		ripemd160 = hashlib.new('ripemd160')
		ripemd160.update(public_key_sha256)
		public_key_sha256_ripemd160 = ripemd160.digest()
		
		if testnet:
			prefix = b'6F'
		else:
			prefix = b'00'

		public_key_hashed = prefix + binascii.hexlify(public_key_sha256_ripemd160)
		public_key_hashed_in_byte = binascii.unhexlify(public_key_hashed)
		check_sum = binascii.hexlify(double_sha256(public_key_hashed_in_byte)[:4])
		address = base58.b58encode( binascii.unhexlify(public_key_hashed + check_sum))

		return address



	def convert_private_key_from_byte_to_wif_format(self, private_key_byte, testnet):

		private_key_hex = binascii.hexlify(private_key_byte)

		if testnet:
			prefix = b'ef'
		else:
			prefix = b'80'
		
		binary_prefix_key = binascii.unhexlify(prefix + private_key_hex)
		checksum = binascii.hexlify(double_sha256(binary_prefix_key)[:4])
		private_key = base58.b58encode(binascii.unhexlify(prefix + private_key_hex + checksum))

		return private_key


k1 = Key()
print(k1.private_key)
print(k1.address)

k2 = Key(testnet=False)
print(k2.private_key)
print(k2.address)