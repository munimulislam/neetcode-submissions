class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not len(stack):
                    return False

                opening = stack.pop()
                
                if (char == ']' and opening != '[') or (char == '}' and opening != '{') or (char == ')' and opening != '('):
                    return False
        
        return len(stack) == 0

        