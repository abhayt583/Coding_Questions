class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res=[]
        for i in range(1,len(mountain)-1):
            if mountain[1+i]<mountain[i]>mountain[-1+i]:
                res.append(i)
          
        return res