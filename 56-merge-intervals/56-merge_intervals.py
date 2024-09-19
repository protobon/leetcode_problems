def mergeIntervals(intervals):
    if len(intervals) == 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    results = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = results[-1]
        next_interval = intervals[i]

        if next_interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            results.append(next_interval)
    
    return results



if __name__ == "__main__":
    print(mergeIntervals([[1,4],[0,0]]))
    print(mergeIntervals([[1,4],[0,4]]))
    print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
    print(mergeIntervals([[1,4],[4,5]]))
