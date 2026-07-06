class Solution:
    def isValid(self, s: str) -> bool:
        answer = []
        for item in s:
            if item in '({[':
                answer.append(item)
            else:
                if not answer:
                    return False
                top = answer.pop()
                match item:
                    case ')':
                        if top != '(':
                            return False
                    case '}':
                        if top != '{':
                            return False
                    case ']':
                        if top != '[':
                            return False
        if not answer:
            return True
        else:
            return False


        