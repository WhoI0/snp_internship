def max_odd(array):
    odd_number = 0
    for element in array:
        if type(element) is not int and type(element) is not float:
            continue
        if element % 2 == 0:
            continue
        else:
            if element > odd_number:
                odd_number = int(element)
    print(odd_number)


print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
