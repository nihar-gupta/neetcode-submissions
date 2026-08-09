class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()

        if len(s) != len(t) : return False


        for i in range(len(s)):
            
            if s[i] in d and d[s[i]] != t[i]: return False
            #if t[i] in d and d[t[i]] != s[i]: return False
            #if t[i] in d and d[t[i]] 

            d[s[i]] = t[i]
            #d[t[i]] = s[i]


        d=dict()
        for i in range(len(t)):
            if t[i] in d and d[t[i]] != s[i]: return False
            d[t[i]]=s[i]
        return True



            # if s[i] != t[i]:
            #     if s[i] in d:
            #         if d[s[i]] != t[i]: return False
            #     else:
            #         d[s[i]]=t[i]
            # else:
            #     if s[i] in d and d[s[i]] != t[i]: return False
            #     d[s[i]] = t[i]
            #     d[t[i]] = s[i]
        

        # d = dict()
        # for i in range(len(t)):
        #     if s[i] != t[i]:
        #         if t[i] in d:
        #             if d[t[i]] != s[i]: return False
        #         else:
        #             d[t[i]]=s[i]
        # return True
        