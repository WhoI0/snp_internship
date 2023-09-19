def connect_dicts(dict1, dict2):
    sorted_dict = {}
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    if sum1 > sum2:
        prior_dict = dict1
        ne_prior_dict = dict2
    else:
        prior_dict = dict2
        ne_prior_dict = dict1
    for key, value in ne_prior_dict.items():
        if value >= 10:
            sorted_dict[key] = value
    for key, value in prior_dict.items():
        if value >= 10:
            sorted_dict[key] = value
    return dict(sorted(sorted_dict.items(), key=lambda item: item[1]))


# print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
