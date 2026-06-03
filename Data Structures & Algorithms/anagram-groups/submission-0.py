class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anag_map:
                anag_map[sorted_word].append(word)
            else:
                anag_map[sorted_word] = [word]
        return list(anag_map.values())