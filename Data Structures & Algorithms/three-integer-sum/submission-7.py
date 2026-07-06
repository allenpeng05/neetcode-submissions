class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        answer = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = sorted_nums[j] + sorted_nums[k]
                if s == target:
                    answer.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k+1]:
                        k -= 1

                elif s > target:
                    k -= 1
                else:
                    j += 1
        return answer

        