from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = [(-freq,num) for num,freq in count.items()]
        heapq.heapify(heap)

        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result
        