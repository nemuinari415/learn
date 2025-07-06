#アルゴリズム 線形探索
def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))