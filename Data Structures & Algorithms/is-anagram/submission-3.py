class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for schar, tchar in zip(s, t):
            d[schar] = d.get(schar, 0) + 1;
            d[tchar] = d.get(tchar, 0) - 1;
        for item in d:
            if d[item] != 0:
                return False
        return True
    
        

        