# 01 - What a tuple is
# stores an ordered collection of values
deployment: tuple[str, str, int] = ("payments-api", "production", 3)
# Tuples preserve order, allow duplicates, can contain different types, are immutable

# 02 - Tuples versus lsit
# List when values may change, tuple when values represent a fixed group
coordinate: tuple[int, int] = (4, 7)
version: tuple[int, int, int] = (3, 12, 1)

# 03 - Creating tuples
services: tuple[str, str] = ("api", "worker")
#Empty Tuple
empty_tuple: tuple[()] = ()

# 04 - Single-item tuples
# A single item tuple requires a trailing comma
service: tuple[str] = ("api",)

# 05 - Indexing and slicing is just like lists
deployment = ("api", "production", 3)

deployment[0]   # "api"
deployment[-1]  # 3
deployment[:2]  # ("api", "production")

# 06 - Tuples are immutable
# You cannot replace, add or remove tuple items
deployment: tuple[str, str, int] = ("api", "production", 3)

deployment[2] = 5
# TypeError

#Create a new tuple instead
updated_deployment = ("api", "production", 5)

# 07 - Useful Built-ins and methods
statuses: tuple[str, ...] = ("running", "failed", "running")

len(statuses)              # 3
"failed" in statuses       # True
statuses.count("running")  # 2
statuses.index("failed")   # 1
#index() raises ValueError if the value is missing

# 08 - Iterating and unpacking
# Iteration is just like a list
services: tuple[str, ...] = ("api", "worker", "database")

for service in services:
    print(service)

# 09 - Unpacking assigns each value to a variable
deployment = ("api", "production", 3)

service, environment, replicas = deployment
# The number of variables must match the number of values

# 09 - Useful LeetCode Patterns
# Return multiple values
def get_bounds(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)

lowest, highest = get_bounds([4, 1, 9])

# Dictionary keys and set values
visited: set[tuple[int, int]] = set()

visited.add((0, 0))
visited.add((0, 1))

if (0, 1) in visited:
    print("Already visited")