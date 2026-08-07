# 1 - What is a list?
# An ordered, changeable collection of values
services: list[str] = ["API", "worker", "database"]
#Order is preserved, and you can access elements by their index
#Indexes start at 0
#Duplicates are allowed
#Lists are mutable, values can be added, removed or replaced
#Generally lists should be of one type, but Python does not enforce this

# 2 - Creating a list
deployment_queue: list[str] = []
replica_counts: list[int] = [3, 5, 2, 4]
#Convert another iterable into a list
service_name: str = "API"
services_list: list[str] = list(service_name)
#Repeating an immutable value
health_checks: list[bool] = [True] * 5 # [True, True, True, True, True]

#Accessing values
services: list[str] = ["API", "worker", "database"]
print(services[0]) #API
print(services[1]) #worker
print(services[2]) #database
#Negative indexes count backwards
print(services[-1]) #database

#An invalid index will raise an IndexError
print(services[3]) #IndexError: list index out of range

#List not empty check, an empty list evaluates to False
if services:
    first_service: str = services[0]

# 4 - Updating values
services: list[str] = ["API", "worker", "database"]
services[1] = "cache" #["API", "cache", "database"]

# 5 - Basic Slicing
services: list[str] = ["API", "worker", "database"]
print(services[1:3]) #["worker", "database"]
print(services[:2]) #["API", "worker"]
print(services[1:]) #["worker", "database"]
#Slicing does not raise an error when the end is beyond the list
#A slice creates a new list

# 6 - Adding values
services: list[str] = ["API", "worker", "database"]
services.append("cache") #["API", "worker", "database", "cache"]
# extend adds multiple values from another iterable
services.extend(["cache", "search"]) #["API", "worker", "database", "cache", "search"]
# insert adds a value at a specific index
services.insert(1, "cache") #["API", "cache", "worker", "database"]

# 7 - Removing values
deployment_queue: list[str] = ["API", "worker", "database"]
last_service: str = deployment_queue.pop() #last_service is "database", deployment_queue is ["API", "worker"]
#Remove at a specific index
first_service: str = deployment_queue.pop(0) #first_service is "API", deployment_queue is ["worker"]
#remove() removes the first matching value
services: list[str] = ["api", "worker", "api"]
services.remove("api") # ["worker", "api"]

#del removes by index or slice
deployment_queue: list[str] = ["api", "worker", "database"]
del services[1] #["api", "database"]

# clear() removes everything
services.clear() # []

# 8 - Membership and useful built-ins
services: list[str] = ["api", "worker", "database"]
if "api" in services:
    print("API service found")

if "cache" not in services:
    print("Cache missing")

#When frequent membership checks matter, a set is usually better

#len() is length of list
service_count: int = len(services)

#sum() can be used to sum up integer lists
replica_counts: list[int] = [2,3,4]
total_replicas: int = sum(replica_counts)

#min() and max() retrieve minimum and maximum values respectively
lowest_count: int = min(replica_counts)
highest_count: int = max(replica_counts)
#Calling these functions on empty list will raise ValueError

#Joining lists
backend_services: list[str] = ["api", "worker"]
data_services: list[str] = ["database", "cache"]

all_services: list[str] = backend_services + data_services

# 9 - Sorting and reversing
# .sort() sorts the existing list in place
response_times: list[int] = [120, 40, 80]

response_times.sort()
# [40, 80, 120]

# Descending
response_times.sort(reverse=True)
# [120, 80, 40]

#.sort() returns none so sorted_times = response_times.sort() would return None
#sorted() is preferable, returns a new sorted list and leaves original unchanged
response_times: list[int] = [120, 40, 80]
sorted_times: list[int] = sorted(response_times)

#Reversing
response_times.reverse()
#reversed() returns an iterator not a list, so to create a new list
reversed_services = list(reversed(services))

# 10 - Iterating over lists
services: list[str] = ["api", "worker", "database"]
for service in services:
    print(service)

# Use enumerate() when you need the index and value
for index, service in enumerate(services):
    print(index, service)

# Iterate backwards
for service in reversed(services):
    print(service)

# 11 - Copying a list correctly
# Assignment does not create a copy
services: list[str] = ["api", "worker"]

other_services = services
other_services.append("database")

print(services)
# ["api", "worker", "database"]
#Both variables refer to the same lists
# Create a shallow copy with
other_services: list[str] = services.copy()

# 12 - Nested Lists
deployment_matrix: list[list[str]] = [
    ["api", "running"],
    ["worker", "failed"],
    ["database", "running"],
]

# Access a row
deployment_matrix[1]
# ["worker", "failed"]

# Access a value inside a row
deployment_matrix[1][0]  # "worker"
deployment_matrix[1][1]  # "failed"

# 13 - Common Patterns
#Collect matching values, instantiate an empy list and add to it
response_times: list[int] = [120, 250, 80, 310]
slow_requests: list[int] = []

for response_time in response_times:
    if response_time > 200:
        slow_requests.append(response_time)

# Searching for an index
services: list[str] = ["api", "worker", "database"]
target: str = "worker"

target_index: int = -1

for index, service in enumerate(services):
    if service == target:
        target_index = index
        break

# Two-pointer pattern
numbers: list[int] = [1, 3, 5, 7, 9]
target: int = 10

left: int = 0
right: int = len(numbers) - 1

while left < right:
    current_sum: int = numbers[left] + numbers[right]

    if current_sum == target:
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

# Do not modify a list while iterating over it!