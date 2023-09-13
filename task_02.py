def coincidence(list, range):
    if list == [] or range ==[]:
        return []
    for element in list:
        try:
            int(element)
        except:
            continue
        if int(element) in range:
            print(element)


print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))


