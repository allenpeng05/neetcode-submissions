# simple two pointer solution
# move the shorter bar inwards, since this is the bottleneck
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        answer = 0
        while l < r:
            height = min(heights[l], heights[r])
            distance = r - l
            amount = height * distance
            answer = max(amount, answer)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return answer
        
        