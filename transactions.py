"""
	requirement
		- create transaction
		- create transaction with change address support
		- create transaction with fee support
		- create transaction with unspent consolidation support
		- transfer funds
		- create transaction frorm unspent
		- create transaction with message
		- create offline transaction
"""

# bob

# b'92ASXhnGAbAi9FYP3k8Ru6jLKAY2VyxYf3vKzLJ4bPfGA6B5eFm'
# b'mg8Y9jaVt6HJpy4pvKFJ1z3KZWbaR3BDFf'
# amount = 110000000
# transaction_id = a4c13a5d6b1a50cb12af7452daeb758f6c0972c3fabaa7a242125b958e387511
# transaction_index = 0
# "outputs": [
#        {
#          "value": 110000000,
#          "script": "76a91406bad2197f73f2af9522e770e48d8dc26173565688ac",
#          "addresses": [
#            "mg8Y9jaVt6HJpy4pvKFJ1z3KZWbaR3BDFf"
#          ],
#          "script_type": "pay-to-pubkey-hash"
#        }


# alice
# b'93TGfBvCX8oW9e7UQLiXAmb2QHLXNsEz6bBVcwhAU4LtjY1vFom'
# b'n268kLx7MuuoqbuX4VRDZvvGhgVuFJvChP'


# sara
# b'92C97ce7tUW54ev7Zsu5wd2DvF8w5wf6vpoGmvdx9R3ULtTHXWM'
# b'mgfxna24EgTji21eXuYegAqju3xuLBcuNK'


import struct


class Tx(object):
 	def __init__(self):
 		version = struct.pack('<L', 1)
 		
 		tx_in_count = struct.pack('<L', 1)
 		tx_in = ""

 		tx_out_count = struct.pack('<L', 1)
 		tx_out = ""

 		lock_time = struct.pack('<L', 0)

 		tx_out_value = struct.pack('<Q', 100)

 		print(version)


tx = Tx()




