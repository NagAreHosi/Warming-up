#logic-1
#1
def cigar_party(cigars, is_weekend):
    if is_weekend == True and cigars >= 40:
        return True
    else:
        if cigars >= 40 and cigars <= 60:
            return True
    return False

#2
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    else:
        if you < 8 and date < 8:
            return 1
        else:
            return 2

#3

def squirrel_play(temp, is_summer):
    if is_summer == True:
        if temp >= 60 and temp <= 100:
            return True
        else:
            return False
    else:
        if temp >= 60 and temp <= 90:
            return True
        else:
            return False

#4
def caught_speeding(speed, is_brithday):
    if is_brithday:
        if speed <= 65:
            return 0
        if 65 < speed <= 85:
            return 1
        if speed > 85:
            return 2
    else:
        if speed <= 60:
            return 0
        if 60 < speed <= 80:
            return 1
        if speed > 80:
            return 2


#5

def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    return a + b

#6

def alarm_clock(day, vacation):
    if vacation:
        if 1 <= day <= 5:
            return '10:00'
        else:
            return 'off'
    else:
        if 1 <= day <= 5:
            return '7:00'
        else:
            return '10:00'

#7
def love6(a, b):
    if a == 6 or b == 6:
        return True
    if a + b == 6 or abs(a - b) == 6:
        return True
    return False

#8

def in1to10(n, outside_mode):
    if outside_mode:
        if n <= 1 or n >= 10:
            return True
        else:
            return False
    else:
        if 1 <= n <= 10:
            return True
    return False

#9
def near_ten(num):
    a = num % 10
    if 0 <= a <= 2 or  8 <= a <= 9:
        return True
    return False

#logic-2
#1
def make_bricks(small, big, goal):
    sum = 0
    if small + 5 * big < goal:
        return False
    else:
        for i in range(big):
           sum = sum + 5
           if sum == goal:
               return True
           if sum < goal and abs(goal - sum) < 5:
               if small >= abs(goal - sum):
                   return True
               else:
                   return False
           else:
               continue
    if sum + small >= goal:
        return True
    return False

#2

def lone_sum(a, b, c):
    if a == b:
        if b == c:
            return 0
        else:
            return c
    else:
        if a == c:
            return b
        else:
            if b == c:
                return a
            else:
                return b + c + a

#3

def no_teen_sum(a, b, c):
    d = [a, b, c]
    sum = 0
    for i in d:
        if 13 <= i <= 14 or 17 <= i <= 19:
            sum = sum + 0
        else:
            sum = sum + i
    return sum

#4
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 >= 5:
        return (num / 10) * 10 + 10
    else:
        return (num / 10) * 10

#5
def close_far(a, b, c):
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            return True
        else:
            return  False
    else:
        if abs(a - c) <= 1 and abs(b - c) >= 2:
            return True
        else:
            return False

#6

def make_chocolate(small, big, goal):
    #刚好big可以整数给goal
    if goal / 5 <= big and goal % 5 == 0:
        return 0
    #big*5大于goal：
    if goal < big * 5:
        if small >= goal % 5:
            return goal % 5
        else:
            return -1
    #big * 5小于goal：
    if small >= goal - big * 5:
        return goal - big * 5
    else:
        return -1
