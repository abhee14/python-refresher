deployments: list[tuple[str, str, int]] = [
    ("payments-api", "production", 3),
    ("worker", "staging", 1),
    ("frontend", "production", 2),
]

for service, environment, replicas in deployments:
    if environment == "production":
        print(f"{service}: {replicas} replicas")