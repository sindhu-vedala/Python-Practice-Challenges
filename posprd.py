'''
rethink logic!
'''
arr = [ 4, 1, -1, -2, 4]

prd = 1
maxlen = mxlen = 0
for i in arr:
    print("for i: ", i)
    if i*prd > 0:
        print("if")
        prd = i*prd
        maxlen = maxlen + 1
        if (maxlen > mxlen):
            mxlen = maxlen 
            prod = prd
        print("prd: {}, maxlen = {}".format(prd,maxlen))
    elif prod * i > 0:
        prd = prod = prod*i 
        maxlen = mxlen = mxlen + 1
    else:   
        prd = 1
        maxlen = 0
        

print(mxlen)