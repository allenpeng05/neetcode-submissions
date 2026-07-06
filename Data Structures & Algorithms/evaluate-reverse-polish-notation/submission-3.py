class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                match token:
                    case "+":
                        result = b + a
                    case "-":
                        result = b - a
                    case "*":
                        result = b * a
                    case "/":
                        result = int(b/a)
                stack.append(result)
        return int(stack.pop())
                

        