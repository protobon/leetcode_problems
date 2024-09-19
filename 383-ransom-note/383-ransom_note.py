def canConstruct(ransomNote, magazine):
    letters = dict()
    for letter in magazine:
        if not letters.get(letter):
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in ransomNote:
        if not letters.get(letter):
            return False
        letters[letter] -= 1
    return True


if __name__ == "__main__":
    print(canConstruct("a", "b"))
    print(canConstruct("aa", "ab"))
    print(canConstruct("aa", "aab"))
