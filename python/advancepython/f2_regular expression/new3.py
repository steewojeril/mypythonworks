# 1. Validating an Email

import re
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "test@example.com"
match = re.match(email_pattern, email)
print(match is not None)  # Output: True
