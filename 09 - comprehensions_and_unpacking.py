# 01 List Comprehensions
# A list comprehension builds a new list from an iterable
squares: list[int] = [number * number for number in numbers]

# Equivalent Loop
squares: list[int] = []

for number in numbers:
    squares.append(number * number)

# Use a condition to filter values
even_numbers = [number for number in numbers if number % 2 == 0]

# Transformation comes before for; filtering comes after:
result = [transform(value) for value in values if condition(value)]
# Prefer a normal loop when logic requires multiple steps, side effects or nested conditions

# 02 - Set and dictionary comprehensions
# Useful for transforming values while removing duplicates
unique_lengths: set[int] = {
    len(service_name)
    for service_name in service_names
}

# Dictionary Comprehension
index_by_service: dict[str, int] = {
    service: index
    for index, service in enumerate(services)
}

# Another common pattern
squares_by_number = {
    number: number * number
    for number in numbers
}

# If duplicate keys are produced, the later value wins
values = ["api", "api"]

mapping = {
    value: index
    for index, value in enumerate(values)
}

# {"api": 1}

# 03 - Conditional expressions inside comprehensions
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

# This differs from filtering
# Transform every number
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

# Keep only even numbers
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

# Both can be combined, but it's a bit confusing
result = [
    number * 2 if number > 10 else number
    for number in numbers
    if number >= 0
]

# 04 - Basic unpacking
# Unpacking assigns iterable values to separate variables
coordinates = (4, 7)

row, column = coordinates

# The number of variables must normall match
first, second = [10, 20]

# Common interview uses:
for key, value in mapping.items():
    ...

for index, value in enumerate(values):
    ...

# Swap values without a temp variable
left, right = right, left

# Unpack a returned tuple
minimum, maximum = find_bounds(values)

# Use _ for an intentionally ignored value
service_name, _ = service_record

# 05 - Starred Unpacking
# Use * to collect remaining values into a list
first, *middle, last = [1, 2, 3, 4, 5]

# first = 1
# middle = [2, 3, 4]
# last = 5

# Other forms
first, *rest = values
*start, last = values

# A starred target can match zero values
first, *rest = [10]

# first = 10
# rest = []

# Use * to unpack values into a new list
combined = [*left_values, *right_values]

# Use ** to unpack dicts
combined_config = {
    **default_config,
    **custom_config,
}