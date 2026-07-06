# create a set to store all the nums
# a number x is a start of a chain if x - 1 not in set
# walk forward while x + 1 in set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        answer = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                answer = max(answer, length)
        
        return answer
            


        
            


            
        
        

        