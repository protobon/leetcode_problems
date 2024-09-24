from collections import defaultdict


def groupAnagrams(strs):
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    """

    anagrams_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        anagrams_dict[key].append(s)
    return anagrams_dict.values()

if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["a"]))
