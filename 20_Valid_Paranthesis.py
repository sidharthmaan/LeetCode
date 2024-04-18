"""https://leetcode.com/problems/valid-parentheses/"""

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for bracket in s:
            if bracket in brackets:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[bracket] != top:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True    