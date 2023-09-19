def sort_list(array):
    if not array:
        return []
    element_min = min(array)
    element_max = max(array)
    for i in range(0, len(array)):
        if array[i] == element_min:
            array[i] = element_max
        elif array[i] == element_max:
            array[i] = element_min
    array.append(element_min)
    return array


# print(sort_list([1]))
