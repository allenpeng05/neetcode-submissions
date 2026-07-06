# sort array to use two pointer method
# avoid duplicates by
# 1) in outer for loop skip if i is same as previous
# 2) once a solution is found, skip all same ones
# IMPORTANT: employ look behind instead of look ahead to avoid out of bounds
# IMPORTANT: guard everything with while left < right to avoid out of bounds
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return answer

            

        

        