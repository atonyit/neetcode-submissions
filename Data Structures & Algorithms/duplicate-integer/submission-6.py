class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        #input values into the set, compare the original list length to the set length

        for num in nums:
            my_set.add(num)

        return len(my_set) != len(nums)