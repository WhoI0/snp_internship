def is_palindrome(string):
    if string is None:
        return False
    string = str(string)
    c = '''!()-[]{};:&^%$?.,\'\"/\\_*@`~# '''
    for x in c:
        string = string.replace(x, "").lower()
    if string == string[::-1]:
        return string == string[::-1]

print(is_palindrome(333))
