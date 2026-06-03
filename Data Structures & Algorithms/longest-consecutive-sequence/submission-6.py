class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        count = 1
        max_count = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1  # reset to 1, not 0

        return max_count