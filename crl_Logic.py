#1
def cigar_party(cigars, is_weekend):
  if is_weekend == True and cigars >= 40:
    return True
  elif is_weekend == False and cigars >= 40 and cigars <=60:
    return True
  return False
#2
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  return 1
#3
def squirrel_play(temp, is_summer):
  return (not is_summer and (temp>=60 and temp<=90))\
  or (is_summer and (temp>=60 and temp<=100))
#4
def caught_speeding(speed, is_birthday):
  if (not is_birthday and speed <= 60) or (is_birthday and speed <= 65):
      return 0
  elif (not is_birthday and speed >= 81) or (is_birthday and speed >= 86):
      return 2
  return 1
#5
def sorta_sum(a, b):
  if a+b>=10 and a+b <= 19:
    return 20
  else:
    return a+b
#6
def alarm_clock(day, vacation):
  weekaday = [1,2,3,4,5]
  if (vacation and day in weekaday) or (not vacation and (day == 0 or day == 6)):
    return "10:00"
  elif vacation and (day == 0 or day == 6):
    return "off"
  return "7:00"
#7
def love6(a, b):
  return a==6 or b==6 or a+b==6 or abs(a-b)==6
#8
def in1to10(n, outside_mode):
  if n in range(2,10) and outside_mode:
    return False
  elif n in range(1,11) or outside_mode:
    return True
  return False
#9
def near_ten(num):
  m = min(abs(10-num%10),abs(num%10))
  return m<=2


#1
def make_bricks(small, big, goal):
  if small == 0:
    return (goal % 5) <= big
  elif big == 0:
    return goal <= small
  else:
    return small >= (goal % 5) and small + 5*big >= goal
#2
def lone_sum(a, b, c):
  if a==b and a==c:
    return 0
  elif a==b:
    return c
  elif a==c:
    return b
  elif b==c:
    return a
  return a+b+c
#3
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  return a + b + c
#4
def no_teen_sum(a, b, c):
  l = [a, b, c]
  sum = 0
  for i in range(len(l)):
    if fix_teen(l[i]):
      sum += 0
    else:
      sum += l[i]
  return sum
  
def fix_teen(n):
  return (n >= 13 and n < 15) or (n > 16 and n <= 19)
#5
def round_sum(a, b, c):
  return num(a) + num(b) + num(c)

def num(n):
  if n % 10 >= 5:
    return (n // 10 + 1) * 10 
  return (n // 10 ) * 10 
#6
def close_far(a, b, c):
  return ((abs(a-b) <=1 and abs(a-c) >= 2) or (abs(a-c) <=1 and abs(a-b) >= 2))\
  and abs(b-c)>=2
#7
def make_chocolate(small, big, goal):
  if big * 5 >= goal and goal % 5 <= small:
    return goal % 5
  elif big * 5 <= goal and (goal - big * 5) <= small:
    return goal - 5 * big
  return -1

