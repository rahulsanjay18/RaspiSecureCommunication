import RSA_encrypt
import RSA_decrypt

msg = '---Dan is a weenie 123---'

ctxt = RSA_encrypt.RSA_encrypt_Alg(msg)

print ctxt

ptxt = RSA_decrypt.RSA_decrypt_Alg(ctxt)

print ptxt
