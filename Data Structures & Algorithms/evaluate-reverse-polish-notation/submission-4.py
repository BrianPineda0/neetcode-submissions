class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok in "+-/*":
                a = stack.pop()
                b = stack.pop()
                match tok:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(b-a)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(b / a))

            else: stack.append(int(tok))
        
        return stack.pop()
