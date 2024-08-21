def is_palendrom(s) :
    s = s.lower().replace(" ","")
    return s == s[::-1]
print(is_palendrom("racecar"))

    