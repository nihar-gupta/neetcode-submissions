class Solution:
    def removeElement(self, a: List[int], v: int) -> int:

        i=0
        n = len(a)
        j=0

        c=0
        while i<n:
            if a[i] != v:
                c+=1
                a[j]=a[i]
                j+=1
            i+=1
        return c


        