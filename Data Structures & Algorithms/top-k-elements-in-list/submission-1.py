class Solution:
    def topKFrequent(self, nums: List[int], kk: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) + 1
        keys  = list(d.keys())
        val = list(d.values())
        sorted_index  = sorted(range(len(val)), key=lambda k:val[k])
        keys = [keys[k] for k in sorted_index]
        val  = [val[k] for k in sorted_index]
        return keys[len(keys)-kk : len(keys)]
        