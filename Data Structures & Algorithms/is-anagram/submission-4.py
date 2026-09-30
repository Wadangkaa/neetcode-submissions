class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        distS, distT = {}, {}
        for i in range(len(s)):
            distS[s[i]] = distS.get(s[i], 0) + 1
            distT[t[i]] = distT.get(t[i], 0) + 1
        
        for c in distS:
            if distS[c] != distT.get(c, 0):
                return False
        return True