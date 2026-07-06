# classic two pointers approach since array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while (l < r):
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l+1, r+1]
            elif currentSum > target:
                r -= 1
            else:
                l += 1

            


        