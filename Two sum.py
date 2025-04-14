from itertools import combinations
class Solution:
    def twosum(self, nums,target):
        index_combs = combinations(range(len(nums)),2)
        # result = [((i, j), (nums[i], nums[j])) for i, j in index_combs]
        for i,j in index_combs:
            if nums[i]+nums[j] == target:
                return [i,j]
                break
s = Solution()
print(s.twosum([2,7,11,15],9))
