import re



pattern = r"[a-z]+"

text = "Hello World 123"
matches = re.findall(pattern, text)
print("Matches found:", matches)