class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0
        while i <= 32:
            if ((n >> i) & 1) == 1:
                count += 1
            i += 1

        return count
