# use left and right pointers to maintain a current window
# use set to keep track of what characters are currently in the window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r + 1 -l)
        
        return best



        