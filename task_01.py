def is_palindrome(string):
    if string is None:
        return False
    string = str(string)
    c = '''!()-[]{};:&^%$?.,\'\"/\\_*@`~# '''
    for x in c:
        string = string.replace(x, "").lower()
    if string == string[::-1]:
        return string == string[::-1]
    else:
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
