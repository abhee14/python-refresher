# 1 - Creating Variables
name: string = "Abhee"
age = 28
height = 1.65
is_engineer = True

# 2 - Basic data types

#Int: Whole Numbers
age = 28
score = 100
temperature = -5

#Float: Decimal Numbers
height = 1.65
price = 19.99
percentage = 87.5
result = 10/4 #2.5 because regular division always returns a float

#Bool: True or False
is_engineer = True
has_job = False

#A comparison can produce a boolean value
age = 28
is_adult = age >= 18 #True
is_adult = age < 18 #False

#None: Represents the absence of a value
result = None
user = None

#Checking for None is not == but uses "is"
if result is None:
    print("Result is None")

if result is not None:
    print("Result is not None")

# 3 - Checking a variable's type
type(age) #<class 'int'>
isinstance(age, int) #True, checks whether a value belongs to a type

# 4 - Type Conversion
#Convert to Integer
age_text = "28"
age = int(age_text) #28

#A float loses it's decimal part when converted to an integer
number = int(5.9) #5

#String to Float
price = float("19.99") #19.99

#Integer to Float
number = float(10) #10.0

#Convert to String
str(28) #"28"

#Conver to Boolean
bool(1) #True
bool(0) #False
bool("Hello") #True
bool("") #False
bool(None) #False
print(bool("False")) #True because it is a non-empty string

# 5 - Reassigning Variables
score = 10
score = 20 #score is now 20

#Python is dynamically typed, so you can change the type of a variable
value = 10 #value is an integer
value = "Hello" #value is now a string
value = True #value is now a boolean

# 6 - Variable Operations
score = 10
score = score + 5 #score is now 15

score = 10
score += 5 #score is now 15, shorthand for score = score + 5
score -= 3 #score is now 12, shorthand for score = score - 3
score *= 2 #score is now 24, shorthand for score = score * 2
score /= 4 #score is now 6.0, shorthand for score = score / 4

score = 10
score //= 2 #score is now 5, shorthand for score = score // 2, floor division operator
score %= 2 #score is now 1, shorthand for score = score % 2, modulus operator

score = 4
score **= 2 #score is now 16, shorthand for score = score ** 2, exponentiation operator
#Python does not support count++

# 7 - Multiple Assignment
name,age,active = "Abhee", 28, True #name is "Abhee", age is 28, active is True
#Assign the same value to multiple variables
x = y = z = 0 #x, y, and z are all 0
#Swap Two Variables
a = 10
b = 20
a, b = b, a #a is now 20, b is now 10

# 8 - Type Hints
name: str = "Abhee"
age: int = 28
height: float = 1.65
is_engineer: bool = True
result: None = None

#These are not enforced by Python, but can be used by IDEs and linters to catch potential errors
age: int = 28
age = "twenty-eight"  # Python still allows this

# 9 - Variable Naming Convention
#Python normally uses snake_case for variable names
snake_case_variable = "This is snake case"

#Python is case-sensitive
name = "Abhee"
Name = "John" #This is a different variable than name

# 10 - Constants
#Python does not have built-in constant types, but uppercase names indicate value should not be changed
MAX_RETRIES = 5

# 11 - Truty and falsy values

#These values are considered false in conditions:
False
None
0
0.0
""
[]
{}
set()

# Most other values are considered 
name = ""

if name:
    print("A name was provided")
else:
    print("Name is empty")

count = 5

if count:
    print("Count is not zero")