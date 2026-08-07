def first_repeated_service(services: list[str]) -> str | None:
    first_index: dict[str, int] = {}

    for index, service in enumerate(services):
        if service in first_index:
            return service

        first_index[service] = index

    return None


services = ["api", "worker", "database", "worker"]

print(first_repeated_service(services))
# worker