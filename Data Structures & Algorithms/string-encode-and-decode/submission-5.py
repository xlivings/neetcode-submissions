class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded = ""
        sizes = ""
        for curr in strs:
            multiDigit = ""
            strLength = str(len(curr))
            if len(strLength) > 1:
                multiDigit = "[" + str(len(curr)) + "]"
                sizes = sizes + multiDigit
            else:
                sizes = sizes + str(len(curr))
            encoded = encoded + curr
            print(len(curr))
        sizes = sizes + "*"
        encoded = sizes + encoded
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        bracketSeen = False
        arr = []
        lengths = []
        i = 0
        multiDigit = ""
        while s[i] != "*":
            if s[i] == "[" or bracketSeen:
                if s[i] == "]":
                    bracketSeen = False
                    lengths.append(int(multiDigit[1:]))
                    multiDigit = ""
                else:
                    multiDigit = multiDigit + s[i]
                    bracketSeen = True
            else:
                lengths.append(int(s[i]))
            i += 1
        i = i + 1
        for j in range(len(lengths)):
            arr.append(s[i:i+lengths[j]])
            i = i + lengths[j]
            
        return arr