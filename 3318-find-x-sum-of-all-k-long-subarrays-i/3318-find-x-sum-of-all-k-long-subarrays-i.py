from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        n = len(nums)
        
        
        for i in range(n - k + 1):
         
            freq = {}  
            j = i
            while j < i + k:
                num = nums[j]
                
                if num in freq:
                    freq[num] = freq[num] + 1
                else:
                    freq[num] = 1
                j += 1

           
            pairs = []
            for key in freq:
                pair = [freq[key], key]  
                pairs.append(pair)

            m = len(pairs)
           
            for a in range(m):
                max_index = a
                for b in range(a + 1, m):
                    
                    if pairs[b][0] > pairs[max_index][0]:
                        max_index = b
                  
                    elif pairs[b][0] == pairs[max_index][0]:
                        if pairs[b][1] > pairs[max_index][1]:
                            max_index = b

                if max_index != a:
                    temp = pairs[a]
                    pairs[a] = pairs[max_index]
                    pairs[max_index] = temp


            sum_top_x = 0
            count_taken = 0
            idx = 0
            while idx < m and count_taken < x:
                sum_top_x = sum_top_x + pairs[idx][0] * pairs[idx][1]
                count_taken = count_taken + 1
                idx = idx + 1


            res.append(sum_top_x)
        
        return res

