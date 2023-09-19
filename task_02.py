def coincidence(list = [], range = []):
    k = []
    if list == [] or range == []:
        return []
    for element in list:
        try:
            int(element)
        except:
            continue
        if int(element) in range:
            k.append(element)
    return k


# print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
