class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1=0
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                count+=1
                max1=max(max1,count)
            else:
                count=0
        return max1