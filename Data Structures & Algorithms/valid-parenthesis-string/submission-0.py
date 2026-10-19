class Solution:
    def checkValidString(self, s: str) -> bool:
        min_range = 0
        max_range = 0

        for i in s: 
            if i == '(':
                # stright forware +1 case
                min_range += 1
                max_range += 1

            elif i == ")":
                # stright forware -1 case
                min_range -= 1
                max_range -= 1

            else:
                min_range -= 1
                max_range += 1

            if max_range < 0:
                return False

            if min_range < 0:
                min_range = 0

        if min_range == 0:
            return True 
        return False
        