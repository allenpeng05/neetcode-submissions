# basic binary search
# make sure to set midpoint = left + (right - left) // 2 to avoid overflow
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = l + (r - l) // 2
            curr = nums[midpoint]

            if curr == target:
                return midpoint
            elif curr < target:
                l = midpoint + 1
            else:
                r = midpoint - 1
        
        return -1






        

        