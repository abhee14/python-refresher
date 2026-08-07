# 1 - Creating Strings
#Use either single or double quotes
first_name: str = "Abhee"
job_title: str = 'Infrastructure Engineer'

#Use whichever avoid unnecessary escaping
message: str = "I'm learning Python"
quote: str = 'He said, "Hello"'

#Best Practice
#Use clear snake_case and add type hints for better readability and maintainability
service_name: str = "payment-service"
deployment_status: str = "successful"

# 2 - Multiline Strings
#Use triple quotes for multiline strings
description: str = """This service processes payments.
It runs in Kubernetes.
It is deployed through CI/CD."""
#These would be used for function and class documentation

# 3 - Accessing Characters in a String
service_name: str = "payment-service"
print(service_name[0]) #p
print(service_name[7]) #s
#Negative indexing starts from the end of the string
print(service_name[-1]) #e
print(service_name[-7]) #s
#Accessing an invalid index will raise an IndexError
print(service_name[20]) #IndexError: string index out of range

# 4 - String Length
print(len(service_name)) #15

# 5 - String Slicing
service_name: str = "payment-service"
print(service_name[0:7]) #payment, characters from index 0 to 6
print(service_name[8:15]) #service, characters from index 8 to 14

# You can omit the start or stop index to slice from the beginning or to the end of the string
print(service_name[:7]) #payment, characters from the start to index 6
print(service_name[8:15]) #service, characters from index 8 to the end

# Slicing with a step
print(service_name[0:7:2]) #pymnt, characters from index 0 to 6 with a step of 2

# Reverse a string
reversed_service_name: str = service_name[::-1] #ecivres-tnemyap

# Slicing beyond string length does not raise an error, it just returns the available characters
print(service_name[0:20]) #payment-service, characters from index 0 to 14

# 6 - Strings are immutable
status: str = "failed"
status[0] = "s" #TypeError: 'str' object does not support item assignment

# Create a new string or change the value instead
status = "F" + status[1:] #status is now "Failed"

# String methods also return new strings rather than changing the original
status: str = "Failed"
upper_status: str = status.upper() #upper_status is "FAILED", status is still "Failed"

# 7 - String Concatenation
environment: str = "production"
service: str = "payments"

resource_name: str = environment + "-" + service #resource_name is "production-payments"

# Repetition
separator: str = "-" * 10 #separator is "----------"

# f-strings (formatted string literals) can be used for more readable string concatenation
resource_name: str = f"{environment}-{service}" #resource_name is "production-payments

# 8 - String formatting with f-strings
service_name: str = "payments"
replica_count: int = 3
message: str = f"The {service_name} service has {replica_count} replicas."

#Expressions can be used inside f-strings
replica_count: int = 3
message: str = f"The {service_name} service has {replica_count * 2} replicas after scaling."

# Format decimal values
cpu_usage: float = 0.756
message: str = f"CPU usage is {cpu_usage:.2%}" #message is "CPU usage is 75.60%"

# 9 - Changing case
service_name: str = "Payments Service"
print(service_name.lower()) #payments service
print(service_name.upper()) #PAYMENTS SERVICE
print(service_name.title()) #Payments Service
print(service_name.capitalize()) #Payments service

# Case-insensitive comparison
status: str = "SUCCESS"

if(status.lower() == "success"):
    print("The operation was successful.")

# A better option is casefold()
if (status.casefold() == "success"):
    print("The operation was successful.")

# 10 - Removing whitespace
raw_status: str = "   successful\n"
print(raw_status.strip()) #successful, removes leading and trailing whitespace
print(raw_status.lstrip()) #successful\n, removes leading whitespace
print(raw_status.rstrip()) #   successful, removes trailing whitespace

# Common input-cleaning pattern:
status: str = input("Enter the status: ").strip().lower()

# 11 - Replacing text
resource_name: str = "payment_service"
resource_name = resource_name.replace("_", "-")

# 12 - Splitting Strings
# split() converts a string into a list of substrings based on a delimiter
resource_name: str = "payment-service"
parts: list[str] = resource_name.split("-") #parts is ["payment", "service"]
# Without an argument, split() uses whitespace as the default delimiter

# 13 - Joining Strings
services: list[str] = ["payments", "orders", "users"]
services_text: str = ", ".join(services) #services_text is "payments, orders, users"

# 14 - Searching inside strings

# Checking membership
log_message: str = "deployment failed due to timeout"
print("failed" in log_message) #True
print("success" in log_message) #False

# find() returns the first index or -1 if not found
message: str = "deployment failed due to timeout"
index: int = message.find("failed") #index is 11
index: int = message.find("success") #index is -1

# index() is similar to find() but raises a ValueError if not found
index: int = message.index("failed") #index is 11
index: int = message.index("success") #ValueError: substring not found

# 15 - Prefixes and suffixes
file_name: str = "deployment.yaml"
print(file_name.startswith("deployment")) #True
print(file_name.endswith(".yaml")) #True

# Multiple suffixes can be checked by passing a tuple
if file_name.endswith((".yaml", ".yml")):
    print("This is a YAML file.")

# 16 - Counting Occurrences
message: str = "error warning error success error"
count: int = message.count("error") #count is 3

# 17 - Useful Validation Methods
print("123".isdigit()) #True, checks if all characters are digits
print("abc".isalpha()) #True, checks if all characters are alphabetic
print("abc123".isalnum()) #True, checks if all characters are alphanumeric
print("   ".isspace()) #True, checks if all characters are whitespace
print("lowercase".islower()) #True, checks if all characters are lowercase
print("UPPERCASE".isupper()) #True, checks if all characters are uppercase

# 18 - Escape Characters
message: str = "Line one\nLine two"
path: str = "C:\\Users\\Abhee"
quote: str = "He said, \"Hello\""

"\n"  # New line
"\t"  # Tab
"\\"  # Backslash
"\""  # Double quote
"\'"  # Single quote

# Raw strings can be used to treat backslashes literally
raw_path: str = r"C:\Users\Abhee" #raw_path is "C:\\Users\\Abhee"

# 19 - Comparing Strings
first_status: str = "success"
second_status: str = "success"

print(first_status == second_status)  # True
print(first_status != second_status)  # False

# Comparisons are case-sensitive
# For case-insensitive comparisons, use casefold() or lower()

# 20 - Iterating over a string
service_name: str = "payments"
for char in service_name:
    print(char)  # Prints each character in the string on a new line
