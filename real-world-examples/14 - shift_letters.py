"""
Practical Example: Shift Lowercase Letters

Shift each lowercase English letter by a given number of positions.
Letters wrap back to "a" after "z".

Examples:
    shift_letters("xyz", 2) -> "zab"
    shift_letters("abc", 1) -> "bcd"
"""


def shift_letters(text: str, shift: int) -> str:
    # Store characters in a list because repeatedly concatenating strings
    # inside a loop is less efficient and less idiomatic.
    shifted_characters: list[str] = []

    for character in text:
        # Convert the character to a zero-based alphabet position:
        # "a" -> 0, "b" -> 1, ..., "z" -> 25.
        position: int = ord(character) - ord("a")

        # Add the shift.
        #
        # % 26 wraps positions back to the start of the alphabet:
        # 25 + 2 = 27
        # 27 % 26 = 1
        shifted_position: int = (position + shift) % 26

        # Convert the zero-based position back into a letter.
        shifted_character: str = chr(
            ord("a") + shifted_position
        )

        shifted_characters.append(shifted_character)

    # Join the character list into the final string.
    return "".join(shifted_characters)


# Example calls.
first_result: str = shift_letters("xyz", 2)
print(first_result)
# zab

second_result: str = shift_letters("deployment", 3)
print(second_result)
# ghsorbphqw


# This implementation assumes every input character is between "a" and "z".
# Spaces, uppercase letters, digits, and punctuation would need separate handling.