class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = deque()

        for c in s:
            if c in d.keys():
                stack.append(c)
            else:
                if not stack or c != d[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return not stack



        