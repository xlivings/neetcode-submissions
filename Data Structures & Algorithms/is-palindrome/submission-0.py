class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i].isalnum() and s[j].isalnum() and s[i] == s[j]:
                i = i + 1
                j = j - 1
            elif s[i].isalnum() and s[j].isalnum() and s[i] != s[j]:
                return False
            elif not s[i].isalnum():
                i = i + 1
            elif not s[j].isalnum():
                j = j - 1
            
        return True
        