n = 9
ar = [10, 10, 50, 20, 30, 20, 50]
dct = {}
count = 0
for i in ar:
    if str(i) in dct.keys():
        dct[str(i)] = dct[str(i)] + 1
    else:
        dct[str(i)] = 1
for i in dct.values():
   count = count + int(i/2)
