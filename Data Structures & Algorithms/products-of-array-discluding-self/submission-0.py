class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]*n
        for i in range (n):
            ans=1
            for j in range(n):
                if i!=j:
                    ans*=nums[j]
            result.append(ans)
        return result
