class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        for i in allowed:
            s.add(i)
        
        c = 0
        for word in words:
            found = True
            for i in word:
                if i not in s:
                    found = False
                    break
            if found:
                c+=1
        return c
        