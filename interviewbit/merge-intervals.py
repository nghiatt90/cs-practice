# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals or len(intervals) == 0:
            return [newInterval]
        
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1
        
        # End of array
        if i == len(intervals):
            return intervals + [newInterval]
        
        # New inteval is not overlapped
        if intervals[i].start > newInterval.end:
            return intervals[:i] + [newInterval] + intervals[i:]
        
        # Merge
        intervals[i].start = min(intervals[i].start, newInterval.start)
        j = i
        while j < len(intervals) and intervals[j].start <= newInterval.end:
            j += 1
        intervals[i].end = max(intervals[j-1].end, newInterval.end)
        return intervals[:i+1] + intervals[j:]
        
