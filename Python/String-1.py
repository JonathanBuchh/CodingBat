# hello_name
def hello_name(name):
    return "Hello " + name + "!"

# make_abba
def make_abba(a, b):
    return a + b + b + a

# make_tags
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

# make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:4]

# extra_end
def extra_end(str):
    output = ""
    for x in range(3):
        output += str[len(str)-2:len(str)]
    return output

# first_two
def first_two(str):
    if len(str) < 2:
        return str
    else:
        return str[0:2]

# first_half
def first_half(str):
    half = len(str) / 2
    return str[:half]

# without_end
def without_end(str):
    return str[1:len(str)-1]

# combo_string
def combo_string(a, b):
    shorter = a
    longer = b
    if len(a) > len(b):
        shorter = b
        longer = a
    return shorter + longer + shorter

# non_start
def non_start(a, b):
    return a[1:] + b[1:]

# left2
def left2(str):
    return str[2:] + str[:2]
