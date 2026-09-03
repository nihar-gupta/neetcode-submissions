class Solution:
    def isPalindrome(self, s: str) -> bool:
        al = []
        for i in range(26):
            al.append(chr(ord("A")+i))
            al.append(chr(ord("a")+i))
        
        for i in range(10):
            al.append(str(i))
        
        ss = ""
        for i in s: 
            if i in al:
                ss=ss+i
        
        i = 0
        j = len(ss)-1
        while i<j:
            if ss[i] == ss[j] or ss[i].lower() == ss[j] or ss[i]==ss[j].lower():
                pass
            else: return False
            i+=1
            j-=1
        return True

        