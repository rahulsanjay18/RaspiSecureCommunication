# This file is the RSA encryption algorithm

# RSA Parameters Used
# [p, q, n, z , e, d] = [17, 19, 323, 288, 17, 17]

def RSA_encrypt_Alg(msg):

	ptxt = msg # plain text
	ctxt = []  # cipher text

	for i in range(0, len(ptxt)):
	    	num = ord(ptxt[i]) # Uses ASCII library to map text to ints
		rsa_val = ((num ** 17) % 323)
		ctxt.append(str(rsa_val)) # RSA encryption implementation

	return ctxt

# Note that this returns a list of strings as opposed to a single string because of the limitations with ASCII and our RSA algorithm
# Can use unicode instead since that offers a larger library so we aren't restricted by 256 mappings



