class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        current = []
        result = []

        def backtrack(index, current_sum):
            
            # base case
            if current_sum == target:
                result.append(current.copy())
                return
            if current_sum > target:
                return
            if index == len(nums):
                return
        
            # include current number
            current.append(nums[index])
            backtrack(index, current_sum + nums[index])

            # exclude current number
            current.pop()
            backtrack(index + 1, current_sum)
        
        backtrack(0, 0)
        return result
        