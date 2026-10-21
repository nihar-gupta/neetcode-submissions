class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(a, b):
            for key, val in b.items():
                if key not in a: return False 
                if a[key] < val: return False 
            return True


        tt = dict()
        for i in t: 
            tt[i] = tt.get(i,0)+1
        
        ss = dict()

        rt = ""
        mi = float('inf')
        found = None 

        n = len(s)
        j = 0
        for i in range(n):
            ss[s[i]] = ss.get(s[i], 0) + 1

            if check(ss, tt):

                while True:
                    ss[s[j]] -= 1
                    if ss[s[j]] == 0:
                        ss.pop(s[j])

                    if check(ss, tt):
                        j+=1
                    else:
                        ss[s[j]] = ss.get(s[j], 0)+1
                        break
                if mi > i-j+1:
                    mi = i-j+1
                    found = True 
                    rt = s[j:i+1]
        if found: return rt 
        else: return ""




        