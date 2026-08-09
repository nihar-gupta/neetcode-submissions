class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        self.pre = []
        c = 0
        for i in range(len(nums)):
            c = c + nums[i]
            self.pre.append(c)

    def sumRange(self, left: int, right: int) -> int:
        if left > right: return None
        c = self.pre[right]
        if left > 0: c = c - self.pre[left-1]
        return c
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)