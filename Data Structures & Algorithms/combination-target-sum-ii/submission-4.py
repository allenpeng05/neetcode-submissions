class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        candidates.sort()

        def backtrack(index, current_target):
            if current_target == 0:
                result.append(current.copy())
                return
            if index == len(candidates):
                return
            if current_target < 0: 
                return
            
            current.append(candidates[index])
            backtrack(index + 1, current_target - candidates[index])

            current.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, current_target)

        
        backtrack(0, target)
        return result
        