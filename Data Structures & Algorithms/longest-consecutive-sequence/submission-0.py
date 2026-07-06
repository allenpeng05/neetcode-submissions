class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        seen = set()
        for i in range(n):
            seen.add(nums[i])
        for x in seen:
            if x - 1 not in seen:
                current = 1
                start = x
                while (start + 1) in seen:
                    current += 1
                    start += 1
                answer = max(current, answer)
        return answer
            


            
        
        

        