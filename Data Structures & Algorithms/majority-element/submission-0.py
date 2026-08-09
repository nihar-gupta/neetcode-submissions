class Solution:
    def majorityElement(self, a: List[int]) -> int:

        me = a[0]
        c = 1
        for i in range(1, len(a)):
            if a[i] == me: c+=1
            else:
                c-=1
                if c<=0: me = a[i]
        return me
        