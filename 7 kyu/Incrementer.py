def incrementer(nums):
    for i, num in enumerate(nums):
        nums[i] = (num + i + 1) % 10
    return nums