# negative values then heapify into minheap to simulate maxheap
# in maxheap, heap[0] ie root is largest value
# negative values when pushing and popping
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))
        
        return -stones[0] if stones else 0