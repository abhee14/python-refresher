"""
Useful Python Built-ins for Coding Questions

This file contains concise notes and small examples for:
- ord() and chr()
- math.inf
- enumerate() and zip()
- min(), max(), sum(), any(), and all()
- abs(), divmod(), and reversed()
"""

import math


# ---------------------------------------------------------------------------
# 1. ord() and chr()
# ---------------------------------------------------------------------------

# ord() converts one character into its Unicode integer value.
letter_code: int = ord("a")       # 97

# chr() converts a Unicode integer value back into a character.
letter: str = chr(97)             # "a"

# Convert a lowercase letter into a zero-based alphabet position.
position: int = ord("d") - ord("a")   # 3

# Convert a zero-based alphabet position back into a lowercase letter.
converted_letter: str = chr(ord("a") + position)   # "d"

# Common fixed-size frequency-array pattern for lowercase English letters.
word: str = "deployment"
letter_counts: list[int] = [0] * 26

for character in word:
    index: int = ord(character) - ord("a")
    letter_counts[index] += 1

# Common mistake:
# ord("api")  # TypeError: ord() requires a string of exactly one character.


# ---------------------------------------------------------------------------
# 2. math.inf
# ---------------------------------------------------------------------------

# Positive infinity is useful when searching for a minimum.
minimum_latency: float = math.inf

for latency in [250, 90, 180]:
    minimum_latency = min(minimum_latency, latency)

# minimum_latency is now 90.

# Negative infinity is useful when searching for a maximum.
maximum_latency: float = -math.inf

for latency in [250, 90, 180]:
    maximum_latency = max(maximum_latency, latency)

# maximum_latency is now 250.

# This is also valid:
alternative_infinity: float = float("inf")

# math.inf is normally clearer when the math module is already imported.


# ---------------------------------------------------------------------------
# 3. enumerate() and zip()
# ---------------------------------------------------------------------------

services: list[str] = ["api", "auth", "payments"]

# enumerate() provides both the index and the value.
for index, service_name in enumerate(services):
    print(index, service_name)

# Use start= when numbering should begin from another value.
for position, service_name in enumerate(services, start=1):
    print(position, service_name)

# Preferred:
for index, service_name in enumerate(services):
    pass

# Valid but usually less idiomatic:
for index in range(len(services)):
    service_name = services[index]

latencies: list[int] = [100, 250, 180]

# zip() iterates through multiple iterables together.
for service_name, latency in zip(services, latencies):
    print(service_name, latency)

# Important: zip() stops when the shortest iterable ends.
paired_values: list[tuple[int, str]] = list(
    zip([1, 2, 3], ["a", "b"])
)
# [(1, "a"), (2, "b")]


# ---------------------------------------------------------------------------
# 4. min(), max(), sum(), any(), and all()
# ---------------------------------------------------------------------------

values: list[int] = [120, 450, 80, 300]

lowest: int = min(values)     # 80
highest: int = max(values)    # 450
total: int = sum(values)      # 950

# min() and max() support key=.
longest_service: str = max(services, key=len)
# "payments"

deployments: list[tuple[str, int]] = [
    ("api", 120),
    ("payments", 300),
    ("auth", 90),
]

slowest_deployment: tuple[str, int] = max(
    deployments,
    key=lambda deployment: deployment[1],
)
# ("payments", 300)

statuses: list[str] = ["healthy", "failed", "healthy"]

# sum() can count values satisfying a condition because:
# True behaves like 1 and False behaves like 0.
failed_count: int = sum(
    status == "failed"
    for status in statuses
)
# 1

# any() is True when at least one item is truthy.
has_failure: bool = any(
    status == "failed"
    for status in statuses
)
# True

# all() is True only when every item is truthy.
all_healthy: bool = all(
    status == "healthy"
    for status in statuses
)
# False


# ---------------------------------------------------------------------------
# 5. abs(), divmod(), and reversed()
# ---------------------------------------------------------------------------

# abs() returns the absolute value.
distance: int = abs(10 - 17)   # 7

# divmod() returns quotient and remainder together.
minutes, seconds = divmod(125, 60)
# minutes == 2
# seconds == 5

numbers: list[int] = [1, 2, 3]

# reversed() returns an iterator.
for number in reversed(numbers):
    print(number)

# Convert the reverse iterator to a list when needed.
reversed_numbers: list[int] = list(reversed(numbers))
# [3, 2, 1]

text: str = "python"

# For strings, slicing is usually the clearest reversal.
reversed_text: str = text[::-1]
# "nohtyp"


# ---------------------------------------------------------------------------
# Less commonly needed in Blind 75 solutions
# ---------------------------------------------------------------------------

value: object = 10

# isinstance() checks whether a value has a given runtime type.
if isinstance(value, int):
    print("The value is an integer.")

numbers = [1, 2, 3]

# map() is valid, but a comprehension is usually clearer.
mapped_squares: list[int] = list(
    map(lambda number: number * number, numbers)
)

# Preferred:
squares: list[int] = [
    number * number
    for number in numbers
]