'''
'''
if __name__ == '__main__':
    n = int(input())
    avg = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        avg = avg + i

    print('%3.2f'%(avg/len(student_marks[query_name])))
    