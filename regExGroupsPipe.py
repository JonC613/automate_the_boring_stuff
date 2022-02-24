import re

phoneNumRegExGroupDash = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegExParens = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
batRegex = re.compile(r'Bat(man|mobile|woman|copter|bat)')


moSearch = phoneNumRegExGroupDash.search('My number is 402-417-6494')
moSearchParen = phoneNumRegExParens.search('My number is (402) 417-6494')
moBatSearchBatMobile = batRegex.search('Batmobile lost a wheel')
moBatSearchBatMotorCycle = batRegex.search('BatMotorcycle lost a wheel')

print(moSearch.group())
print(moSearch.group(1))
print(moSearch.group(2))
print(moSearchParen.group())
print(moBatSearchBatMobile.group())
print(moBatSearchBatMotorCycle.group())