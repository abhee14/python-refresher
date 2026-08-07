# 01 - Division, floor division and modulo
7 / 2   # 3.5
7 // 2  # 3
7 % 2   # 1

# / ALWAYS returns a float
# use // when you need integer-style division
# // rounds down, not towards zero
-7 // 2  # -4
-7 % 2  # 1

# 02 - Comparison Chaining
if 0 <= index < len(values):
    print(values[index])

# This is prefferred over
if index >= 0 and index < len(values):
    ...

# You can chain several comparisons
if left <= middle <= right:
    ...

# Check whether three items are equal
if a == b == c:
    ...

# 03 - Equality vs. identity
# use == to compare values
if current_value == target:
    ...

# use is primary for None
if result is None:
    ...
# Preferred
if result is not None:
    ...

# Do not use is for strings or numbers

# 04 - Truthiness and empty collections
# These values are treated as false:
False
None
0
0.0
""
[]
{}
set()

# This allows for concise checks
if not values:
    return 0

# 05 - and, or and conditional expressions
if node is not None and node.value == target:
    ...
# The second condition runs only when the first is true

# and/or return operants, not neccessarily bool
"" or "default"   # "default"
"api" or "worker" # "api"

0 and 10          # 0
5 and 10          # 10

# This makes defaulting possible
display_name = provided_name or "unknown"

# Short conditional (ternary)
# result = value_if_true if condition else value_if_false
status = "healthy" if error_count == 0 else "failed"

# 06 - range() and index-based loops
# range(start, stop, step) generates integers from 0 up to, but not including stop
for index in range(len(values)):
    print(index, values[index])

# Useful forms:
range(n)             # 0 to n - 1
range(start, stop)   # start to stop - 1
range(start, stop, step)

# Prefer direct iteration where possible
for value in values:
    print(value)

# enumerate() and zip()
# Use enumerate when you need both index and value
for index, value in enumerate(values):
    print(index, value)

# Start counting from another value
for position, service in enumerate(services, start=1):
    print(position, service)

# Use zip() to iterate over multiple collections together
for expected, actual in zip(expected_values, actual_values):
    if expected != actual:
        return False

# zip() stops when the shortest collection ends
list(zip([1, 2, 3], ["a", "b"]))
# [(1, "a"), (2, "b")]

# 08 - Reverse Iteration
# Use reversed() when you need values in reverse order:
for value in reversed(values):
    print(value)

# For a reversed copy
reversed_values = values[::-1]

# 09 - while, break and continue
# while is common for two points, binary search, and repeated processing
left = 0
right = len(values) - 1

while left < right:
    if values[left] == values[right]:
        left += 1
        right -= 1
    else:
        return False

# Use break to exit the nearest loop:
for value in values:
    if value == target:
        result = value
        break

# Use continue to skip to the next iteration
for value in values:
    if value < 0:
        continue

    process(value)

# 10 - Mutation and iteration mistakes
# Do not remove items while iterating over it
# Create a filtered list
values = [value for value in values if value >= 0]