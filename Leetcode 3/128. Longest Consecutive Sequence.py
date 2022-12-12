class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        nums = list(nums_set)
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            cur_len = 1
            temp = nums[i]
            while(temp + 1 in nums_set):
                cur_len += 1
                temp += 1
            max_len = max(max_len,cur_len)
        return max_len