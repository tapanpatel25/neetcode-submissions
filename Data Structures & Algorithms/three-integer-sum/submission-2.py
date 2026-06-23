class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])

                if third in seen:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                
                seen.add(nums[j])
        
        ans = list(result)
        return ans