class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        rt = 10000000000
        d =dict()
        d["b"]=0
        d["a"]=0
        d["l"]=0
        d["o"]=0
        d["n"]=0
        for i in text: 
            d[i] = d.get(i, 0)+1
        
        rt = min(rt, d["b"], d["a"], d["l"]//2, d["o"]//2, d["n"])
        return rt

        