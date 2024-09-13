def mergeAlternately(word1, word2):
    """
    Merges two strings alternately. If one string is larger than the other, appends the rest to the end.

    Constraints:

    1 <= len(word1), len(word2) <= 100
    """
    result = ""    
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        result += word1[i] + word2[i]
    result += word1[min_len:] if min_len < len(word1) else word2[min_len:]
    return result
