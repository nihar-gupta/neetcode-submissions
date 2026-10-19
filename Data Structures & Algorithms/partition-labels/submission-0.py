class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        n = len(s)
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = [i,i]
            else:
                d[s[i]] = [d[s[i]][0], i]
        
        #print(d)
        a = list(d.values())
        #print(a)

        groups = []

        n = len(a)
        for i in range(n):
            merged = False

            j = 0
            while j<len(groups):

                if a[i][0] < groups[j][0] and a[i][1] > groups[j][0] and a[i][1] < groups[j][1]:
                    merged = True
                    groups[j][0] = min(groups[j][0], a[i][0])
                    groups[j][1] = max(groups[j][1], a[i][1])
                    break 
                elif a[i][0] > groups[j][0] and a[i][0] < groups[j][1] and a[i][1] > groups[j][1]:
                    merged = True
                    groups[j][0] = min(groups[j][0], a[i][0])
                    groups[j][1] = max(groups[j][1], a[i][1])
                    break
                elif a[i][0] > groups[j][0] and a[i][1] < groups[j][1]:
                    merged = True
                    groups[j][0] = min(groups[j][0], a[i][0])
                    groups[j][1] = max(groups[j][1], a[i][1])
                    break
                elif a[i][0] < groups[j][0] and a[i][1] > groups[j][1]:
                    merged = True
                    groups[j][0] = min(groups[j][0], a[i][0])
                    groups[j][1] = max(groups[j][1], a[i][1])
                    break
                
                j+=1
            if not merged:
                groups.append(a[i])
        rt = []
        for i in groups:
            rt.append(i[1]-i[0]+1)
        return rt





