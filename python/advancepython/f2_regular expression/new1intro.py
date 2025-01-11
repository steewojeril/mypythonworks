import re
# ()	Capture and group

# 1. Special Characters and Their Meaning

# 1. . (Dot)
# Matches any character except a newline (\n).
print(re.findall(r"e.a", "hello apple, sea"))  # Output: ['e.a', 'a.a']

# 2. ^ (Caret)
# Anchors the regex to the beginning of the string. This means it will only match if the pattern appears at the start of the string.
print(re.findall(r"^hello", "hello world"))  # Output: ['hello']
print(re.findall(r"^world", "hello world"))  # Output: []

# 3. $ (Dollar Sign)
# Anchors the regex to the end of the string. It will only match if the pattern appears at the end of the string.
print(re.findall(r"world$", "hello world"))  # Output: ['world']
print(re.findall(r"hello$", "hello world"))  # Output: []

# 4. [] (Square Brackets)
# Matches any one of the characters inside the brackets.
print(re.findall(r"[aeiou]", "hello"))  # Output: ['e', 'o']

# 5. | (Pipe)
# Acts like a logical OR. It matches the pattern on the left or the pattern on the right.
print(re.findall(r"apple|banana", "apple orange banana"))  # Output: ['apple', 'banana']

# 6. * (Asterisk)
# Matches 0 or more repetitions of the preceding character or group.
print(re.findall(r"ba*", "baaaana"))  # Output: ['baaa']

# 7. + (Plus)
# Matches 1 or more repetitions of the preceding character or group.
print(re.findall(r"ba+", "baaaana"))  # Output: ['baaa']

# 8. ? (Question Mark)
# Matches 0 or 1 occurrence of the preceding character or group.
print(re.findall(r"colou?r", "color colour"))  # Output: ['color', 'colour']

# 9. {n}
# Matches exactly n occurrences of the preceding character or group.
print(re.findall(r"a{3}", "aaabbbcccc"))  # Output: ['aaa']

# 10. {n, m}
# Matches between n and m occurrences of the preceding character or group.
print(re.findall(r"a{2,4}", "aaaabbbbb"))  # Output: ['aaa', 'aa']

# 2. Character Classes

# 1. \d (digit)
# Matches any digit (0-9).
print(re.findall(r"\d", "abc123"))  # Output: ['1', '2', '3']

# 2. \D (non-digit)
# Matches anything that is not a digit.
print(re.findall(r"\D", "abc123"))  # Output: ['a', 'b', 'c']

# 3. \w (word character)
# Matches any alphanumeric character or underscore ([a-zA-Z0-9_]).
print(re.findall(r"\w", "hello123_"))  # Output: ['h', 'e', 'l', 'l', 'o', '1', '2', '3', '_']

# 4. \W (non-word character)
# Matches anything that is not a word character.
print(re.findall(r"\W", "hello123_"))  # Output: [' ']

# 5. \s (whitespace)
# Matches any whitespace character (spaces, tabs, newlines).
print(re.findall(r"\s", "hello world"))  # Output: [' ']

# 6. \S (non-whitespace)
# Matches anything that is not a whitespace character.
print(re.findall(r"\S", "hello world"))  # Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
