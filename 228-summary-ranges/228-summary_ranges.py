def summaryRanges(nums):
    results = []
    if not nums:
        return results
    
    start = finish = nums.pop(0)
    for num in nums:
        if num != finish + 1:
            results.append(str(start) + "->" + str(finish) if start != finish else str(start))
            start = finish = num
        else:
            finish = num
    results.append(str(start) + "->" + str(finish) if start != finish else str(start))
    return results


if __name__ == "__main__":
    print(summaryRanges([0]))
    print(summaryRanges([0,1,2,4,5,7]))
    print(summaryRanges([0,2,3,4,6,8,9]))