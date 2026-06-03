from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        # Sort by frequency (descending) and get top k elements
        top_k = freq_count.most_common(k)
        return [num for num, freq in top_k]