class Solution:
    def countCharacters(self, a: List[str], c: str) -> int:
        p = [0]*26
        for i in c:
            p[ord(i)-ord('a')] += 1
        
        def fun(a, p):
            q = [0]*26
            for i in a:
                q[ord(i)-ord('a')] += 1
            
            for i in range(26):
                if q[i] > p[i]: return False
            return True

        
        ans = 0
        for i in a:
            if fun(i, p):
                ans += len(i)
        return ans