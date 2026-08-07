# 01 Function syntax and return type
# General form
def function_name(parameter: type) -> return_type:
    ...
# Example
def find_max(values: list[int]) -> int:
    return max(values)

# Type hints are not enforced at runtime
# A function without an explicit return outputs None

# 02 Parameters and arguments
# Python supports positional and keyword arguments
def search(values: list[int], target: int) -> int:
    ...

search([1, 2, 3], 2)
search(values=[1, 2, 3], target=2)

# Default parameteres
def traverse(values: list[int], start: int = 0) -> None:
    ...

# Required parameters always come before default parameters
def traverse(values: list[int], start: int = 0) -> None:
    ...

# 03 - Returning Multiple Values
# Python returns multiple values as a tuple
def find_bounds(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)

# You can unpack the result
smallest, largest = find_bounds([4, 1, 8])

# 04 - Mutation and object references
# Python passes references to objects
# A function can mutate a list passed into it:
def add_service(services: list[str]) -> None:
    services.append("api")

services: list[str] = []
add_service(services)

print(services)
# ["api"]

# Reassigning the local parameter does not replace the caller's variable
def reset_services(services: list[str]) -> None:
    services = [] # Original list is unchanged

# This mutates the original list, it is generally preferred to return a new item
def reset_services(services: list[str]) -> None:
    services.clear()

# 05 - Avoid mutable default arguments
# Do not use a mutable object as a default argument
def collect(value: int, values: list[int] = []) -> list[int]:
    values.append(value)
    return values

# The same list is reused across calls
collect(1)  # [1]
collect(2)  # [1, 2]

# Preferred
def collect(value: int, values: list[int] | None = None,) -> list[int]:
    if values is None:
        values = []

    values.append(value)
    return values

# Generally create a mutable collection outside the helper or use None

# 06 - Local scope and nonlocal
# Variables created inside a function are local to that function
def count_values(values: list[int]) -> int:
    count = 0

    for _ in values:
        count += 1

    return count

# A nested function can read variables from its outer function
def search(values: list[int], target: int) -> bool:
    found = False

    def check(value: int) -> None:
        if value == target:
            print(found)  # Reading is allowed

# To reassign an outer variable use nonlocal
def count_even(values: list[int]) -> int:
    count = 0

    def check(value: int) -> None:
        nonlocal count

        if value % 2 == 0:
            count += 1

    for value in values:
        check(value)

    return count

# You do not need nonlocal when mutating an outer collection
result: list[int] = []

def add_value(value: int) -> None:
    result.append(value)

# 07 - Basic recursion structure
