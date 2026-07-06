# we want to keep the k smallest distances
# use max heap trick : negative distances, so smallest one at root is actually largest
# push (-dist, x, y)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # sqrt is monotonic, no need for is
            distance = x*x + y*y
            heapq.heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result

        