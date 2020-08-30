# azerdii →  s = 'azerdii'
# 5       →  k = 5

# erdii
#!!!needs optimization!!!

vcount = 0
vstr = "Not found!"
s = "azerdii"
k = 5
j=0
# while j+k < len(s):
#     count = 0
#     for i in s[j:j+k]:
#         if i in ['a','e','i','o','u']:
#             count = count + 1
#     if count > vcount:
#         vcount = count
#         vstr = s[j:j+k]
#     j = j+1
count = 0
for i in s[::]:
    if i in "aeiou":
        count = count + 1



print("VSTR: ",vstr)
