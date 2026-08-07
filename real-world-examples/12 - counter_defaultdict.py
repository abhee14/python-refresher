# Group Anagrams

from collections import Counter, defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: defaultdict[
        tuple[tuple[str, int], ...],
        list[str],
    ] = defaultdict(list)

    for word in words:
        frequency_key = tuple(sorted(Counter(word).items()))
        groups[frequency_key].append(word)

    return list(groups.values())


# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))