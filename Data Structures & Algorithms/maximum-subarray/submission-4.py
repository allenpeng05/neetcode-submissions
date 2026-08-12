# DP approach
# curSum tracker and bestSum tracker
# at each step, either add the current number to curSum, or start over(ie curSum = current number)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, bestSum = (float("-inf"), float("-inf"))

        for num in nums:
            curSum = max(curSum + num, num)
            bestSum = max(curSum, bestSum)
        
        return bestSum

        