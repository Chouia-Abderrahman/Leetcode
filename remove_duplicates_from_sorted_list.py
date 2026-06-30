from contextlib import nullcontext
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_number = nums[0]
        k = 1
        for number in nums:
            if current_number != number:
                k += 1
                current_number = number
                nums[k-1] = number
        nums = nums[:k]
        print(nums)
        print(k)
        return k




nums = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
s.removeDuplicates(nums)