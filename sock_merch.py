n = 9
ar = [10, 10, 50, 20, 30, 20, 50]
dct = {}
count = 0
for i in ar:
    print("DICT KEYS: ",dct.keys())
    if str(i) in dct.keys():
        print("True")
        dct[str(i)] = dct[str(i)] + 1
        print(dct)
    else:
        print("!")
        print(dct)
        dct[str(i)] = 1
print(dct)
for i in dct.values():
   count = count + int(i/2)
print(count)