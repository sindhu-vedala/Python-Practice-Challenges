s = list("51Pa*0Lp*0e")
# dec = "aP1pL5e"
dec = []
while s:
    strr = s.pop()
    if strr == "0":
        dec.append(s[0])
        s.remove(s[0])
    elif strr == "*":
        i = (s.pop())
        j = (s.pop())
        dec.append(j)
        dec.append(i)

    else:
        dec.append(strr)
dec = "".join(dec[::-1])
print("DEC: ",dec)
    

    

