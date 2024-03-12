class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        open_count = 0  # Keep track of opening parentheses

        for char in s:
            if char == "(":
                open_count += 1
                if open_count > 1:  # Skip the first opening parenthesis
                    result += char
            elif char == ")":
                open_count -= 1
                if open_count > 0:  # Skip the last closing parenthesis
                    result += char
            else:
                result += char  # Append other characters as they are

        return result