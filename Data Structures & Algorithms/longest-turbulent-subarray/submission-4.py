class Solution:
    def maxTurbulenceSize(self, a: List[int]) -> int:

        if len(a) <= 1: return len(a)

        mc = 1
        c = 1
        i = 1
        n = len(a)
        sign = None
        while i<n:
            if a[i] < a[i-1]:
                # decreasing 
                if sign == None:
                    c += 1
                    sign = 'dec'
                elif sign == 'inc':
                    c += 1
                    sign = 'dec'
                else:
                    c = 2
                mc = max(mc, c)
            elif a[i] > a[i-1]:
                # increasing 
                if sign == None:
                    sign = 'inc'
                    c += 1
                elif sign == 'dec':
                    sign = 'inc'
                    c += 1
                else:
                    c = 2
                mc = max(mc, c)
            else:
                c = 1
                sign = None

            i+=1
        return mc




        
        # mc = 1
        # c = 1
        # n = len(a)
        # sign = None
        # for i in range(1,n):
        #     if sign == None:
        #         if a[i] > a[i-1]:
        #             sign = 'inc'
        #             c += 1
        #         elif a[i] < a[i-1]:
        #             sign = 'dec'
        #             c += 1
        #         else:
        #             sign = None 
        #             c=1
        #         mc = max(mc, c)
        #     else:
        #         if a[i] > a[i-1]:
        #             if sign == 'inc':
        #                 c = 1
        #             elif sign == 'dec':
        #                 sign = 'inc'
        #                 c+=1
        #             else:
        #                 sign = 'inc'
        #                 c=1
        #             mc = max(mc, c)
        #         elif a[i] < a[i-1]:
        #             if sign == 'inc':
        #                 sign = 'dec'
        #                 c+=1
        #             elif sign == 'dec':
        #                 c=1
        #             else:
        #                 sign = 'dec'
        #                 c=1
        #             mc=max(mc, c)
        #         else:
        #             sign = None 
        #             c = 1
        # return mc


