# Important Functions in Python's re Module

import re

# re.match(): Checks if the pattern matches at the beginning of the string.

re.match(r"hello", "hello world")  # Output: match object (true or false)

# re.search(): Searches for the pattern anywhere in the string.

result = re.search(r"hello", "hello world")

if result:
    print("Match found:", result.group())  # group()-to extract specific parts of a string based on patterns.
else:
    print("No match found")


# re.findall(): Finds all occurrences of the pattern in the string.

re.findall(r"\d", "abc123def456")  # Output: ['1', '2', '3', '4', '5', '6']

# re.sub(): Replaces occurrences of the pattern with a new string.

re.sub(r"\d", "#", "abc123")  # Output: 'abc###'

# re.split(): Splits the string by occurrences of the pattern.

re.split(r"\s+", "hello world")  # Output: ['hello', 'world']