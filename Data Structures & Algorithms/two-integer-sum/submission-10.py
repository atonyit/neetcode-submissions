class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            #is target - nums[i] in mp
            if target - nums[i] in mp:
                return [mp[target-nums[i]], i]
            
            #add to hasmap
            mp[nums[i]] = i
            # key = number, value = index


            