class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        n = len(intervals)
        i = 0

        result.append(intervals[i])
        i += 1

        while i < n:
            # is there overlap between current interval and previous existing in result
            # [a, b] and [c, d]
            # d >= a and c <= b
            if intervals[i][1] >= result[-1][0] and intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
                i += 1
            #if not, just append
            else:
                result.append(intervals[i])
                i += 1 
        return result
        