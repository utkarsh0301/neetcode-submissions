class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        current_sum=nums[0]
        n =len(nums)
        for i in range(1,n):
            if current_sum<0:
                current_sum=0
            current_sum+=nums[i]
            if current_sum>ans:
                ans=current_sum
        return ans
    
