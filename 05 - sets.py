# 01 - What a set is
# A set stores unique values
service_names: set[str] = {"api", "worker", "database"}
# Sets are useful when you need to:
# remove duplicates
# test whether a value exists
# compare a group of values
# track values you have already visited

# Sets are unordered and do not support indexing
service_names[0]  # TypeError

# 02 - Creating a Set
regions: set[str] = {"eu-west-1", "us-east-1"}
#Create an empty set with set()
regions: set[str] = set()

#Conver another iterable into a set:
deployments = ["api", "worker", "api"]
unique_deployments = set(deployments)

print(unique_deployments)
# {"api", "worker"}

# 03 - Membership testing
healthy_services: set[str] = {"api", "database"}

if "api" in healthy_services:
    print("API is healthy")

if "worker" not in healthy_services:
    print("Worker needs attention")

# Membership testing is faster in a set than a lsit

# 04 - Adding Values
# Use .add() to add one value
active_services: set[str] = {"api"}
active_services.add("worker")
# Adding an existing value does nothing

# Use update to add multiple values
active_services.update(["database", "cache"])

# 05 - Removing values
active_services.remove("worker")
# It rasies an erorr if the value is absent
active_services.remove("unknown")  # KeyError
# Use discard when the value might not exist
active_services.discard("unknown")

# 06 - Union
# A union contains every value found in either set
production_services: set[str] = {"api", "database"}
staging_services: set[str] = {"api", "worker"}

all_services = production_services.union(staging_services)
# or
all_services = production_services | staging_services

# 07 - Intersection contains the values present in both sets
required_regions: set[str] = {"eu-west-1", "us-east-1"}
available_regions: set[str] = {"eu-west-1", "ap-south-1"}

supported_regions = required_regions & available_regions
# or
supported_regions = required_regions.intersection(available_regions)

print(supported_regions)
# {"eu-west-1"}

# 08 - Difference and symmetric difference
# Difference contains values in first set but not in the second
expected_services: set[str] = {"api", "worker", "database"}
running_services: set[str] = {"api", "database"}

missing_services = expected_services - running_services

print(missing_services)
# {"worker"}

# Order matters
expected_services - running_services  # Missing services
running_services - expected_services  # Unexpected running services

# Symmetric difference contains values that appear in exactly one set
changed_services = expected_services ^ running_services

print(changed_services)
# {"worker"}

# 09 - Set comparisons
# Check whether one set is contained in another
required_permissions: set[str] = {"read", "write"}
granted_permissions: set[str] = {"read", "write", "deploy"}

if required_permissions <= granted_permissions:
    print("All required permissions are granted")

# Useful Operators
a <= b  # a is a subset of b
a < b   # a is a proper subset of b
a >= b  # a is a superset of b
a > b   # a is a proper superset of b

# A proper subset must be smaller
{"read"} < {"read", "write"}   # True
{"read"} < {"read"}            # False
{"read"} <= {"read"}           # True

# Check whether two sets have no shared values
if production_hosts.isdisjoint(test_hosts):
    print("The environments are isolated")

# 10 - Looping and hashable values
failed_services: set[str] = {"api", "worker"}

for service in failed_services:
    print(service)

# Values stored in set must be immutable, so no lists/dictionaries/sets
"""
A recursive functio needs
1. A base case that stops recursion
2. A recursive call that moves towards the base case
3. A returned or accumulated result
"""

def factorial(number: int) -> int:
    if number <= 1:
        return 1

    return number * factorial(number - 1)

# Each call has it's own local variables
"""
factorial(4)
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1
"""

# 08 - Base cases and progress
# A base case must cover the smallest valid problem
def sum_values(values: list[int], index: int = 0) -> int:
    if index == len(values):
        return 0

    return values[index] + sum_values(values, index + 1)

# The recursive call must move towards the base case
sum_values(values, index + 1)

# Common infinite recursion mistake
def sum_values(values: list[int], index: int = 0) -> int:
    if index == len(values):
        return 0

    return values[index] + sum_values(values, index) #Index is never changing

# Also ensure the base case handles empty input
sum_values([])
# 0

# 09 - Returning recursive results
# A recursive call's result must be returned or used
# The final recursive result is discard so the function can return None
# Example
def contains(values: list[int], target: int, index: int = 0) -> bool:
    if index == len(values):
        return False

    if values[index] == target:
        return True

    return contains(values, target, index + 1)

# A common tree pattern is to combine returned results
def tree_height(node) -> int:
    if node is None:
        return 0

    left_height = tree_height(node.left)
    right_height = tree_height(node.right)

    return 1 + max(left_height, right_height)

# 10 Recursive state and common bugs
# Recursive state can be managed in two ways
# Pass state as arguments
def dfs(
    node: int,
    graph: dict[int, list[int]],
    visited: set[int],
) -> None:
    if node in visited:
        return

    visited.add(node)

    for neighbour in graph.get(node, []):
        dfs(neighbour, graph, visited)

# Capture state in a nested helped (Preferred for Leetcode)
def count_nodes(graph: dict[int, list[int]], start: int) -> int:
    visited: set[int] = set()

    def dfs(node: int) -> None:
        if node in visited:
            return

        visited.add(node)

        for neighbour in graph.get(node, []):
            dfs(neighbour)

    dfs(start)
    return len(visited)

"""
Common bugs
- forgetting the base case
- failing to move toward the base case
- forgetting return before a recursive call
- marking graph nodes visited too late
- sharing mutable state accidentally
- modifying a path without undoing it during backtracking
"""

