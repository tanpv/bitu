"""
	requirement
		
		main function
		- create private key
		- get public point
		- get public key in compressed format
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

print(len(os.urandom(32)))