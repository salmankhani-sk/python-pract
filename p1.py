def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz:", i)
        elif i % 5 == 0:
            print("buzz:" , i)
        elif i % 3 == 0:
            print("fizz:", i)
        
        else :
            print(i)
fizz_buzz()