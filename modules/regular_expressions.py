#A regular expression (Regex) helps find patterns in data
import re

text = '''Python is an awesome language to learn. It has many real world applications '''

match = re.search('awesome', text, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(text[start:end])