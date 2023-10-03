class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = {}
        good_pairs = 0
        for num in nums:
            if num in num_count:
                good_pairs += num_count[num]
                num_count[num] += 1
            else:
                num_count[num] = 1
        return good_pairs
