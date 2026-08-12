# greedy solution
# i > maxReachIndex, means we are unable to reach this index, so return false
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachIndex = 0

        for i in range(len(nums)):
            if i > maxReachIndex:
                return False
            maxReachIndex = max(maxReachIndex, i + nums[i])
        
        return True
            


        