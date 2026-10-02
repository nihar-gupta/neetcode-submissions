class TimeMap:

    def __init__(self):
        self.d = dict()
        
    def do_sort(self, a):
        curr = len(a) - 1
        prev = curr - 1
        while prev >=0 and a[prev] > a[curr]:
            a[prev] , a[curr] = a[curr], a[prev]
            prev -= 1
            curr -= 1
        return a

        





    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = dict()
            self.d[key]["niharValue"] = None
            
        self.d[key][timestamp] = value
        if self.d[key]["niharValue"] == None:
            self.d[key]["niharValue"] = [timestamp]
        else:
            self.d[key]["niharValue"].append(timestamp)
            self.d[key]["niharValue"] = self.do_sort(self.d[key]["niharValue"])
            


    def get_sml_value(self, a, target):
        low = 0
        high = len(a)-1
        ans = None
        while low<=high:
            mid = (low+high)//2
            if a[mid] == target:
                return mid 
            elif a[mid] > target:
                high = mid-1
            else:
                ans = mid
                low = mid+1
        return ans

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d and timestamp in self.d[key]:
            return self.d[key][timestamp]
        elif key in self.d and self.d[key]["niharValue"] != None:
            valll = self.get_sml_value(self.d[key]["niharValue"], timestamp)

            if valll != None:
                return self.d[key][ self.d[key]["niharValue"][valll] ]
        return ""
        
