msg="quiero que eco"
if 'eco' in msg:
    msg=msg.split()
    poss=msg.index('eco')
    msg=msg[poss+1:]
    print(msg)
    msg=' '.join(msg)
    print(msg)