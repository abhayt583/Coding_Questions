class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if nums[0]>=nums[1]:
            return 0
        if nums[-1]>=nums[-2]:
            return len(nums)-1

        
        for i in range(len(nums)):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i
            else:
                continue
        
       