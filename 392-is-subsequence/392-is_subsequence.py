def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i = 0
    s_len = len(s)
    t_len = len(t)
    for j in range(t_len):
        if i == s_len:
            return True
        if s[i] == t[j]:
            i += 1
        elif s_len - i + 1 > t_len - j + 1:
            return False
    return True if i == s_len else False
