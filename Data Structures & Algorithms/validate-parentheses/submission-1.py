class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping.values():  # If it's an opener
                stack.append(char)
            
            elif char in mapping.keys():  # If it's a closer
                if len(stack) == 0: 
                    return False
                
                if mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0  # All brackets must be closed