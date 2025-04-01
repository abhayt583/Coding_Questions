class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        hashm={}
        for index,value in enumerate(nums):
            hashm[value]=True
        if target in hashm:
            return True
        else:
            return False           
        