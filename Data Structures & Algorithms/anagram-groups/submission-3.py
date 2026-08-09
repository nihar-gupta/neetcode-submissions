class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_into_str(a):
            p = [0]*26
            for i in a:
                p[ord(i)-ord('a')] += 1
        
            return tuple(p)

        rt_dict = dict()

        n = len(strs)
       
        for i in strs:
            cc = convert_into_str(i)
            if cc in rt_dict:
                rt_dict[cc].append(i)
            else:
                rt_dict[cc]=[i]
        
        return list(rt_dict.values())




        # def convert_to_dict(a):
        #     d = dict()
        #     for i in a:
        #         d[i] = d.get(i, 0)+1
        #     return d
        
        # def check_anagram(a, b):
        #     for key in a.keys():
        #         if key not in b or b[key] != a[key]:
        #             return False
            
        #     for key in b.keys():
        #         if key not in a or a[key] != b[key]: return False
            
        #     return True

        # n = len(strs)
        # rt = []
        # di = []

        # for i in range(n):
        #     d_curr = convert_to_dict(strs[i])

        #     found = False
        #     for j in range(len(di)):
        #         if check_anagram(di[j] , d_curr):
        #             found = True
        #             rt[j].append(strs[i])
        #             break
            
        #     if not found:
        #         di.append(d_curr)
        #         rt.append([strs[i]])

        # return rt










        # def anagrams(a,b):
        #     d = dict()
        #     for i in a:
        #         if i in d:
        #             d[i]+=1
        #         else:
        #             d[i]=1
        #     for i in b:
        #         if i in d:
        #             d[i]-=1
        #             if d[i]<0: return False
        #         else:
        #             return False
            
        #     for i in d.values():
        #         if i != 0: return False
        #     return True
                
        
        # rt = []
        
        # for st in strs:
        #     found = False
        #     for i in range(len(rt)):
        #         if anagrams(st, rt[i][0]):
        #             rt[i].append(st)
        #             found = True
        #             break
        #     if not found:
        #         rt.append([st])
        # return rt
                
        