# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:03:33 2019

@author: crl
"""

#array_front9
def array_front9(nums):
  if len(nums)<=4:
    for i in range(len(nums)):
      if nums[i] == 9:
        return True
    return False
  else:
    for i in range(4):
      if nums[i] == 9:
        return True
    return False

#array123 
def array123(nums):
  if len(nums)<3:
    return False
  else:
    for i in range(len(nums)-2):
      if nums[i:i+3] == [1,2,3]:
        return True
    return False


#string_match 
def string_match(a, b):
  shorter = min(len(a),len(b))
  count = 0
  for i in range(shorter-1):
    a1 = a[i:i+2]
    b1 = b[i:i+2]
    if a1 == b1:
      count += 1
  return count
