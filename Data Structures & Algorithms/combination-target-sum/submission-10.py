# similar solution to subset, similar backtracking algorithm
# difference is that same number may be chosen multiple times

# base cases: we have used all the numbers, we find a correct combination(ie
# current_target = 0), we go over(ie current_target < 0)

# keep a current sum that is passed through the recursion as well
# when we backtrack, we can either skip the number, or use it
# we only move index forward when we skip the number because we are able to use it multiple times

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
        