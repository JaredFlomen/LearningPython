#A regular expression (Regex) helps find patterns in data
import re

text = '''Python is an awesome language to learn. It has many real world applications. I love python'''

match = re.search('awesome', text, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(text[start:end])

matches = re.findall('python', text, re.I)
print(matches)