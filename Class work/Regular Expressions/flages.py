import re
pattern = r"hello"

text = "Hello"
match = re.search(pattern, text, re.IGNORECASE)
print("Case-insensitive match:", match.group() if match else "No match")