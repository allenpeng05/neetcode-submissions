class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0
        # no overlap between [a, b] and [c, d]
        # b < c
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1 
        # if there is overlap between [a, b] and [c, d]
        #1: b >= c AND
        #2: d >= a
        # no need to add b >= c check since we know its true if we are in this loop
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        # no overlap between [a, b] and [c, d]
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

        

        