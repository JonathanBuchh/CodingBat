# string_times
def string_times(str, n):
    output = ""
    for x in range(n):
        output += str
    return output

# front_times
def front_times(str, n):
    output = ""
    if len(str) < 3:
        for x in range(n):
            output += str
    else:
        for x in range(n):
            output += str[0:3]
    return output

# string_bits
def string_bits(str):
    return str[0:len(str):2]

# string_splosion
def string_splosion(str):
    output = ""
    for x in range(len(str)+1):
        output += str[0:x]
    return output

# last2
def last2(str):
    end = str[len(str)-2:len(str)]
    output = 0
    for x in range(len(str)-2):
        if str[x:x+2] == end:
            output += 1
    return output

# array_count9
def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count

# array_front9
def array_front9(nums):
    if len(nums) < 4:
        for i in nums:
            if i == 9:
                return True
    else:
        for i in range(4):
            if nums[i] == 9:
                return True
    return False

# array123
def array123(nums):
    for x in range(len(nums)-2):
        if nums[x] == 1:
            if nums[x+1] == 2:
                if nums[x+2] == 3:
                    return True
    return False

# string_match
def string_match(a, b):
    count = 0
    shorter = min(len(a), len(b))
    for i in range(len(a)-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
