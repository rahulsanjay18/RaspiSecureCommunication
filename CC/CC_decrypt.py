def CC_decrypt_Alg(msg, alpha):
    ptxt = '' # initialization
    alpha = (alpha % 256) # implements periodic shift w.r.t. ASCII

    for i in range(len(msg)):
        ptxt += chr(ord(msg[i]) - alpha) # reverses caeser cipher

    return ptxt

