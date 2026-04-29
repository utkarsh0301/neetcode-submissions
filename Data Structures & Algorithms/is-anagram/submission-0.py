class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #brute force solution  
        #time complexity sorted(s) ,sorted(t)
        # : O(nlogn+mlogm)

        if sorted(s)!=sorted(t):
            return False
        else:
            return True

