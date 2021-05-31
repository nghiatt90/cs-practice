# https://www.interviewbit.com/problems/merge-overlapping-intervals/
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
    
#     def __repr__(self):
#         return f'[{self.start}, {self.end}]'

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        output = []
        current = intervals[0]
        for o in intervals[1:]:
            if o.start <= current.end:
                current.end = max(current.end, o.end)
            else:
                output.append(current)
                current = o
        output.append(current)
        return output
