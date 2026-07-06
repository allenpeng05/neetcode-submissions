# simply two pointer solution
# move the shorter bar inwards, since this is the bottleneck
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        answer = 0
        left, right = 0, n - 1
        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            answer = max(answer, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return answer
        