class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low <= high:
            mid = (low + high) // 2  # Calculate mid pointer

            # Step 1: Check if mid points to the target
            if nums[mid] == target:
                return mid  # Return index of the target
            
            # Step 2: Identify the sorted half
            if nums[low] <= nums[mid]:  # Left half is sorted
                # Check if target is in the sorted left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1  # Eliminate the right half
                else:
                    low = mid + 1  # Eliminate the left half
            else:  # Right half is sorted
                # Check if target is in the sorted right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1  # Eliminate the left half
                else:
                    high = mid - 1  # Eliminate the right half
        return -1
        