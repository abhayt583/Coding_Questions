class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i,v in enumerate(nums):
            if v in dict:
                return True
            dict[v]=True
        return False
        