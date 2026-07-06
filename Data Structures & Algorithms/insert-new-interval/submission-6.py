class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #[a, b] *[c, d]*
        result = []
        n = len(intervals)
        i = 0

        #if interval is smaller than newInterval ie b < c
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        #if they are overlapping ie b >= c AND d >= a
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        #if interval is larger than newInterval ie a > d

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        