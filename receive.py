import socket
import sys
sys.path.insert(0, './CC')
sys.path.insert(0, './RSA')
import CC_decrypt
import RSA_decrypt

UDP_IP = "192.168.14.1"
UDP_Port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_Port))

alg_used = 'RSA' # decryption algorithm used (default is RSA)

while True:
    data, addr = sock.recvfrom(1024)
    decrypt_alg, addr = sock.recvfrom(1024)
    if decrypt_alg == 'CC':
	shift, addr = sock.recvfrom(1024)
        ptxt = CC_decrypt.CC_decrypt_Alg(data, int(shift)) # CC decryption aglorithm using the shift
	alg_used = 'Caesar Cipher'

	print "received message: ", data
	print "decrypted message: ", ptxt
	print "received shift: ", shift
	print alg_used
    else:
	data = data.split(' ')
	ptxt = RSA_decrypt.RSA_decrypt_Alg(data) # RSA decryption algorithm

	print "received message: ", data
	print "decrypted message: ", ptxt
	print alg_used


