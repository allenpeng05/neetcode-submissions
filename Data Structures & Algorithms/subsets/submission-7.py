# backtracking algorithm
# save the global result, as well as the current subset we are building
# when index == len(nums), we have made a decision about every number
# for num in nums, we either include it or don't include it
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index):
            if index == len(nums):
                result.append(current.copy())
                return
            
            current.append(nums[index])
            backtrack(index + 1)

            current.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return result
            
            

            
        