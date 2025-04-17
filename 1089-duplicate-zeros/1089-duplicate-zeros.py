class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ln=len(arr)
        new=[]
        for i in arr:
            if i==0:
                new.append(0)
            new.append(i)

        arr.clear()
        arr.extend(new[:ln])
