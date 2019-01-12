#以下为warming-up1
#2
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

#3
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b

#4
def diff21(n):
    if n > 21:
        return 2 * abs(21 - n)
    else:
        return abs(21 - n)

#5
def parrot_trouble(talking, hour):
    if(talking == True):
        if(hour < 7 or hour > 20):
            return True
        else:
            return False
    else:
        return False

#6
def makes10(a, b):
    if a + b == 10 or a == 10 or b == 10:
        return True
    else:
        return  False

#7
def near_hundred(n):
    if(n > 89 and n < 111 or n > 189 and n < 211):
        return True
    else:
        return False

#8
def pos_neg(a, b, negatiove):
    if negatiove == True and a < 0 and b < 0:
        return True
    else:
        if (a > 0 and b < 0 or a < 0 and b > 0) and negatiove == False:
            return True
        else:
            return False

#9
def not_string(str):
    if len(str) < 3 or 'not' not in str[:3]
        return 'not ' + str
    else:
        return str

#10
def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back

#11
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]

#12
def front3(str):
    if(len(str) < 3):
        return str * 3
    return str[:3] * 3

#以下为warming-up2
#1
def string_times(str, n):
    return str * n

#2
def front_times(str, n):
    if(len(str) >= 3):
        return str[:3] * n
    return str * n

#3
def string_bits(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

#4
def string_splosion(str):
    result = ''
    for i in range(len(str) + 1):
        result = result + str[:i]
    return result

#5
def last2(str):
    count1 = 0
    if len(str) <= 2:
        return 0;
    else:
        sub_str = str[len(str) - 2:len(str)]
        # print(sub_str)
        for i in range(len(str)):
            if(i >= 2):
                if sub_str is str[i - 2:i]:
                    count1 = count1 + 1
    return count1

#6
def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

#7
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False

#8
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 3] == 3:
            return True
    return False

#9
def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub
            count = count + 1
    return count
