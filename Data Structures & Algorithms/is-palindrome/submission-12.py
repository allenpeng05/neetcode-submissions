# form a clean string with only lowercase alphanumerical characters
# see if the clean string is the same as clean string[::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c.lower() for c in s if c.isalnum())
        return clean == clean[::-1]
        
        