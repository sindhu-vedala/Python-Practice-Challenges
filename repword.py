from collections import Counter
# import os

def firstRepeatedWord(s):
    # Write your code here
    print(s)
    s.replace(';',' ')
    print(s)
    word_list = s.split(' ')
    repeated_word = set()
    for word in word_list:
        print("For: ",word)
        if word in repeated_word:
            print("For, if ",word)
            return word
        else:
            print("For elss: ", word)
            repeated_word.add(word)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = firstRepeatedWord(s)

    # fptr.write(result + '\n')

    # fptr.close()
