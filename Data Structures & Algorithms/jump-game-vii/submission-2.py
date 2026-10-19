class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)
        if s[-1] == "1": return False
        reach = [False for i in range(n)]

        reach[0] = True 

        for i in range(n):
            if s[i] == "0" and reach[i]:
                for j in range(min(i+minJump, n), min(i+maxJump+1, n)):
                    reach[j] = True 
                    if reach[-1]:
                        return True 
        
        if reach[-1]: return True 
        return False

        