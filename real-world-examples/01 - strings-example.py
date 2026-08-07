raw_identifier: str = " PRODUCTION-payment-api-v3 "

# Remove surrounding whitespace and convert to lowercase
deployment_identifier: str = raw_identifier.strip().lower()

# Split the identifier into parts using the hyphen as a delimiter
parts: list[str] = deployment_identifier.split("-")

environment: str = parts[0] # "production"
service: str = parts[1] # "payment"
component: str = parts[2] # "api"
version_text: str = parts[3] # "v3"

# Remove the leading 'v' from the version and convert to an integer
version_number_text: str = version_text.removeprefix("v") # "3"

if version_number_text.isdigit():
    version_number: int = int(version_number_text) # 3

    full_service_name: str = f"{service}-{component}" # "payment-api"

    summary: str = (
        f"Deployment Summary:\n"
        f"Deploying {full_service_name} version {version_number} to the {environment} environment."
    )

    print(summary
    )
else:
    print(f"Invalid version format: {version_text}")