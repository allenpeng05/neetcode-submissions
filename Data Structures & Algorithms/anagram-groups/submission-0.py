class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for item in strs:
            sorted_word = ''.join(sorted(item))
            if sorted_word not in s:
                s[sorted_word] = [item]
            else:
                s[sorted_word].append(item)
        return list(s.values())

        
        