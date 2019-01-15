# -*- coding: utf-8 -*-
#1
def cigar_party(cigars, is_weekend):
  if cigars<40 :
    return False
  else:
    return 40<=cigars<=60 or is_weekend 

#2
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>8 or date > 8:
    return 2
  else:
    return 1

#3
def squirrel_play(temp, is_summer):
  return 60<=temp<=100 if is_summer else 60<=temp<=90

#4
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed<=65:
      return 0
    elif speed<=85:
      return 1
    else:
      return 2
  else:
    if speed<=60:
      return 0
    elif speed<=80:
      return 1
    else:
      return 2

#5
def sorta_sum(a, b):
  return 20 if 10<=a+b<=20 else a+b

#6
def alarm_clock(day, vacation):
  if vacation and (day==0 or day==6):
    return 'off'
  elif vacation and 1<=day<=5:
    return '10:00'
  else:
    return '7:00' if 1<=day<=5 else '10:00'

#7
def love6(a, b):
  return (a is 6 or b is 6) or (a+b is 6) or (abs(a-b) is 6) 

#8
def in1to10(n, outside_mode):
  if outside_mode:
    return (n<=1)or(n>=10)
  else:
    return 1<=n<=10

#9
def near_ten(num):
  return num%10<=2 or 10-num%10<=2

#1
def make_bricks(small, big, goal):
  n=goal//5
  goal = goal-n*5 if n<big else goal-big*5
  return goal<=small
#2
def lone_sum(a, b, c):
  sum=a+b+c
  if a==b or a==c:
    sum-=a
  if b==a or b==c:
    sum-=b
  if c==a or c==b:
    sum-=c
  return sum

#3
def lucky_sum(a, b, c):
  n=a+b+c
  if a is 13:
    return n-a-b-c
  elif b is 13:
    return n-b-c
  elif c is 13:
    return n-c
  return n

#4
def no_teen_sum(a, b, c):
  n = a+b+c
  if (a in range(13,15)) or (a in range(17,20)):
     n-=a
  if (b in range(13,15)) or (b in range(17,20)):
     n-=b
  if (c in range(13,15)) or (c in range(17,20)):
     n-=c
  return n

#5
def round_sum(a, b, c):
  a_last = a%10
  b_last = b%10
  c_last = c%10
  a=a+10-a_last if a_last>=5 else a-a_last
  b=b+10-b_last if b_last>=5 else b-b_last
  c=c+10-c_last if c_last>=5 else c-c_last
  return a+b+c

#6
def close_far(a, b, c):
  return (abs(b-a)<=1 or abs(c-a)<=1)and((abs(c-a)>=2 and abs(c-b)>=2)or(abs(b-a)>=2 and abs(b-c)>=2))

#7
def make_chocolate(small, big, goal):
  n=goal//5
  goal=goal-n*5 if n<=big else goal-big*5
  return goal if goal<=small else -1
