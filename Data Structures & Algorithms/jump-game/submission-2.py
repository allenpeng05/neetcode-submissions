class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = [0] * n
        reach[0] = 1
        for i in range(n):
            if reach[i] != 1:
                continue
            jumps = nums[i]
            for j in range(1, jumps + 1):
                if i + j < n:
                    reach[i + j] = 1
        return reach[n - 1] == 1
            


        