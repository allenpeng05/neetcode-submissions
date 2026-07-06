class Solution:
    # use a default dict with factory function list
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            answer[sorted_s].append(s)
        return list(answer.values())
        





        
        