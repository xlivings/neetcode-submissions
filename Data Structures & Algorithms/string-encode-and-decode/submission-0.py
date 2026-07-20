class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded = ""
        for str1 in strs:
            encoded = encoded + str1 + str(len(str1)) + "*"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        for i in range(len(s)):
            if s[i] == '*':
                length = int(s[i-1])
                arr.append(s[i-length-1:i-1])
        return arr