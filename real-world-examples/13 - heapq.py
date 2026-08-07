# Maintain a min-heap containing only the three largest values seen so far
import heapq


def highest_latencies(
    latencies: list[int],
    limit: int,
) -> list[int]:
    heap: list[int] = []

    for latency in latencies:
        heapq.heappush(heap, latency)

        if len(heap) > limit:
            heapq.heappop(heap)

    return sorted(heap, reverse=True)

# Example
latencies = [120, 450, 80, 300, 600, 200]

print(highest_latencies(latencies, 3))
# [600, 450, 300]

"""
The heap stores the best three candidates. 
Whenever it grows beyond size three, the smallest candidate is removed.

"""