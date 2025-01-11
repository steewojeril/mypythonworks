# 3. Extracting Dates from Text

# If you want to extract dates like DD-MM-YYYY from text:
import re

date_pattern = r"\d{2}-\d{2}-\d{4}"
text = "The event is on 25-12-2025."
dates = re.findall(date_pattern, text)
print(dates)  # Output: ['25-12-2025']
