# 01 - What heapq provides
# Python's heapq module implements a min-heap using a normal list
# The smallest value is always at index 0
import heapq

latencies: list[int] = [250, 90, 180, 40]

heapq.heapify(latencies)

print(latencies[0])
# 40

# The list is now a valid heap, but it is not fully sorted
print(latencies)
# Possible result: [40, 90, 180, 250]

# Do not rely on the internal list order beyond
heap[0]  # Smallest item
# heapify() modifies the list in place

# 02 - Adding and removing values
# Add a value with heappush()
heap: list[int] = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 12)

# Remove and return the smallest value
smallest: int = heapq.heappop(heap)
# 5

# Inspect the smallest value without removing it
smallest: int = heap[0]

# Typical pattern
while heap:
    value = heapq.heappop(heap)
# Calling heappop() or accessing heap[0] on an empty heap raises IndexError.

# 03 - Storing tuples for priorities
# Heap elements can be tuples
deployment_queue: list[tuple[int, str]] = []

heapq.heappush(deployment_queue, (3, "payments"))
heapq.heappush(deployment_queue, (1, "api"))
heapq.heappush(deployment_queue, (2, "authentication"))

# Python compare tuples from left to right
priority, service_name = heapq.heappop(deployment_queue)

print(priority, service_name)
# 1 api

# This is the usual priority-queue pattern
heapq.heappush(heap, (priority, value))
priority, value = heapq.heappop(heap)

# For equal priorties, Python compare the second tuple item
(1, "api") < (1, "payments")

# This can cause an error if the second values are not comparable
# A safe pattern is to include a unique counter
heapq.heappush(heap, (priority, sequence_number, value))
# Then ties are resolved using sequence_number

# 04 - Max-heaps using negative values
# heapq is a min-heap, for coding questions requiring a max-heap, negate numeric values
numbers: list[int] = [10, 30, 20]

max_heap: list[int] = []

for number in numbers:
    heapq.heappush(max_heap, -number)

# Remove the largest original number
largest: int = -heapq.heappop(max_heap)
# 30

# For priority updates
heapq.heappush(heap, (-priority, service_name))

negative_priority, service_name = heapq.heappop(heap)
priority = -negative_priority

# For priority tuples
heapq.heappush(heap, (-priority, service_name))

negative_priority, service_name = heapq.heappop(heap)
priority = -negative_priority

# Common mistake
heapq.heappush(max_heap, -number)

largest = heapq.heappop(max_heap)

# largest is still negative. Negate again when popping
largest = -heapq.heappop(max_heap)

# 05 Useful heap operations and common mistakes
# Find the smallest or largest few values
numbers: list[int] = [40, 10, 70, 20, 90]

smallest_three: list[int] = heapq.nsmallest(3, numbers)
largest_two: list[int] = heapq.nlargest(2, numbers)

# Results
smallest_three
# [10, 20, 40]

largest_two
# [90, 70]
# These are convenient when k is relatively small

# Replace the smallest value
removed: int = heapq.heapreplace(heap, new_value)
# This removes the smallest item and then adds the new item
# A more commonly useful combined operation is
removed: int = heapq.heappushpop(heap, new_value)

# A more commonly useful combined operation is
removed: int = heapq.heappushpop(heap, new_value)
# It pushes the new value and then removes the smallest

# For interview prep the essential operations are usually:
heapq.heapify(heap)
heapq.heappush(heap, value)
heapq.heappop(heap)
heap[0]

"""
Common mistakes:
- Assuming the heap list is fully sorted.
- Forgetting that Python uses a min-heap.
- Forgetting to negate values when popping from a simulated max-heap.
- Sorting the heap after every insertion, which defeats the purpose of using a heap.
"""