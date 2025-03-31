class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while l<r:
            mid=(l+r)//2
            if nums[l]>nums[mid]:
                l=mid+1
            else:
                r=mid
        smallest_no=r
        l=smallest_no
        r=smallest_no-1
        while l<r:
            mid=(l+2)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<taget:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
        return -1
            






        