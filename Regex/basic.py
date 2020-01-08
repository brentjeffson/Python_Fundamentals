import re

s = """
    The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

pattern = re.compile(r'The[\s\S]+\.span\(\)')
res = re.search(pattern, s)
pos = res.span()
print(s[pos[0]:pos[1]])



