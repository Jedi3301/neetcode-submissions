import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            if i == 0:
                final.append(math.prod(nums[1:]))
            else:
                final.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        return final