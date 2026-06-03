class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        for i in nums:
            freq[i].append(i)

        for i in freq.keys():
            freq[i] =len(list(freq[i]))

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num, count in sorted_freq[:k]:
            result.append(num)

        return result