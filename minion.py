def subStrScore(string, substr):
    count = 0
    for i in range(len(string)):
        count = count + string[i:i+len(substr)].count(substr)
    print("{}: {}".format(substr, count))
    return count

        
string = 'BANANA'
sub_str = set([])
scoreA = 0
scoreB = 0

vowel = 'a', 'e', 'i', 'o', 'u'
for i in range(len(string)):
    for j in range(i+1):
        if string[j:i+1] is not '':
            sub_str.add(string[j:i+1]) 


for s in sub_str:
        if (s.lower()).startswith(vowel):
            scoreA = scoreA + subStrScore(string, s)
        else:
            scoreB = scoreB + subStrScore(string, s)
print("No of ss", len(sub_str))
print(sub_str)
print(scoreA, scoreB)