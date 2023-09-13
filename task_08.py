def multiply_numbers(inputs):
    if type(inputs) !=str:
        inputs = str(inputs)
    result = 1
    for num in inputs:
        if num.isdigit():
            result *= int(num)
    return result if result !=1 else None
print(multiply_numbers([5, 6, 4]))