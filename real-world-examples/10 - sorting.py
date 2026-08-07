#Sort by highest error count first, shortest service name when error counts are equal


services: list[tuple[str, int]] = [
    ("authentication", 4),
    ("api", 7),
    ("payments", 4),
    ("notifications", 2),
]

ordered_services: list[tuple[str, int]] = sorted(
    services,
    key=lambda service: (-service[1], len(service[0])),
)

print(ordered_services)

"""
Outputs

[
    ("api", 7),
    ("payments", 4),
    ("authentication", 4),
    ("notifications", 2),
]

"""