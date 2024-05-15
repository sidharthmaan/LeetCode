'''https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            summ = numbers[left] + numbers[right]
            if summ > target:
                right -= 1
            elif summ < target:
                left += 1
            else:
                return [left + 1, right + 1]
