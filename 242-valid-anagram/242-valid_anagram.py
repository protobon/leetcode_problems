def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_letters = dict()
    for letter in s:
        if s_letters.get(letter):
            s_letters[letter] += 1
        else:
            s_letters[letter] = 1
    for letter in t:
        if not s_letters.get(letter):
            return False
        s_letters[letter] -= 1
    return True


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
