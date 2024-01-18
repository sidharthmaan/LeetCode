class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i, j]

        # return 

        # Using HashMap
        
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i
        return