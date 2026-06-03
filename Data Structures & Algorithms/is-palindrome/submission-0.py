class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for i in s:
            if i.isalnum():  # ✅ Call the method using parentheses
                clean += i.lower()  # also lowercase for case insensitivity
        return clean == clean[::-1]