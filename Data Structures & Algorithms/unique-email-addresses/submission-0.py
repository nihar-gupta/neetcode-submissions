class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        c = 0 
        s = set()

        for i in emails:
            rr = i.rsplit("@",1)

            k = ""

            for j in rr[0]:
                if j == "+":
                    break
                elif j==".":
                    pass
                else:
                    k+=j
            
            new_email = k+"@"+rr[1]
            s.add(new_email)
        return len(s)


        