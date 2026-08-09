class Solution:
    def canPlaceFlowers(self, a: List[int], c: int) -> bool:

        if len(a) == 1 and a[0]==0 and c==1: return True
        n=len(a)
        for i in range(len(a)):
            if c<=0: return True
            if a[i] == 0:
                if i==0:
                    if i+1<n and a[i+1]==0:
                        a[i] = 1
                        c -= 1
                elif i==len(a)-1:
                    if i-1>=0 and a[i-1]==0:
                        a[i] = 1
                        c -= 1
                else:
                    if i+1<n and a[i+1]==0 and i-1>=0 and a[i-1]==0:
                        a[i]=1
                        c-=1
        if c<=0: return True
        return False



        