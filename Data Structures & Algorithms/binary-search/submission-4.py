class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            midpoint = l + (r - l) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return -1



        

        