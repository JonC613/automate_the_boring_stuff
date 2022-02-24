import re

batRegex = re.compile(r'Bat(wo)?man')
#mo = batRegex.search('The Adventures of Batman')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)*man')
#mo = batRegex.search('The Adventures of Batwoman')
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwman')
#print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
moAC = phoneRegex.search("My phone number is 402-417-6494")
moNoAC = phoneRegex.search("My phone number is 417-6494")
print(moAC.group())
print(moNoAC.group())

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print (mo.group())

haRegex = re.compile(r'(Ha){3}')
haMo = haRegex.search('He said "HaHaHa"')
print (haMo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){2,4}')
phoMO = phoneRegex.search('My numbers are 402-417-6494,417-6494,212-555-5511')
print (phoMO.group())

digitRegex = re.compile(r'(\d){3,5}')
digMo = digitRegex.search('1234567890')
print(digMo.group())

digitRegex = re.compile(r'(\d){3,5}?')
digMo = digitRegex.search('1234567890')
print(digMo.group())