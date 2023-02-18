class Solution:
    def isValid(self, s: str) -> bool:
        # solution: check if stack is empty
        
        
        # create dictionnary
        symbols = {")": "(", "}": "{", "]": "["}
        
        stack = []
        
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if (not stack) or (symbols.get(char) != stack.pop()): 
                    return False
        
        return stack == []
