'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        for i in range(1, len(nums)):
            if nums[first] != nums[i]:
                first += 1
                nums[first] = nums[i]
        return first + 1