# cigar_party
def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    if cigars >= 40 and cigars <= 60:
        return True
    return False

# date_fashion
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

# squirrel_play
def squirrel_play(temp, is_summer):
    if temp >= 60:
        if is_summer:
            if temp <= 100:
                return True
        if temp <= 90:
            return True
    return False

# caught_speeding
def caught_speeding(speed, is_birthday):
    bad = 60
    worst = 80
    if is_birthday:
        bad += 5
        worst += 5
    if speed <= bad:
        return 0
    if speed <= worst:
        return 1
    if speed > worst:
        return 2

# sorta_sum
def sorta_sum(a, b):
    sum = a + b
    if sum >= 10 and sum <= 19:
        sum = 20
    return sum

# alarm_clock
def alarm_clock(day, vacation):
    weekday = "7:00"
    if vacation:
        if day == 0 or day == 6:
            return "off"
        weekday = "10:00"
    if day >= 1 and day <= 5:
        return weekday
    else:
        return "10:00"

# love6
def love6(a, b):
    if a == 6 or b == 6:
        return True
    if abs(a-b) == 6 or a+b == 6:
        return True
    return False

# in1to10
def in1to10(n, outside_mode):
    if outside_mode:
        if n <= 1 or n >= 10: return True
        else: return False
    if n >= 1 and n <= 10: return True
    return False

# near_ten
def near_ten(num):
    if (num % 10) <= 2: return True
    if (num % 10) >= 8: return True
    return False
