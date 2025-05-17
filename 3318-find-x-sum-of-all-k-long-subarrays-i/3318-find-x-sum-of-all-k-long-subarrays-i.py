

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            freq = {}

            # Count occurrences manually for the subarray nums[i:i+k]
            for j in range(i, i + k):
                num = nums[j]
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            
            # Convert dictionary to list of [count, value] pairs
            pairs = []
            for key in freq:
                pairs.append([freq[key], key])  # [count, value]

            # Manually sorting by frequency and then by value
            for a in range(len(pairs)):
                for b in range(a + 1, len(pairs)):
                    if pairs[b][0] > pairs[a][0]:  # Sort by count descending
                        pairs[a], pairs[b] = pairs[b], pairs[a]
                    elif pairs[b][0] == pairs[a][0]:  # If count is the same, sort by value descending
                        if pairs[b][1] > pairs[a][1]:
                            pairs[a], pairs[b] = pairs[b], pairs[a]

            # Compute sum of top x elements
            sum_top_x = 0
            count_taken = 0
            for pair in pairs:
                if count_taken < x:
                    sum_top_x += pair[0] * pair[1]
                    count_taken += 1
                else:
                    break

            res.append(sum_top_x)

        return res



