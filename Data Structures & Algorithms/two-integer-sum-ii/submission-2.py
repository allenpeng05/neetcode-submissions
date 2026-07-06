class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 1
        index2 = len(numbers)
        while index2 > index1:
            sum = numbers[index1-1] + numbers[index2-1]
            if sum == target:
                return [index1, index2]
            elif sum > target:
                index2 -= 1
            else:
                index1 +=1



        