class Solution(object):
    def reverseSign(self, number):
        if (str(number)[0] == '-'):
            return int(str(number)[1:])
        else:
            return int('-' + str(number))

    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_positive = []
        sorted_negative = []
        for num in nums:
            if (str(num)[0] == '-'):
                sorted_negative.append(num)
            else:
                sorted_positive.append(num)
        sorted_positive.sort()
        sorted_negative.sort()
        for i in range(k):
            if sorted_negative:
                first_negative = sorted_negative.pop(0)
                nums[nums.index(first_negative)] = self.reverseSign(first_negative)
                if not sorted_negative:
                    first_negative = self.reverseSign(first_negative)
                    for j in range(k - i -1):
                        nums[nums.index(first_negative)] = self.reverseSign(first_negative)
            elif sorted_positive:
                first_positive = sorted_positive.pop(0)
                if first_positive == 0:
                    sorted_positive.clear()
                else:
                    nums[nums.index(first_positive)] = self.reverseSign(first_positive)
        return sum(nums)


s = Solution()
# print(s.largestSumAfterKNegations([4, 2, 3], 1))
# print(s.largestSumAfterKNegations([2,-3,-1,5,-4], 2))
# print(s.largestSumAfterKNegations([3,-1,0,2], 3))
# print(s.largestSumAfterKNegations([-2,9,9,8,4], 5))
print(s.largestSumAfterKNegations([5,6,9,-3,3], 2))
# test = [4, 2, 3]
# test.pop(0)
# print(test)
# test.pop(0)
# test.pop(0)
# test.pop(0)
# print(test)

