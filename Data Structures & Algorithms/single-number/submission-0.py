class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor=0
        for num in nums:
            xor^=num
        return xor
        