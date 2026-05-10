class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input values into the set, compare the original list length to the set length

        return len(set(nums)) != len(nums)