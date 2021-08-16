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
