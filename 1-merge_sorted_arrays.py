def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    # border cases
    if len(nums1) != m + n or len(nums2) != n or m < 0 or m + n > 200:
        return
    if m == 0:
        nums1[:] = nums2[:]
        return

    # logic
    for i in reversed(range(len(nums1))):
        if n == 0:
            break
        left = m - 1
        right = n - 1
        if m != 0 and nums1[left] > nums2[right]:
            nums1[i] = nums1[left]
            m -= 1
        else:
            nums1[i] = nums2[right]
            n -= 1
