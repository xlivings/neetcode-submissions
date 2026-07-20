class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        grouped = {}
        for str in strs:
            grouped[str] = False
        for str1 in strs:
            tracker = []
            tracker.append(str1)
            for str2 in strs:
                if str1 == str2:
                    continue
                if self.isValidAnagram(str1, str2):
                    tracker.append(str2)
                    grouped[str2] = True
            if not grouped[str1]:
                groups.append(tracker)
                grouped[str1] = True

        return groups
    
    def isValidAnagram(self, s, t):
        # s = "anagram"
        # t = "nagaram"

        if len(s) != len(t):
            return False

        dictS = {}
        dictT = {}

        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        return dictT == dictS