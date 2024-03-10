class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        
        # Another Way
    
        # l = s.split()
        # n = len(l[-1])
        # return n