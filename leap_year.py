def is_leap(year):
    leap = False
    # if year%400 == 0 or year%4 == 0:
    #     leap = True 
    # if year%100 == 0 and year%400 != 0:
    #     leap = False
    leap = True if year%400 == 0 or year%4 == 0 else False if year%100 == 0 and year%400 != 0 else False
    return leap

year = int(input())
print(is_leap(year))