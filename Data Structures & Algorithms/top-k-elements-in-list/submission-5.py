
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
        
        k_sorted_count = sorted_count[:k]
        answer = [num for num, freq in k_sorted_count]
        return answer
            


        


        