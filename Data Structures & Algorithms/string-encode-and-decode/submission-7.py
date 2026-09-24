class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "GupTa"
        for i in range(len(strs)):
            if strs[i] == "":
                strs[i] = "NihAr"
        return "GupTa".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == "GupTa": return []
        s = s.split("GupTa")
        for i in range(len(s)):
            k = s[i]
            k=k.replace("NihAr", "")
            s[i] = k
        return s
