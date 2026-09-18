class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # by creating a heap and a dict, we can group the number and its freq
        mp = {}

        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        heap = []
        for key, value in mp.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)

        ans = []
        for arr in heap:
            ans.append(arr[1])

        return ans
        

        

        