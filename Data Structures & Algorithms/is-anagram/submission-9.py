class Solution:
    ## create a dictionary to track the count of characters in a word
    ## first pass adds to the count(for s)
    ## second pass removes from the count(for t)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        for char in t:
            d[char] = d.get(char, 0) - 1
        for v in d.values():
            if v != 0:
                return False
        return True

            

        