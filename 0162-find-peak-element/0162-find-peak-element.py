class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxx=float('-inf')
        for i,n in enumerate(nums):
            if n>maxx:
                maxx=n
            else:
                continue
        return nums.index(maxx)
       