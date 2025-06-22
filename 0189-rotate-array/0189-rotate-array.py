class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # l,r=0,len(nums)-1

        # while l<r:
        #     nums[l],nums[r]=nums[r],nums[l]

        result = []
        n = len(nums)
        k = k % n
        for i in range(n):
            index = (n - k + i) % n
            result.append(nums[index])
       
        for i in range(n):
            nums[i] = result[i]














        #   result=[]
        # # k=k% len(nums)
        # # two=len(nums)-1
        # # for i in range(k-1):
        # #     two=two-1
        # # one=two-1
        # # while one!=two:
        #       two=two%len(nums)
        #       result.append(nums[two])
        # #     two=two+1
        # # return nums
        
        