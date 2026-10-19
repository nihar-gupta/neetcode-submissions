class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1]
        right =[1]
        n=len(ratings)
        for i in range(1,n):
            if ratings[i-1] >= ratings[i]:
                left.append(1)
            else:
                left.append(left[-1]+1)

        for i in range(n-2,-1,-1):
            if ratings[i+1] >= ratings[i]:
                right.append(1)
            else:
                right.append(right[-1]+1)
        right=right[::-1]
        su=0
        for i in range(n):
            su += max(left[i], right[i])
        return su
        