class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            midpoint = l + (r - l) // 2
            hours = sum(math.ceil(pile/midpoint) for pile in piles)
            if hours <= h:
                r = midpoint - 1
            else:
                l = midpoint + 1
        
        return l



        
        