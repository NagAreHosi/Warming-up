#List-1
#1
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

#2
def same_first_last(nums):
    if len(nums) == 0:
        return False
    elif nums[0] == nums[-1]:
        return  True
    return False

#3
def make_pi():
    return [3, 1, 4]

#4
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

#5
def sum3(nums):
    return nums[0] + nums[1] + nums[2]

#6
def rotate_left3(nums):
    L = nums[1:3] #切片器需要有一个返回值
    L.append(nums[0]) #append没直接在本身加，所以返回值是None
    return L

#7
def reverse3(nums):
    nums.reverse()
    return nums

#8
def max_end3(nums):
    m = max(nums[0], nums[2])
    return [m, m, m]

#9
def sum2(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0
    return nums[0] + nums[1]

#10
def middle_way(a, b):
    return [a[1],b[1]]

#11
def make_ends(nums):
    return [nums[0], nums[-1]]

#12
def has23(nums):
    return 2 in nums or 3 in nums

#List-2
#1
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count
    #return len(list(filter(lambda x: x % 2 == 0, nums)))

#2
def big_diff(nums):
    a, b = nums[0], nums[0]
    for i in range(1 ,len(nums)):
        a, b= max(a, nums[i]), min(b, nums[i])
    return a-b

#3
def centered_average(nums):
    sum = 0
    a, b = nums[0], nums[0]
    for i in range(0 ,len(nums)):
        a, b= max(a, nums[i]), min(b, nums[i])
        sum += nums[i]
    sum -= a + b
    return int(sum / (len(nums) - 2))

#4
def sum13(nums):
    sum = 0
    flag = False
    for i in range(len(nums)):
        if flag:
            flag = False
            continue
        if nums[i] == 13:
            flag = True
            continue
        sum += nums[i]
    return sum

#5
def sum67(nums):
    sum = 0
    flag = False
    for i in range(len(nums)):
        if flag:
            if nums[i] == 7:
                flag = False
            continue
        if nums[i] == 6:
            flag = True
            continue
        sum += nums[i]
    return sum
#6
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return  True
    return False