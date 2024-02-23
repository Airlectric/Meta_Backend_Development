class Solution:
    def isValid(self,s):
        open_bracket = {'(','{','['}
        close_bracket = {')':'(','}':'{',']':'['}
        stack = []

        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif char in close_bracket:
                if not stack or stack.pop() != close_bracket[char]:
                    return False
        return len(stack) == 0
