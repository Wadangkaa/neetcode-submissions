class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
      
        container1 = {}
        container2 = {}
      
        for i in range(len(s)):
            container1.update({s[i]: container1[s[i]] + 1 if container1.get(s[i]) else 1})
            container2.update({t[i]: container2[t[i]] + 1 if container2.get(t[i]) else 1})
        
        for key, value in container1.items():
            if (container2.get(key) != value):
                return False
        
        return True