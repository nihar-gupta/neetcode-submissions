class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #your code goes here
        def helper(d):
            mm = 0
            kk = 0
            for key, val in d.items():
                if val > mm: 
                    mm = val 
                    kk = key 
            return kk, mm


        ma = 0
        d = dict()
        n = len(s)
        j = 0
        for i in range(n):
            d[s[i]] = d.get(s[i], 0)+1

            # check valid d 
            while True:
                key, value = helper(d)
                total_length = i-j+1
                if total_length - value > k:
                    d[s[j]]-=1
                    if d[s[j]] == 0:
                        d.pop(s[j])
                    j+=1
                else:
                    break 
            
            ma = max(ma, i-j+1)
        return ma





        

        

        