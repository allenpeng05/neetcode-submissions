# one pass to add everything to a set
# a number x is a start of a chain if x - 1 not in set
# walk forward while x + 1 in set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        answer = 0
        for i in range(n):
            seen.add(nums[i])
        for x in seen:
            if x - 1 not in seen:
                start = x
                current = 1
                while (start + 1 in seen):
                    start += 1
                    current += 1
                answer = max(current, answer)
        return answer

        
            


            
        
        

        