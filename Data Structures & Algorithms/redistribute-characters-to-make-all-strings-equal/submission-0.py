class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = dict()
        for word in words:
            for char in word:
                d[char] = d.get(char, 0) + 1
        
        n=len(words)
        for i in d.values():
            if i%n != 0: return False
        return True
        