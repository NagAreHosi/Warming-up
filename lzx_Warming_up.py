# -*- coding: utf-8 -*-
#Warming_up2
#5
def last2(str):
  s=str[len(str)-2:]
  count=0
  if len(str)<2:
    return 0
  for i in range(len(str)-2):
    if str[i:i+2]==s:
      count+=1
  return count
#6
def array_count9(nums):
  return nums.count(9)
#7
def array_front9(nums):
  if 9 in nums[:4]:
    return True
  else:
    return False
#8
def array123(nums):
  if (1 in nums) and (2 in nums) and (3 in nums) :
    return True
  else:
    return False
#9
def string_match(a, b):
  s=''
  count=0
  for i in range(len(b)-1) if range(len(a))>range(len(b)) else range(len(a)-1):
    if a[i:i+2]==b[i:i+2]:
      count+=1
  return count
