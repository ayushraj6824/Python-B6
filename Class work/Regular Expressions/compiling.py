#pattern is with us in compile  form 
#pattern that is compile using re model search that pattern and printing the matches ,matches are stored 
#in list form this method is efficient in performance wise it worksimiar to other method
import re
pattern = re.compile(r"\d+")

text = "123 apples, 456 bananas"
matches = pattern.findall(text)
print("Matches:", matches)