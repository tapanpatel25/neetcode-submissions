class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if nums[i] in track:
                return [track[nums[i]], i]
            track[diff] = i
    

        