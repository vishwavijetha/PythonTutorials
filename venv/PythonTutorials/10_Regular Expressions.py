"""
================================================================================================================================
Author: Vishwa
Date Created: 02/04/2019
--------------------------
Topic: Regular Expressions and Pattern Matching --
--------------------------
module: { import re }

Declaration: { pattern = re.compile(r'regex pattern'), re.IGNORECASE | re.DOTALL | re.VERBOSE}

Methods: { compile(), search(), findall(), groups(), group(), groupindex(), finditer(), split(), match(), sub(), subn()}


Patterns: { \d, \D, \w, \W, \s, \S, 'abc', [abc], [a-zA-Z], (s)?, (s)*, (s)+, [^abc], [abc]$, ., .*, {n}, {n,}, {,m}, {n,m}}
================================================================================================================================
"""
import re

print('\nRegular Expression:\n')
print('\n1) Matching first occurrence of phone number using search() and  group() methods:')
print('----------------------------------------------------------------------------------')
input_text = 'hi my number is 7760607555 and u can also reach me at 7123456789'
pattern = r'[789]{1}[0-9]{9}'
print('Input text: ', input_text)
print('Regex Pattern: ', pattern)
regex_pattern_obj = re.compile(pattern)
matcher = regex_pattern_obj.search(input_text)
print(matcher.group())

print('\n2) Matching all occurrences of phone number using findall() method -- {returns a list of matched objects}:')
print('----------------------------------------------------------------------------------')
input_text = 'hi my number is 7760607555 and u can also reach me at 7123456789'
pattern = r'[789]{1}[0-9]{9}'
print('Input text: ', input_text)
print('Regex Pattern: ', pattern)
regex_pattern_obj = re.compile(pattern)
matcher = regex_pattern_obj.findall(input_text)
print(matcher, matcher[0], matcher[1])

print('\n3) Matching email ids:')
print('----------------------------------------------------------------------------------')
input_text = '''hi my primary emails are a_z@b.c.0102.abcd, vishwa.vijetha@gds.com and u can also reach me
 at vishwa.ste@gmail.com'''
pattern = r'([._a-zA-Z0-9]+@[._a-zA-Z0-9]+\.[a-zA-Z]{2,4})'
print('Input text: ', input_text)
print('Regex Pattern: ', pattern)
regex_pattern_obj = re.compile(pattern, re.VERBOSE)
matcher = regex_pattern_obj.findall(input_text)
print(matcher)
