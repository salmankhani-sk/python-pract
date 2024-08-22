def unique_element(lst):
    seen = set()
    unique_lst = []
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

lst = [1,2,3,2,4,56,7,3,23,66,77,66,75,345,86,34,86,1,2,3]

print(unique_element(lst))