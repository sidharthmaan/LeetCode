'''https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)
        return result        
        
        
        
        
        # count = {}
        # result, maxcount = 0, 0

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     result = n if count[n] > maxcount else result
        #     maxcount = max(count[n], maxcount)
        # return result
