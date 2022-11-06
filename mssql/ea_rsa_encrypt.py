"""
	signed loginnme
"""
import base64
import os

import rsa


class ea_encrypt_ad_login:

	def generateKeys():
		(publicKey, privateKey) = rsa.newkeys(512)
		with open(os.path.join(os.getcwd(), 'keys/publicKey.pem'), 'wb') as p:
			p.write(publicKey.save_pkcs1('PEM'))
		with open('keys/privateKey.pem', 'wb') as p:
			p.write(privateKey.save_pkcs1('PEM'))

	def loadKeys():
		with open('keys/publicKey.pem', 'rb') as p:
			publicKey = rsa.PublicKey.load_pkcs1(p.read())
		with open('keys/privateKey.pem', 'rb') as p:
			privateKey = rsa.PrivateKey.load_pkcs1(p.read())
		return privateKey, publicKey

	def generate_keys():
		# RSA modulus length must be a multiple of 256 and >= 1024
		(publicKey, privateKey) = rsa.newkeys(512)
		return   (publicKey, privateKey)

	def encrypt_message(a_message , publicKey):
		print(a_message)
		return rsa.encrypt(a_message.encode(), publicKey)
		# encrypted_msg =rsa.encrypt(a_message.encode(), publicKey)
		# encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
		# return encrypted_msg

	def decrypt_message(encoded_encrypted_msg, privateKey):
		decMessage = rsa.decrypt(encoded_encrypted_msg, privateKey).decode()
		print(decMessage)
		try:
			return rsa.decrypt(encoded_encrypted_msg, privateKey)
		except Exception:
			print(Exception)
			return False

		# decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
		# decoded_decrypted_msg = rsa.decrypt(encoded_encrypted_msg, privateKey).decode()
		# return decoded_decrypted_msg

	########## BEGIN ##########
	#
	# a_message = "The quick brown fox jumped over the lazy dog"
	# (publicKey, privateKey) = generate_keys()
	# encrypted_msg = encrypt_message(a_message , publicKey)
	# decrypted_msg = decrypt_message(encrypted_msg, privateKey)
	#
	# # print( "%s - (%d)" % (privatekey.exportKey() , len(privatekey.exportKey())))
	# # print( "%s - (%d)" % (publickey.exportKey() , len(publickey.exportKey())))
	# print(" Original content: %s - (%d)" % (a_message, len(a_message)))
	# print( "Encrypted message: %s - (%d)" % (encrypted_msg, len(str(encrypted_msg))))
	# print( "Decrypted message: %s - (%d)" % (decrypted_msg, len(str(decrypted_msg))))
# ea_encrypt_ad_login.generateKeys()