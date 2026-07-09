class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float("-inf")
        bestSum = float("-inf")
        for num in nums:
            curSum = max(curSum + num, num)
            bestSum = max(bestSum, curSum)
        return bestSum
        