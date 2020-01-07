if __name__ == "__main__":
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    # X=1
    # Y=1
    # Z=1
    # N=2

    output_list = []

    # for i in range(X+1):
    #     print('Iteration i - ',i)
    #     for j in range(Y+1):
    #         print('Iteration j - ',j)
    #         for k in range(Z+1):
    #             print('Iteration k - ',k)
    #             if (i+j+k) != N:
    #                 print('Inside if - i+j+k = ',(i+j+k))
    #                 output_list.append([i,j,k])
    #                 print(output_list)

    # output_list.sort()
    # print("================================")
    # print(output_list)
    output_list = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if ((i+j+k) != N)]
    output_list.sort()
    print(output_list)
    