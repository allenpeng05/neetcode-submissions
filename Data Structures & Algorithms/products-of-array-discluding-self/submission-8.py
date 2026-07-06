class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix/suffix method:
        #prefix pass: compute product of everything before i
        #suffix pass: multiply by product of everything after i
        n = len(nums)
        output = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output

