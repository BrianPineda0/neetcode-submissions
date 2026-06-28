class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
                continue

            match c:
                case ")":
                    if not stack or stack.pop() != "(": return False
                case "]":
                    if not stack or stack.pop() != "[": return False
                case "}":
                    if not stack or stack.pop() != "{": return False
                case _:
                    continue

        
        
        if stack: return False
        else: return True
