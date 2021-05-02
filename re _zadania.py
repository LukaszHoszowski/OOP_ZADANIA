# Zadanie 1
import re


def check_dice(string):
    return True if re.search(r'\d*[d]{1}\d*[+|-]{0,1}\d*\b', string, re.I) else False


# print(check_dice('8D7+10 abcdefghijk'))

# Zadanie 2

with open('text.txt', 'r') as fin:
    text_to_search = fin.read()

print(len(re.findall(r'autor\b', text_to_search)))
print(re.findall(r'\d+%{1}', text_to_search))
print(len(re.findall(r'\.', text_to_search)))
print(len(re.findall(r'polski', text_to_search, re.I)))
