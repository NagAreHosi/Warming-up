# -*- coding: utf-8 -*-
#1
def first_last6(nums):
  return nums[len(nums)-1] == 6 or nums[0] == 6
    
#2
def same_first_last(nums):
  if len(nums)==0:
    return False
  if nums[0]==nums[len(nums)-1]:
    return True
  else :
    return False

#3
def make_pi():
  pi=3.14
  return [int(pi),int(pi*10)%10,(int(pi*100)%100)%10]

#4
def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  else:
    return False

#5
def sum3(nums):
  return nums[0]+nums[1]+nums[2]

#6
def rotate_left3(nums):
  list = nums[1:]
  list.append(nums[0])
  return list

#7
def reverse3(nums):
  nums.reverse()
  return nums

#8
def max_end3(nums):
  ind = 0 if nums[0]>nums[-1] else nums.index(nums[-1])
  return [nums[ind],nums[ind],nums[ind]]

#9
def sum2(nums):
  if len(nums)==0:
    return 0
  else:
    return nums[0] if len(nums)==1 else nums[0]+nums[1]

#10
def middle_way(a, b):
  return [a[1],b[1]]

#11
def make_ends(nums):
  return [nums[0],nums[-1]]

#12
def has23(nums):
  return True if 2 in nums or 3 in nums else False
