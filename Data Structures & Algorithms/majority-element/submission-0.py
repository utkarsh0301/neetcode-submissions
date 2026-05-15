class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashM={}
        n=len(nums)
        for i in range (len(nums)):
            hashM[nums[i]]=1+hashM.get(nums[i],0)
        for key,value in hashM.items():
            if value>n//2:
                return key