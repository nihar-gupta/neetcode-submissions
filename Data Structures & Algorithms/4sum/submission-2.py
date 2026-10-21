# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

#         def solve(a, p1, p2, target):
#             while p1<p2:
#                 k = a[p1] + a[p2]
#                 if k == target:
#                     return a[p1], a[p2]
#                 elif k > target:
#                     p2 -= 1
#                 else:
#                     p1 += 1
#             return None, None


#         nums.sort()
#         rt = set()
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):

#                 p1, p2 = solve(nums, j+1, n-1, target - nums[i] - nums[j])
#                 if p1 != None:
#                     rt.add((nums[i], nums[j], p1, p2))
#         return list(rt)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = (
                        nums[i] + nums[j]
                        + nums[left] + nums[right]
                    )

                    if total == target:
                        result.append([
                            nums[i], nums[j],
                            nums[left], nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate third elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate fourth elements
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

        