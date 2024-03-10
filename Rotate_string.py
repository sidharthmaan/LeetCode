# Input: s = "abcde", goal = "cdeab"
# Output: true
# Input: s = "abcde", goal = "abced"
# Output: false

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal + goal