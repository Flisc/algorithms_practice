from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i

    # Input: nums = [2, 2, 1]
    # Output: 1
s = Solution()
print(s.singleNumber([2, 2, 1]))
