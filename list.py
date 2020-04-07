"""

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

"""
# def switch(cmd):
#     if len(cmd) == 1:
#         return cmd[0]
#     elif len(cmd) == 2:
#         return cmd[0](cmd[1])
#     elif len(cmd) == 3:
#         return cmd[0](cmd[1],cmd[2])

if __name__ == '__main__':
    N = int(input())
    cmds = [ input() for i in range(0,N)]
    # print(cmds)
    list1 = []
    for i in range(0,N):
        cmd = cmds[i].split()
        # print(cmd)
        # print(cmd[0])
        # print(switch(cmd))
        if cmd[0] == "print":
            print(list1)
        elif cmd[0] == "sort":
            list1.sort()
        elif cmd[0] == "pop":
            list1.pop() 
        elif cmd[0] == "reverse":
            list1.reverse()
        elif cmd[0] == "remove":
            list1.remove(int(cmd[1]))
        elif cmd[0] == "append":
            list1.append(int(cmd[1]))
        elif cmd[0] == "insert":
            list1.insert(int(cmd[1]),int(cmd[2]))
        else:
            print("Invalid command")
    
# N = int(input())
# l = []
# for _ in range(N):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print(l)
