class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        result = []

        def backtrack(index, current_target):
            if index == len(nums):
                return
            if current_target == 0:
                result.append(current.copy())
                return
            if current_target < 0:
                return
            
            current.append(nums[index])
            backtrack(index, current_target - nums[index])
            current.pop()
            backtrack(index + 1, current_target)
        
        backtrack(0, target)
        return result
            

