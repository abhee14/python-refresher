def contains_duplicate(deployment_ids: list[str]) -> bool:
    seen: set[str] = set()

    for deployment_id in deployment_ids:
        if deployment_id in seen:
            return True

        seen.add(deployment_id)

    return False


deployment_ids = ["deploy-101", "deploy-102", "deploy-101"]

print(contains_duplicate(deployment_ids))
# True

# Shorter solution
def contains_duplicate(deployment_ids: list[str]) -> bool:
    return len(deployment_ids) != len(set(deployment_ids))