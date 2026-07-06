# the max speed we have to check is the size of the largest pile
# the min speed is 1
# time it takes to finish a pile is the ceiling of # bananas/speed
# everything less than l is too slow
# everything greater than r works
# therefore, when l > r, then l must be the mininum viable speed
# because l works(since l > r), but everything less than l is too slow
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



        
        