# first_last6
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        return True
    return False

# same_first_last
def same_first_last(nums):
    if len(nums) > 1:
        if nums[0] == nums[len(nums)-1]:
            return True
    if len(nums) == 1:
        return True
    return False

# make_pi
def make_pi():
    return [3, 1, 4]

# common_end
def common_end(a, b):
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    return False

# sum3
def sum3(nums):
    count = 0
    for i in range(len(nums)):
        count += nums[i]
    return count

# rotate_left3
def rotate_left3(nums):
    array = nums
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = temp
    return nums

# reverse3
def reverse3(nums):
    output = [nums[2], nums[1], nums[0]]
    return output

# max_end3
def max_end3(nums):
    larger = max(nums[0], nums[2])
    return [larger, larger, larger]

# sum2
def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) > 1:
        return nums[0] + nums[1]

# middle_way
def middle_way(a, b):
    return [a[1], b[1]]

# make_ends
def make_ends(nums):
    return [nums[0], nums[len(nums)-1]]

# has23
def has23(nums):
    if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
        return True
    return False
