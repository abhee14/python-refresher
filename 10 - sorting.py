# sorted()
# Returns a new list and leaves the original collection unchanged
service_names: list[str] = ["payments", "api", "authentication"]

sorted_names: list[str] = sorted(service_names)

print(sorted_names)
# ['api', 'authentication', 'payments']

# sorted() accepts any iterable but always returns a list:
ports: set[int] = {443, 22, 80}

sorted_ports: list[int] = sorted(ports)
# [22, 80, 443]

# .sort() sorts an existing list in place and returns none
service_names.sort()

# 02 - Ascending and descending order
# Ascending order is the default
latencies: list[int] = [250, 90, 180]

latencies.sort()
# [90, 180, 250]

# use reverse=True for descending order
latencies.sort(reverse=True)
# [250, 180, 90]

# 03 - Sorting with key=
# key= specifies the value Python should use
# Sort strings by lingth
service_names: list[str] = ["api", "authentication", "payments"]

by_length: list[str] = sorted(service_names, key=len)
# ['api', 'payments', 'authentication']

# Python calls the key function once for each element
key_value = len(service_name) # The orignal elements are returned the key values are only used for ordering

# Using a lambda
# A lambda is a small anonymous function
numbers: list[int] = [-10, 3, -2, 7]

by_absolute_value: list[int] = sorted(
    numbers,
    key=lambda number: abs(number),
)
# [-2, 3, 7, -10]

# Prefer an existing function when one already expresses the key clearly:
sorted(service_names, key=len)  # Preferred
#over
sorted(service_names, key=lambda name: len(name))

# 04 - Sorting structured data
# For tuples or lists a key can select a particular field
services: list[tuple[str, int]] = [
    ("payments", 250),
    ("api", 90),
    ("authentication", 180),
]

by_latency = sorted(services, key=lambda service: service[1])

# Result
[
    ("api", 90),
    ("authentication", 180),
    ("payments", 250),
]

# Multiple Sorting Criteria
# Return a tuple from the key function
incidents: list[tuple[str, int]] = [
    ("api", 2),
    ("payments", 1),
    ("authentication", 2),
]

ordered = sorted(
    incidents,
    key=lambda incident: (incident[1], incident[0]),
)

# Python compares key tuples from left to right
# 1 - Sort by severity
# 2 - Break ties using the service name

# To sort one numeric field descending while the other remains ascending, negate the descending numeric field
ordered = sorted(
    incidents,
    key=lambda incident: (-incident[1], incident[0]),
)

# 05 - Python-specific behaviour and common mistakes
# Python sorting is stable, elements with equal keys retain their original relative order
deployments = [
    ("api", "failed"),
    ("payments", "passed"),
    ("authentication", "failed"),
]

ordered = sorted(deployments, key=lambda deployment: deployment[1])
# The two failed deployments remin in their original order

# Do not mix incomparable types such as strings and integers
sorted([10, "20"])  # TypeError

# String sorting is lexicographical and case-sensitive
sorted(["api", "Payments", "auth"])
# ['Payments', 'api', 'auth']

#For case-insensitive sorting
sorted(["api", "Payments", "auth"], key=str.lower)