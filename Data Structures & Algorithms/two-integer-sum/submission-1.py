class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we first create a dictionary that would hold the ints and its indexes
        num_map = {}

        # using enumerate() returns the list with its indexes
        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in num_map:
                return [num_map[compliment], i]
            num_map[n] = i
        return []