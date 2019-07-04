def CC_encrypt_Alg(msg, alpha):
    ctxt = [] # cipher text
    msg = list(msg) # converts to list for iterations
    outmsg = '' # initialization
    alpha = (alpha % 256) # implements a periodic shift w.r.t. ASCII

    for c in msg:
        ctxt.append(ord(c) + alpha) # converts to int via ASCII map and adds a shift

    for i in range(len(ctxt)):
	outmsg = outmsg + (chr(ctxt[i])) # converts cipher text to a string

    return outmsg
