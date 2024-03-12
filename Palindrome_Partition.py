''' https://leetcode.com/problems/palindrome-partitioning/submissions/1199861531/ '''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # return s.split()

        n = len(s)
        ans = []
        if n == 0:
            return [[]]
        
        for i in range(1,n+1):
            if s[:i] != s[:i][::-1]:
                continue
            cur = self.partition(s[i:])
            for j in range(len(cur)):
                ans.append([s[:i]]+ cur[j])
        return ans