def combine_anagrams(words_array):
    group = {}
    for word in words_array:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in group:
            group[sorted_word].append(word)
        else:
            group[sorted_word] = [word]
    return list(group.values())


# print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
