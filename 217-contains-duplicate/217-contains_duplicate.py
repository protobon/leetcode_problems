def containsDuplicate(nums):
    myset = set()
    for n in nums:
        if n in myset:
            return True
        myset.add(n)
    return False


if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
