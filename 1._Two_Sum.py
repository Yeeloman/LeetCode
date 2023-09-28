"""ttsp"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_num = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in idx_num:
                return [idx, idx_num[comp]]
            idx_num[num] = idx
        return []
