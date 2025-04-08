class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_duplicate_set=set(nums)
        return len(non_duplicate_set)<len(nums)
        