def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    prefix = strs.pop(0)
    prefix_len = len(prefix)
    for s in strs:
        while prefix[:prefix_len] != s[:prefix_len]:
            prefix_len -= 1
        if not prefix_len:
            return ""
    return prefix[:prefix_len]