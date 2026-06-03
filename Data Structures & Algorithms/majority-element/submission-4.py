from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = Counter(nums)
        majority = len(nums)//2
        keys = [k for k, v in element_count.items() if v >= majority]
        return keys[0]
        