#List-1
#1
def first_last6(nums):
  return nums[0]==6 or nums[-1] == 6
#2
def same_first_last(nums):
  if len(nums) == 0:
    return False
  return nums[0] == nums[-1]
#3
def make_pi():
  return [3,1,4]
#4
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
#5
def sum3(nums):
  return nums[0]+nums[1]+nums[2]
#6
def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]
#7
def reverse3(nums):
  return [nums[2],nums[1],nums[0]]
#8
def max_end3(nums):
  m = max(nums[0],nums[2])
  return [m,m,m]
#9
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums)==1:
    return nums[0]
  return nums[0]+nums[1]
#10
def middle_way(a, b):
  return [a[1],b[1]]
#11
def make_ends(nums):
  return [nums[0],nums[-1]]
#12
def has23(nums):
  return  nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3

#List-2
#1
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count
#2
def big_diff(nums):
  nums.sort()
  return nums[-1] - nums[0]
#2 或者
def big_diff(nums):
  return max(nums) - min(nums)
#3
def centered_average(nums):
  nums.sort()
  sum = 0
  for i in range(1, len(nums)-1):
    sum +=  nums[i]
  return sum / (len(nums) - 2)
#4

def sum13(nums):
  sum = 0
  i = 0
  while i < (len(nums)):
    if nums[i] == 13:
      i += 2
    else:
      sum += nums[i]
      i += 1
  return sum
#5
def sum67(nums):
  sum = 0
  flag = 0
  for i in range(len(nums)):
    if nums[i] != 6 and flag == 0:
      sum += nums[i]
    elif nums[i] == 6:
      flag = 1
    elif nums[i] == 7 and flag == 1:
      flag = 0
  return sum
#6
def has22(nums):
  for i in range(len(nums)-1):
    if nums[i:i+2] == [2, 2]:
      return True
  return False





