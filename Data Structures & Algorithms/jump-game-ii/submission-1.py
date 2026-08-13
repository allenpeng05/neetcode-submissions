class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0

        while r < len(nums) - 1:
            max_index = float("-inf")
            for i in range(l, r + 1):
                max_index = max(max_index, i + nums[i])
            l, r = r + 1, max_index
            count += 1
        
        return count



        