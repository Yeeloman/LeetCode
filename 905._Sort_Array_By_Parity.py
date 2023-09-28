"""ttsp"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new_list = []
        for i, num in enumerate(nums):
            if nums[i] % 2 == 0:
                new_list = [nums[i]] + new_list
            elif nums[i] % 2 == 1:
                new_list = new_list + [nums[i]]
        return new_list
