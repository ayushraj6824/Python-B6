import re
pattern = r"<.*>"

text = "content"
match = re.search(pattern, text)

if match:
    print("Greedy match:", match.group())
else:
    print("No greedy match found")

print("-----------------")

pattern_lazy = r"<.*?>"
match_lazy = re.search(pattern_lazy, text)

if match_lazy:
    print("Lazy match:", match_lazy.group())
else:
    print("No lazy match found")

pattern = r"<.*>"




print("==============")
pattern = r".*"

text = "content"
match = re.search(pattern, text)
print("Greedy match:", match.group())
print("------------")
pattern_lazy = r".*?"
match_lazy = re.search(pattern_lazy, text)
print("Lazy match:", match_lazy.group())