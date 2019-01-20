#List-1
#1
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) -1] == 6:
        return True
    return False

#2
def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
        return True
    return False

#3
def make_pi():
  return [3,1,4]

#4
def common_end(a, b):
    if a[0] == b[0] or a[len(a) - 1] == b[len(b) -1]:
        return  True
    return False

#5
def sum3(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum

#6
def rotate_left3(nums):
    temp = 0
    temp = nums[0]
    nums[0] = nums[2]
    nums[2] = temp
    temp = nums[0]
    nums[0] = nums[1]
    nums[1] = temp
    return nums

#7
def reverse3(nums):
    temp = 0
    temp = nums[0]
    nums[0] = nums[2]
    nums[2] = temp
    return nums

#8
def max_end3(nums):
    larger = max(nums[0], nums[2])
    return [larger, larger, larger]

#9
def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return  nums[0] + nums[1]


#10
def middle_way(a, b):
    c = []
    c.append(a[1])
    c.append(b[1])
    return c

#11
def make_ends(nums):
    a = []
    a.append(nums[0])
    a.append(nums[len(nums) - 1])
    return a

#12
def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    return False


#List-2
#1
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1
    return count

#2
def big_diff(nums):
    biggest = max(nums)
    smallest = min(nums)
    return biggest - smallest

#3
def centered_average(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        return (nums[int(len(nums)/2)] + nums[int(len(nums)/2 - 1)]) / 2
    else:
        return nums[int(len(nums)/2)]


#4
def sum13(nums):
    sum = 0
    i = 0
    if len(nums) == 0:
        return sum
    else:
        while(i < len(nums)):
            if nums[i] != 13:
                sum = sum + nums[i]
            else:
                i = i + 1
            i = i + 1
    return sum

#5
def sum67(nums):
    i = 0
    sum = 0
    while(i < len(nums)):
        if nums[i] != 6:
           sum = sum + nums[i]
           i = i + 1
        else:
            j = i
            while(j < len(nums)):
                if nums[j] != 7:
                    j = j + 1
                else:
                    i = j
                    i = i +1
                    break
    return sum

#6
def has22(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 2:
            if i + 1 >= len(nums):
                return False
            else:
                if nums[i + 1] == 2:
                    return  True
                else:
                    i = i + 1
                    continue
        else:
            i = i + 1
    return False
