class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = [0]*26
        for i in magazine:
            a[ord(i)-ord('a')] += 1
        
        b = [0]*26
        for i in ransomNote:
            b[ord(i)-ord('a')] += 1
        
        for i in range(26):
            if a[i] < b[i]: return False
        return True
        