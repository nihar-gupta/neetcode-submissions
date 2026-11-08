class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(s, i, j, wordDict):
            nonlocal dd 
            if j == len(s):
                if i+1 == j: 
                    rt = True
                elif s[i+1:] in wordDict:
                    rt = True
                else:
                    rt = False
            else:
                if i in dd and j in dd: return dd[i][j]
                if s[i+1:j+1] in wordDict:
                    rt = solve(s, j, j+1, wordDict) or solve(s, i, j+1, wordDict)
                else:
                    rt = solve(s, i, j+1, wordDict)
            if i not in dd: 
                dd[i] = dict()
            if j not in dd[i]:
                dd[i][j] = False 

            dd[i][j] = rt 
            return rt 

        

        wordDict = set(wordDict)
        dd = dict()
        return solve(s, -1, 0, wordDict)

        