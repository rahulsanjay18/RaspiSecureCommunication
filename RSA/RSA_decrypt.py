# This decrypts an RSA msg
import RSA_encrypt

# decryption aglorithm accepts an input of integers
def RSA_decrypt_Alg(msg):
	ctxt = msg # cipher text
	ptxt = []  # plain text

	for i in range(0, len(ctxt)):
		num = int(ctxt[i]) # Use ASCII library to map text to ints
		rsa_val = (num ** 17) % 323
		ptxt.append(chr(rsa_val % 256)) # RSA decryption algorithm
	return ''.join(ptxt)

