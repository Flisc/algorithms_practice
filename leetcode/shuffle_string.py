class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        charByIndex = {}
        for i in indices:
            charByIndex[indices[i]] = s[i]
        return ''.join(str(v) for v in charByIndex.values())

s = Solution()
s.restoreString('asd', [0, 2, 1])
