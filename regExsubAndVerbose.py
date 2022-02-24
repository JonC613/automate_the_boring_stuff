import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Brian gave the string to Agent David'))

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('REDACTED', 'Agent Brian gave the string to Agent David'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Brian gave the string to Agent David'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1******','Agent Brian gave the string to Agent David'))

phoneRegex = re.compile(r'''
\d\d\d      #area code
-           #first dash
\d\d\d      #first 3 digits
-           #second dash
\d\d\d\d    #last 4 digits''', re.VERBOSE)

phoneRegexAreaCode = re.compile(r'''
(\d\d\d-)|              # area code (without parens, with dash)
(\(\d\d\d\) )           # -or- area code with parens / no dash
\d\d\d                  # first 3 digits
-                       # second dash
\d\d\d\d                # last 4 digits''', re.VERBOSE)


print(phoneRegex.findall('My number is 502-221-1113 and her number is 221-115-1122'))
print(phoneRegexAreaCode.findall('My number is 502-221-1113 and her number is 221-115-1122'))