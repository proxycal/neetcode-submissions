class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for i in s:
                v=s.count(i)
                u=t.count(i)
                if v!=u:
                    return False
            return True 
                
        else:
            return False