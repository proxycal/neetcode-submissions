class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        boom = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in boom:
                if stack and stack[-1] == boom[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0
        
        