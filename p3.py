def is_palendrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print("Dear User This program is perform a function when You enter a String if it's reverse same as the spelling of your string then it will return true otherwise it will return false")

sk : str = input("Enter a string to palendrome: ")
print(is_palendrome(sk))