class Solution:
    def minOperations(self, s: str) -> int:
        cur1 = cnt1 = cnt2 = 0
        cur2 = 1
        for c in s:
            if int(c) != cur1:
                cnt1 += 1
            cur1 ^= 1

            if int(c) != cur2:
                cnt2 += 1
            cur2 ^= 1
        return min(cnt1, cnt2)
        