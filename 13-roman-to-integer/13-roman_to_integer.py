def romanToInt(s: str) -> int:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    skip = False
    for i in range(len(s) - 1):
        if skip:
            skip = False
            continue
        if symbols[s[i]] < symbols[s[i+1]]:
            result += symbols[s[i+1]] - symbols[s[i]]
            skip = True
        else:
            result += symbols[s[i]]
    if not skip:
        result += symbols[s[-1]]
    return result