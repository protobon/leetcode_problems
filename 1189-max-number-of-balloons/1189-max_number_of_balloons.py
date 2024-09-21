def maxNumberOfBalloons(text):
    balloon = {
        "b": 1,
        "a": 1,
        "l": 2,
        "o": 2,
        "n": 1
    }
    count = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0
    }

    for char in text:
        if balloon.get(char):
            count[char] += 1
   
    if any([c == 0 for c in count.values()]):
        return 0
    
    count["l"] = count["l"] // 2
    count["o"] = count["o"] // 2
    return min(count.values())


if __name__ == "__main__":
    print(maxNumberOfBalloons("nlaebolko"))
    print(maxNumberOfBalloons("loonbalxballpoon"))
    print(maxNumberOfBalloons("leetcode"))
