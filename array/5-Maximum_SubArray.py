'''https://leetcode.com/problems/maximum-subarray/'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = 0
        maxsub = nums[0]

        for i in nums:
            if cursum < 0:
                cursum = 0
            cursum += i
            maxsub = max(maxsub, cursum)
        return maxsub