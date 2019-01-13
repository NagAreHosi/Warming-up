#Warming-up1
#1
def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False
#2
def monkey_trouble(a_smile, b_smile):
    if(a_smile == b_smile):
        return True
    else:
        return False
#3
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b
#4
def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n
#5
def parrot_trouble(talking, hour):
    if talking == True:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False
#6
def makes10(a, b):
    if (a == 10 or b == 10) or a + b == 10:
        return True
    return False
#7
def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    return False
#8
def pos_neg(a, b, negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    elif negative == False:
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            return True
        else:
            return False
#9
def not_string(str):
    if str.__contains__('not'):
        return str
    else:
        return 'not ' + str
#10
def missing_char(str, n):
    return str[:n] + str[n+1:]

#11
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]

#12
def front3(str):
     return str[:3] + str[:3] + str[:3]

#Warming-up2
#1
def string_times(str, n):
     return n * str

#2
def front_times(str, n):
     return n * str[:3]

#3
def string_bits(str):
    return str[::2]

#4
def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result

#5
def last2(str):
    laststr2 = str[-2:]
    l = len(str) - 2
    count = 0
    for i in range(l):
        str2 = str[i:i+2]
        if laststr2 == str2:
            count += 1
    return count

#6
def array_count9(nums):
    ft = filter(lambda x: x == 9, nums)
    return len(ft)

#7
def array_front9(nums):
    for i in range(len(nums)):
        if i == 4:
            break
        if nums[i] == 9:
            return True
    return False

#8
def array123(nums):
    L1 = [1, 2, 3]
    for i in range(len(nums)-2):
        L2 = nums[i:i+3]
        if L1 == L2:
            return True
    return False

#9
def string_match(a, b):
    L1 = []
    L2 = []
    n = 0
    for i in range(len(a)-1):
        L1.append(a[i:i+2])
        L2.append(b[i:i+2])
    r = min(len(L1), len(L2))
    for i in range(r):
        if L1[i] == L2[i]:
            n += 1
    return n

