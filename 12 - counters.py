# 01 - Counter for frequency counting
# Counter is a dictionary-like type designed for counting hashable values
from collections import Counter

service_names: list[str] = ["api", "auth", "api", "payments", "api"]

counts: Counter[str] = Counter(service_names)

# Result
Counter({
    "api": 3,
    "auth": 1,
    "payments": 1,
})

# Access counts like a dictionary
api_count: int = counts["api"]
# 3

# Unlike a normal dictionary, a missing key returns 0
worker_count: int = counts["worker"]
# 0

# This avoid needing
counts.get("worker", 0)

# 02 - Common Counter interview patterns
# Count characters
character_counts: Counter[str] = Counter("deployment")

# Compare frequencies
# Useful for anagram-style questions
def is_anagram(first: str, second: str) -> bool:
    return Counter(first) == Counter(second)

# Find the most common values
counts: Counter[str] = Counter(
    ["api", "auth", "api", "payments", "api", "auth"]
)

most_common: list[tuple[str, int]] = counts.most_common(2)

# Result
[("api", 3), ("auth", 2)]

# For the single msot common item
value, frequency = counts.most_common(1)[0]

# Updating and reducing counts
# Increment normally
counts["api"] += 1

# Count additional items
counts.update(["api", "worker", "api"])

# Reduce counts
counts.subtract(["api", "auth"])

# Counter values can become zero or negative
counts["missing"] -= 1
# -1

# To keep only positive counts
counts = +counts

# 04 - defaultdict for automatic default values
# A defaultdict creates a default value when a missing key is accessed
from collections import defaultdict

service_ports: defaultdict[str, list[int]] = defaultdict(list)

# Now this works without checking whether the key exists
service_ports["api"].append(443)
service_ports["api"].append(8443)
service_ports["payments"].append(443)

# Preferred for grouping
groups: defaultdict[str, list[str]] = defaultdict(list)

# Preferred for counting when you do not want counter
counts: defaultdict[str, int] = defaultdict(int)

for service_name in service_names:
    counts[service_name] += 1

# 05 - Common mistakes and choosing between them
# Use counter when the primary task is frequency counting
counts = Counter(values)

# Use defaultdict(list) when grouping values
groups[key].append(value)

# Use defaultdict(set) when grouping unique values
dependencies[service].add(dependency)

# For defaultdicts, simply accessing a missing key creates it