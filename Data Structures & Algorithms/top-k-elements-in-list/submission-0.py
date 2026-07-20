class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        mostFrequent = []
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        heapq.heapify(mostFrequent)

        for key, value in frequency.items():
            heapq.heappush(mostFrequent, (value, key))
        
        for i in range(len(mostFrequent) - k):
            heapq.heappop(mostFrequent)
        
        keys = [y for x, y in mostFrequent]
        return keys