class Solution:
    def isPalindrome(self, s: str) -> bool:
       word=s.lower()
       boom=[]
       for i in word:
         if i.isalnum():
             boom.append(i)
       if boom[::-1]==boom:
         return True 
       else:
         return False


        

        
        