def unique_items(lst):
    seem = set()
    unique_list = []
    for item in lst:
        if item not in seem:
            unique_list.append(item)
            seem.add(item)
    return unique_list
lst = []
while True:
    words = input("Enter an integer or enter 'n' to stop the program : " )
    if words.lower() == 'n':
        break
    
    lst.append( words )
print(unique_items(lst))