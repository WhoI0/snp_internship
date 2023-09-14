def count_words(string):
    words_with_count = {}
    list_of_words = string.lower().replace(",", "").replace("-", "").replace("  ", " ").split(' ')
    for word in list_of_words:
        if words_with_count.get(word):
            words_with_count[word] += 1
        else:
            words_with_count[word] = 1
    return words_with_count


print(count_words("A man, a plan, a canal -- Panama"))
