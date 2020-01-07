# import numpy as np

# if __name__ == '__main__':
#     # n = int(input())
#     # arr = map(int, input().split())
#     # arr = list(arr)
    #  arr = [2, 3, 6, 6, 5]
    #  n = len(arr)
#     # print(arr)
#     # # Using builtin 
#     # # 1
#     # arr = sorted(arr)
#     # print(arr[n-2])
#     # # 2
#     # arr.remove(max(arr))
#     # print(max(arr))
#     # print(arr)
#     # wihtout using built in methods
#     # # 1
#     # arr = [3, 1]
#     # n = len(arr)

#     maxx = arr[0]
#     for i in arr:
#         if i>maxx:
#             maxx = i
#     maxx2 = arr[n-1]
#     for i in arr:
#         if i>maxx2 and i<maxx:
            
#             maxx2 = i
        
#     # print('Max: ', maxx)
#     print('2nd max: ', maxx2)
#     for i in arr:
#         arr.remove(i) if i == maxx

if __name__ == '__main__':
    arr = [57 ,57, -57, 57]
    n = len(arr)
    print("n : ",n)
    arr = list(arr)
    maxx = max(arr)
    print("0Max: ",maxx)
    i = n-1
    while i>=0:
        print(i)
        if arr[i] == maxx:
            arr.remove(arr[i])
            i = len(arr)-1
        else:
            i = i-1
    print("Array after removal of max",arr)
    print("02nd max",max(arr))
  