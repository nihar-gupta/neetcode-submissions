class Solution:
    def reverseBits(self, n: int) -> int:
        
        bits = 31
        curr = 0
        ans = 0
        while curr <= 32:
            if n&(1<<curr) != 0:
                # set 
                ans = ans|(1<<(bits-curr))
            curr += 1
        return ans
        