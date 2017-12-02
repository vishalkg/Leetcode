# Insert interval in a list of interval
# Find the position at which to insert
# Insert and call mergeintervals with imsertion_index-1
# Time: O(n)
# Finding insertion_index can be improved to O(log n) using binary search

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    if len(intervals) == 0:
        return [newInterval]
    
    def mergeIntervals(intervals,i):
        while True:
            if i==len(intervals)-1:
                break
            #if intervals[i].end < intervals[i+1].start:
            #    break
            if intervals[i].start <= intervals[i+1].start <= intervals[i].end:
                intervals[i].end = max(intervals[i].end,intervals[i+1].end)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
        
    if newInterval.start<=intervals[0].start:
        return mergeIntervals([newInterval]+intervals,0)
    if intervals[-1].start<=newInterval.start:
        return mergeIntervals(intervals+[newInterval],len(intervals)-1)
    for i in range(len(intervals)):
        if intervals[i].start <= newInterval.start < intervals[i+1].start:
            return mergeIntervals(intervals[0:i+1]+[newInterval]+intervals[i+1:],i)