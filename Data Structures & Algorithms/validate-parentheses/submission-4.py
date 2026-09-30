class Solution:
    mapper = {
      "(": ")",
      "{": "}",
      "[": "]",
    }

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        list = []
        for char in s:
            if char in self.mapper.keys(): # case 1 opening bracket
                list.append(char) # push to stack
            else: # case 2 closing bracket
                if len(list) == 0: # if stack is empty return false
                    return False
                else:# if stack has element
                    if self.mapper.get(list.pop()) != char:
                        return False
                
        if len(list) != 0: # check if stack is empty
            return False
        return True # if true return True otherwise false