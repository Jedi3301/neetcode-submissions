class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for i in strs:
            sorted_key = tuple(sorted(i))
            if sorted_key not in hashmap:
                hashmap[sorted_key] = []
            hashmap[sorted_key].append(i)
        return list(hashmap.values())