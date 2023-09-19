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
    return odd_number if odd_number != 0 else None


# print(max_odd([2, 2, 4]))
