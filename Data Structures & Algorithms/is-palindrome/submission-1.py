class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clear = ""
        for ch in s:
            if ch.isalnum():
                clear+=ch

        return clear==clear[::-1]
        
    

        
        

