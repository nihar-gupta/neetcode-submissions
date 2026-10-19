class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        start = n-1
        end = 0

        tank = gas[start] - cost[start]

        while start > end:
            if tank < 0:
                # we are ran out of gas 
                # so our start point is not correct 
                # we need a prior start point 
                start -= 1
                tank += (gas[start] - cost[start])
            else:
                # we still have the gas 
                # so we can still increase our end pointer so that we will go to 
                # other stations 
                tank += (gas[end] - cost[end])
                end += 1
        
        return start if tank >= 0 else -1

