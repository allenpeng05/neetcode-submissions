# similar solution to subset, similar backtracking algorithm
# difference is that same number may be chosen multiple times

# base cases: we have used all the numbers, we find a correct combination(ie
# current_target = 0), we go over(ie current_target < 0)

# keep a current_target to track which numbers we used
# when we backtrack, we can either skip the number, or use it
# we only move index forward when we skip the number because we are able to use it
# multiple times
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        result = []

        def backtrack(index, current_target):
            if current_target == 0:
                result.append(current.copy())
                return
            if index == len(nums):
                return
            if current_target < 0:
                return
            
            current.append(nums[index])
            backtrack(index, current_target - nums[index])

            current.pop()
            backtrack(index + 1, current_target)
        
        backtrack(0, target)
        return result

            
