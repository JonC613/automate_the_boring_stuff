#! python3

import re, pyperclip
# TODO: regex for phone numbers / regex for emails address / get text off the clipboard / extract email/phone from text / copy extracted data to clipboard

phoneRegex = re.compile(r'''

#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?       # area code (optional)
(\s|-)              # first separator
\d\d\d              # first 3 digits
-                   # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)   # extension word-part(optional)
(\d{2,5}))?         # extension number-part (optional)
)
      

''', re.VERBOSE)

emailRegex = re.compile(r'''

# some.+_thing@something.com

[a-zA-Z0-9_.+]+ # name part
@               # @ part
[a-zA-Z0-9_.+]+ # domain name part    

''',re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(extractedEmail)
#print(allPhoneNumbers)
#print(extractedPhone)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n' .join(extractedEmail)
print(results)

pyperclip.copy(results)