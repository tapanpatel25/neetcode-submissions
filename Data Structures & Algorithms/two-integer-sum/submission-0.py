class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            diff = target- nums[i]
            if diff in d:
                return[d[diff],i]
            d[nums[i]] = i
        return []

        