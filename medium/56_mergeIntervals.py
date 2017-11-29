# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Sort the intervals according to start value of each interval
# last added interval:[a,b] and next interval: [c,d]
# if a<c: append [c,d]
# if c<=b and d>b: modify [a,b] to [a,d]

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals)==0:
        return []
    intervals = sorted(intervals, key=lambda x: x.start)
    #print(intervals)
    result = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i].start>result[-1].end:
            result.append(intervals[i])
        else:
            if intervals[i].start <= result[-1].end and intervals[i].end>result[-1].end:
                result[-1].end = intervals[i].end
    return result