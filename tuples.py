if __name__ == '__main__':
    # n = int(input())
    # n =2
    # integer_list = map(int, input().split())
    integer_list = [1, 2]
    tup_lst = tuple(integer_list)
    print(type(tup_lst))
    print(hash(tup_lst))