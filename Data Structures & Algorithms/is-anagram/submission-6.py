class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        for char in t:
            d[char] = d.get(char, 0) - 1
        for k, v in d.items():
            if v != 0:
                return False
        return True

            

        