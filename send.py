import socket
import sys
sys.path.insert(0, "../CC")
sys.path.insert(0, "../RSA")
import CC_encrypt
import RSA_encrypt

UDP_IP = "192.168.14.1"
UDP_Port = 5005
message = "Dan is a weenie"
shift = '69'
decrypt_alg = 'CC'
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if(decrypt_alg == 'CC'):
	res = CC_encrypt.CC_encrypt_Alg(message, int(shift))
	print "UDP Target IP: ", UDP_IP
	print "UDP Target Port: ", UDP_Port
	print "Message: ", res
	print "Shift: ", shift
	sender.sendto(res, (UDP_IP, UDP_Port))
	sender.sendto(decrypt_alg, (UDP_IP, UDP_Port))
	sender.sendto(shift, (UDP_IP, UDP_Port))
elif(decrypt_alg == 'RSA'):
	res = RSA_encrypt.RSA_encrypt_Alg(message)
	resStr = ''
	for s in res:
		resStr += s + ' '
	resStr = resStr[0:len(resStr) - 1]
	print "UDP Targer IP: ", UDP_IP
	print "UDP Target Port", UDP_Port
	print "Message: ", res
	sender.sendto(resStr, (UDP_IP, UDP_Port))
	sender.sendto(decrypt_alg, (UDP_IP, UDP_Port))
