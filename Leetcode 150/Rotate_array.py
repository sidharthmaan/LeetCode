'''https://leetcode.com/problems/rotate-array/'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(nums, l, r):
            while(l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1
                r = r - 1

        k = k % len(nums)
        rev(nums, 0 , len(nums)-1)
        rev(nums, 0, k-1)
        rev(nums, k, len(nums)-1)
        
        
# Time Complexity is o(n)
# Space Complexity is o(1)