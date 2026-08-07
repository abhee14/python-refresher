# Use a stack to validate matching brackets in a deployment expression:
def has_valid_brackets(expression: str) -> bool:
    matching: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack: list[str] = []

    for character in expression:
        if character in matching.values():
            stack.append(character)
        elif character in matching:
            if not stack or stack.pop() != matching[character]:
                return False

    return not stack

#Examples
has_valid_brackets("deploy(api[blue])")
# True

has_valid_brackets("deploy(api[blue)]")
# False