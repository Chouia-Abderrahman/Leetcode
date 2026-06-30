import random
import timeit

# Brute Force Approach (O(n²))
def twoSum_brute_force(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):  # Fix: Start j from i+1
            if nums[i] + nums[j] == target:
                return [i, j]

# Hash Map Approach (O(n))
def twoSum_hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Test data
# nums = [2, 7, 11, 15]
# target = 9
nums = random.sample(range(1, 1000000), 1000)  # 10,000 unique random numbers
target = nums[100] + nums[500]  # Ensure there's at least one valid pair
# Measure execution time
brute_force_time = timeit.timeit(lambda: twoSum_brute_force(nums, target), number=100000)
hashmap_time = timeit.timeit(lambda: twoSum_hashmap(nums, target), number=100000)

# Print results
print(f"Brute Force Time: {brute_force_time:.6f} seconds")
print(f"Hash Map Time: {hashmap_time:.6f} seconds")
