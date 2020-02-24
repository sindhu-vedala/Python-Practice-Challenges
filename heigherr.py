def countStudents(height):
    # Write your code here
    n = len(height)
    acc_height = height.copy()
    height.sort()
    # print(height)
    # print(acc_height)
    count = 0
    for i in range(n):
        # print("Ier: ",i)
        # print(acc_height[i])
        # print(height[i])
        if acc_height[i] != height[i]:
            count = count + 1
    # print(count)
    

if __name__ == '__main__':
    countStudents([1,1,3,3,4,1])
    