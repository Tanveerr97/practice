import re

text = "Hello world"
pattern = r"He55llo"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match")
