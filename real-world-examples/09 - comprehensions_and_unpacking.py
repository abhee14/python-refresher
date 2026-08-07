def healthy_service_names(
    service_statuses: list[tuple[str, bool]],
) -> set[str]:
    return {
        service_name
        for service_name, is_healthy in service_statuses
        if is_healthy
    }


service_statuses = [
    ("api", True),
    ("worker", False),
    ("database", True),
]

print(healthy_service_names(service_statuses))
# {"api", "database"}