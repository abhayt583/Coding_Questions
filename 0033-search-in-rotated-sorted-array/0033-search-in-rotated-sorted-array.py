class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l 
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # Adjust mid index to account for rotation
            realMid = (mid + pivot) % len(nums)
            if nums[realMid] == target:
                return realMid  
            elif nums[realMid] < target:
                l = mid + 1
            else:
                r = mid - 1

     
        return -1
