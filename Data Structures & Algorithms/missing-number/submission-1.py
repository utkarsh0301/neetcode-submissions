class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=((n)*(n+1))//2
        add =0
        for i in range(n):
            add+=nums[i]
        return sum-add

    