class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for num in nums:
            if num in freq_map:
                return True
            freq_map[num] = 1

        return False