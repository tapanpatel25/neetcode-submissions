class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 
        
        sortedelem = sorted(nums)
        long_streak = cur_streak = 1

        for i in range(1,len(sortedelem)):
            
            if sortedelem[i] == sortedelem[i-1]:
                continue
            
            if sortedelem[i] - sortedelem[i-1] == 1:
                cur_streak += 1
            else:
                long_streak = max(cur_streak,long_streak)
                cur_streak = 1
        
        return max(long_streak,cur_streak)


