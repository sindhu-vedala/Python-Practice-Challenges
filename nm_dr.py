# ##INCOMPLETE##

# from operator import itemgetter

# def person_lister(f):
#     def inner(people):
#         people.sort(key = itemgetter(2))
#     return inner

# @person_lister
# def name_format(*person):
#     print("In n_f: ", person)
#     print("Mr. " if person[3] == "M" else "Ms. ")
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print("Main after input: ",people)
#     # print(*name_format(people), sep='\n')
#     print(name_format(people))


# ms = "ABCDCDC"
# ss = "CDC"
# cnt = 0
# for i in range((len(ms)-len(ss))+1):
#     # print("For: ",ms[i:i+len(ss)])
#     cnt = cnt +(ms.count(ss,i,i+len(ss)))
# print(cnt)

def count_substring(string, sub_string):
    # count = 0
    string.count(sub_string)
    # for i in range((len(string)-len(sub_string))+1):
    #     print(string[i:i+len(sub_string)])
    #     print(sub_string)
    #     count = count + string.count(sub_string,i,len(sub_string))
    #     print(count)
    return string.count(sub_string)

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
