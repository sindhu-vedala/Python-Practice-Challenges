import re
REGEX = r'^[789][0-9]{9}$'

N = int(input())
for i in range(N):
    n = (input())
    print("YES") if re.match(REGEX, n) else print("NO")