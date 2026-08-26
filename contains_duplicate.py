class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        for i in nums:
            if i in unique:
                return True
            else:
                unique.add(i)
        return False



solution = Solution()

tests = [
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 1], True),
    ([1, 1], True),
    ([1], False),
    ([], False),
    ([1, 2, 3, 2, 4], True),
    ([5, 5, 5, 5], True),
    ([-1, -2, -3, -4], False),
    ([-1, -2, -3, -1], True),
    ([0, 1, -1, 2, -2], False)
]

for nums, expected in tests:
    result = solution.containsDuplicate(nums)
    print("Input:", nums)
    print("Result:", result)
    print("Expected:", expected)
    print("---")