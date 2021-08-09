# sleep_in
def sleep_in(weekday, vacation):
    if vacation is True:
        return True
    if weekday is False:
        return True
    else:
        return False

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if a_smile is False and b_smile is False:
        return True
    return False

# sum_double
def sum_double(a, b):
    if a is b:
        return (a + b)*2
    return a + b

# diff21
def diff21(n):
    if n > 21:
        return abs(21-n)*2
    return abs(21-n)

# parrot_trouble
def parrot_trouble(talking, hour):
    if talking is True:
        if hour < 7 or hour > 20:
            return True
    return False

# makes10
def makes10(a, b):
    if a is 10 or b is 10:
        return True
    if a + b is 10:
        return True
    return False

# near_hundred
def near_hundred(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10:
        return True
    return False

# pos_neg
def pos_neg(a, b, negative):
    if negative is True:
        if a < 0 and b < 0:
            return True
        return False
    if a < 0 and b > 0:
        return True
    if a > 0 and b < 0:
        return True
    return False

# not_string
def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str

# missing_char
def missing_char(str, n):
    return str[:n] + str[n + 1:]

# front_back
def front_back(str):
    if len(str) <= 1:
        return str
    return str[len(str)-1] + str[1:len(str)-1] + str[0]

# front3
def front3(str):
    if len(str) < 3:
        return str + str + str
    triple = str[0:3]
    return triple + triple + triple
