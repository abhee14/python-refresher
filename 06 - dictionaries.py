# 01 - A dictionary stores key-value pairs
service_ports: dict[str, int] = {
    "api": 8080,
    "database": 5432,
}

# Each key must be unique
ports = {
    "api": 8080,
    "api": 9000,
}

print(ports)
# {"api": 9000}
# The later value replaces the earlier value
# Dictionaries are especially useful for
# Mapping one value to another
# countine occurrences
# storing indexes
# caching previously calculated results
# representing graphs

# 02 - Creating a dictionary
# Create a populated dictionary
service_status: dict[str, str] = {
    "api": "healthy",
    "worker": "failed",
}

# Create an empty dictionary
service_status: dict[str, str] = {}

# 03 - Accessing Values
service_ports: dict[str, int] = {
    "api": 8080,
    "worker": 8081,
}

port = service_ports["api"]

# A missing key raises KeyError:
port = service_ports["database"]  # KeyError

# Use .get() when the key may be missing:
port = service_ports.get("database")

print(port) # None

# Provid a default value
port = service_ports.get("database", 5432)

# Preferred distinction
service_ports["api"]          # The key must exist
service_ports.get("api", 0)   # Missing keys are acceptable

# 04 - Adding and updating entries
# Assign a value using it's key
service_ports: dict[str, int] = {}

service_ports["api"] = 8080
service_ports["worker"] = 8081

# Same syntax for updates
service_ports["api"] = 9000

# Update several entries

service_ports.update({
    "database": 5432,
    "cache": 6379,
})

# 05 - Checking whether keys exist
service_ports: dict[str, int] = {
    "api": 8080,
    "worker": 8081,
}

if "api" in service_ports:
    print("API exists")

8080 in service_ports # False

# To explicitly check values
if 8080 in service_ports.values():
    print("Port is already used")

# Key membership
seen: dict[int, int] = {}

if target_value in seen:
    return seen[target_value]

# 06 - Removing entries
# Use del when the key must exist
service_ports: dict[str, int] = {
    "api": 8080,
    "worker": 8081,
}

del service_ports["worker"]

# A missing key rasies KeyError
# Use .pop() to remove and return a value
api_port = service_ports.pop("api")

#Provide a default when the key may be absent
database_port = service_ports.pop("database", None)

# To remove everything
service_ports.clear()

# 07 - Iterating over dictionaries
# Looping directly over a dictionary gives it's keys
service_ports: dict[str, int] = {
    "api": 8080,
    "worker": 8081,
}

for service in service_ports:
    print(service)

# is the same as
for service in service_ports.keys():
    print(service)

# Loop over values
for port in service_ports.values():
    print(port)

# Do a key and value loop with .items()
for service, port in service_ports.items():
    print(service, port)

# 08 - Counting values manually
# A dictionary commonly acts as a frequency map
status_codes: list[int] = [200, 500, 200, 404, 500, 200]

counts: dict[int, int] = {}

for status_code in status_codes:
    counts[status_code] = counts.get(status_code, 0) + 1

# Result
{
    200: 3,
    500: 2,
    404: 1,
}

# The important pattern is
counts[value] = counts.get(value, 0) + 1
# Common mistake
counts[value] += 1 #This would raise a key error unless the value was initializaed beforehand

# 09 - Mapping values to indexes
# A dictionary can store where a value appeared
numbers: list[int] = [7, 2, 11, 15]
index_by_value: dict[int, int] = {}

for index, number in enumerate(numbers):
    index_by_value[number] = index

# Result
{
    7: 0,
    2: 1,
    11: 2,
    15: 3,
}

# This pattern is central to problems such as Two Sum:
def two_sum(numbers: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []

# 10 - Mutable values and grouped data
# Dictionary values can be lists, sets or other dictionaries
deployments_by_region: dict[str, list[str]] = {
    "eu-west-1": ["api", "worker"],
    "us-east-1": ["database"],
}

# Append through the key
deployments_by_region["eu-west-1"].append("cache")