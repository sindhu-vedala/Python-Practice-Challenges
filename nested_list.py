if __name__ == '__main__':
    listt = [[input(), float(input())] for _ in range(int(input()))] 
    print(listt)
    print("===============================================")
    max2 = sorted(list(set([score for name, score in listt])))[1]
    print(max2)
    print("===============================================")
    print('\n'.join([name for name,score in sorted(listt) if score == max2]))
    print("===============================================")
    print(sorted(list([score for name, score in listt])))
 