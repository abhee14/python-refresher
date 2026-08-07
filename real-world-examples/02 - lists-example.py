deployment_queue: list[str] = [
    "api",
    "worker",
    "database",
]

deployment_queue.append("frontend")

if deployment_queue:
    current_deployment: str = deployment_queue.pop(0)
    print(f"Deploying {current_deployment}")

for position, service in enumerate(deployment_queue, start=1):
    print(f"{position}: {service}")

remaining_count: int = len(deployment_queue)
print(f"{remaining_count} deployments remaining")