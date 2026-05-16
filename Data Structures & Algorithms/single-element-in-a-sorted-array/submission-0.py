class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashM={}
        n=len(nums)
        for i in range(n):
            hashM[nums[i]]=1+hashM.get(nums[i],0)
        for keys,values in hashM.items():
            if values==1:
                return keys
