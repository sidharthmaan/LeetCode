'''https://leetcode.com/problems/missing-number/'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = sum(nums)
        ans = 0
        for i in range(len(nums)+1):
            ans += i
        return ans - summ