class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m-1
        p2 = n-1
        p3 = len(num1) - 1

        while p1>=0 and p2>=0:

            if num1[p1] > num2[p2]:
                num1[p3] = num1[p1]
                p1-=1
            else:
                num1[p3] = num2[p2]
                p2 -=1
            p3-=1
        
        while p1>=0:
            num1[p3] = num1[p1]
            p1-=1
            p3-=1
        while p2>=0:
            num1[p3] = num2[p2]
            p2-=1
            p3-=1
        return num1
        