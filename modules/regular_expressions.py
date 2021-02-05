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

#Replacing a string
txt = '''I%%% am e%mba%rkin%g on% th%is %awesome journey to le%arn Python.% It is a fa%ntastic%%% langua%%%ge for any% developer to %%learn.'''

replacing_text = re.sub('%', '', txt)
print(replacing_text)

#Escape characters
regex_pattern = r'\d+'
text = 'This example prints out the day 6 and the year 2021'
matching = re.findall(regex_pattern, text)
print(matching)