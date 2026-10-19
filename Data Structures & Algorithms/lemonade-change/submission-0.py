class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        for i in bills:
            if i == 5:
                five +=1
            elif i==10:
                if five == 0:
                    return False
                else:
                    ten += 1
                    five -= 1
                
            else:
                if ten >= 1 and five >=1:
                    ten -= 1
                    five -= 1
                    twenty +=1
                elif five >=3:
                    five -= 3
                    twenty +=1
                else:
                    return False 
        return True
        