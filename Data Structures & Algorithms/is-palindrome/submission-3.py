class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        s = s.lower()
        for i in s:
            if i.isalnum():  # isalpha() misses digits like "a1b1"
                clean += i   # actually append to clean
        return clean == clean[::-1]  # slice reverse instead of iterator
