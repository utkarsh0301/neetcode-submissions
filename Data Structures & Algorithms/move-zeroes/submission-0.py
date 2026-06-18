class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[low]=nums[low],nums[i]
                low+=1

        