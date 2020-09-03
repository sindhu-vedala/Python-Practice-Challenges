c = [0,0,1,0,0,1,0]
mini = 0
i =0
while(i<len(c)-1):
    if c[i] == 0:
        if i+2<len(c) and c[i+2] == 0:
            mini = mini+1
            i = i+2
        elif c[i+1] == 0:
            mini = mini+1
            i = i+1
    else:
             i = i+1

print(mini)
