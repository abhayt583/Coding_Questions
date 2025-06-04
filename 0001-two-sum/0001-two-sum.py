class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  
        for i, num in enumerate(nums):
            t = target - num
            if t in dict:  
                return [dict[t], i] 
            else:
                dict[num] = i 