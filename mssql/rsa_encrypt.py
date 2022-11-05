# Inspired from http://coding4streetcred.com/blog/post/Asymmetric-Encryption-Revisited-(in-PyCrypto)
# PyCrypto docs available at https://www.dlitz.net/software/pycrypto/api/2.6/

import base64

import rsa


def generate_keys():
	# RSA modulus length must be a multiple of 256 and >= 1024
	publicKey, privateKey = rsa.newkeys(512)
	return publicKey, privateKey

def encrypt_message(a_message , publicKey):
	encrypted_msg =rsa.encrypt(a_message, publicKey)
	encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
	return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privateKey):

	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	decoded_decrypted_msg = rsa.decrypt(base64.b64decode(decoded_encrypted_msg.encode()), privateKey)
	return decoded_decrypted_msg

########## BEGIN ##########

a_message = "The quick brown fox jumped over the lazy dog"
privatekey , publickey = generate_keys()
encrypted_msg = encrypt_message(a_message , publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

print( "%s - (%d)" % (privatekey.exportKey() , len(privatekey.exportKey())))
print( "%s - (%d)" % (publickey.exportKey() , len(publickey.exportKey())))
print(" Original content: %s - (%d)" % (a_message, len(a_message)))
print( "Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg)))
print( "Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg)))