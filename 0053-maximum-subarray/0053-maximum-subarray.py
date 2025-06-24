class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=nums[0]
        cur=0
        for i in nums:
            if cur<0:
                cur=0
            cur=cur+i
            if cur>maxx:
                maxx=cur
        return maxx