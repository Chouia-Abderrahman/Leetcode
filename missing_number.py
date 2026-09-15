class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [None]* (len(nums)+1)
        print(seen)
        for i in nums:
            seen[i] = i
        for i in range(0, len(seen)):
            if seen[i] == None:
                return i



if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
    ]

    for nums in test_cases:
        result = sol.missingNumber(nums)
        print(f"nums = {nums} -> missing number = {result}")