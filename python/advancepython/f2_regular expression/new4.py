# Phone Number Validation

# A regex to match phone numbers in the format XXX-XXX-XXXX:
import re
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
phone = "123-456-7890"
match = re.match(phone_pattern, phone)
print(match is not None)  # Output: True

