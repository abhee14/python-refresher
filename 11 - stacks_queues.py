# 01 - Stacks with lists
# A stack uses last in, first out behaviour
# Stacks are implemented with lists in python
stack: list[str] = []

stack.append("build")
stack.append("test")
stack.append("deploy")

# Remove and return the most recendly added item
current_stage: str = stack.pop()
# "deploy"

# Read the top item without removing it
top_stage: str = stack[-1]

# Check before accessing or removing
if stack:
    current_stage = stack.pop() # Using pop on an empy list will cause IndexError


# 02 - Queues should not normally use lists
# A queue uses first in, first out behaviour
# Use collections.deque
# from collections import deque


# 03 - Queues with deque
from collections import deque

queue: deque[str] = deque()

# Add to the right
queue.append("api")
queue.append("payments")

# Remove from the left
service: str = queue.popleft()

# Typical queue pattern:
while queue:
    current = queue.popleft()

# Core queue operations:
queue.append(value)       # Add to right
queue.popleft()           # Remove from left
queue[0]                  # Inspect leftmost item

# Using both ends of a deque
# A deque supports efficient operations at either end
values: deque[int] = deque([2, 3])

values.append(4)
values.appendleft(1)

# deque([1, 2, 3, 4])

# Remove it from either end
right_value: int = values.pop()
left_value: int = values.popleft()

# Useful Operations
values.append(value)
values.appendleft(value)

values.pop()
values.popleft()

# A deque can also represent a stack
stack: deque[int] = deque()

stack.append(10)
stack.append(20)

latest = stack.pop()

# Generally however use lists for stack

# 05 - Common interview patterns and mistakes
# Stack Pattern
stack: list[str] = []

for item in items:
    stack.append(item)

while stack:
    item = stack.pop()

# Queue or BFS pattern
queue: deque[int] = deque([start])

while queue:
    current = queue.popleft()

# Common mistakes
queue.pop() # This removes from the right, giving stack-like behaviour

# For a FIFO queue use
queue.popleft()

# When processing BFS one level at a time, capture level size before modifying queue
level_size = len(queue)

for _ in range(level_size):
    current = queue.popleft()