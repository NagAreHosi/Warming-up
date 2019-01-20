# logic-1
# 1
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (40 <= cigars <= 60 or is_weekend)

# 2
def date_fashion(you, date):
    if you <=2 and date <= 2:
        return 0
    elif you >= 8 and date >= 8:
        return 2
    else:
        return 1

# 3
def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90

# 4
def caught_speeding(speed, is_birthday):
    m = 0
    if is_birthday:
        m += 5
    if speed <= 60 + m:
        return 0
    elif speed > 80 + m:
        return 2
    else:
        return 1

# 5
def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    return  a + b

# 6
def alarm_clock(day, vacation):
    if vacation:
        if 0 < day < 6:
            return '10:00'
        return 'off'
    else:
        if 0 < day < 6:
            return '7:00'
        return '10:00'

# 7
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

# 8
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

# 9
def near_ten(num):
    return (num + 2) % 10 <= 4

# logic-2
# 1
def make_bricks(small, big, goal):
  if small == 0:
    return goal % 5 == 0
  elif big == 0:
    return goal <= small
  else:
    return (goal - min((goal // 5), big) * 5) <= small

# 2
def lone_sum(a, b, c):
    sum = 0
    t = (a, b, c)
    t1 = filter(lambda x: t.count(x) <= 1, t)
    for i in t1:
        sum += i
    return sum

# 3
def lucky_sum(a, b, c):
    sum = 0
    t = (a, b, c)
    for i in t:
        if i == 13:
            break
        sum += i
    return  sum

# 4
def no_teen_sum(a, b, c):
    sum = 0
    t = (a, b, c)
    for i in t:
        if i in range(13, 20) and i not in (15, 16):
            continue
        sum += i
    return sum

# 5
def round_sum(a, b, c):
    sum = 0
    for i in (a, b, c):
        sum += ((i + 5) // 10) * 10
    return sum

# 6
def close_far(a, b, c):
    return abs(b - c <= 2) and ((abs(a - b) >= 2 and abs(a - c) <= 1) or (abs(a - c) >= 2 and abs(a - b) <= 1))

# 7
def make_chocolate(small, big, goal):
    if ((goal // 5) - big) >= 0: # big少了
        goal -= (big * 5)
    elif ((goal // 5) - big) < 0: #big多了
        goal -= ((goal // 5) * 5)
        print(2)
    if goal > small:
        return -1
    elif goal <= small:
        return small
