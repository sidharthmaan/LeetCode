class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num = nums[0]
        count = 0
        i = 0
        while(i < len(nums)):
            if(nums[i] == num):
                if(count < 2):
                    count += 1
                    i += 1
                    continue
                else:
                    nums.pop(i)
                    continue
            else:
                num = nums[i]
                count = 1
                i += 1
        return len(nums)