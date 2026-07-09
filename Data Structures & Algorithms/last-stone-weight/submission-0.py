class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        # Pop the two largest (they are negative at the root)
        largest = 0
        second_largest = 0
        diff = 0

        while len(maxHeap) > 1:
            largest = -heapq.heappop(maxHeap)
            second_largest = -heapq.heappop(maxHeap)
            diff = largest - second_largest

            if diff == 0:
                continue
            heapq.heappush(maxHeap, -diff)
        return -maxHeap[0] if maxHeap else 0