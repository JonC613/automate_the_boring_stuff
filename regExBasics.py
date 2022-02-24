from string import digits
import re

message = 'Call me on my cell phone 404-333-1123 tomorrow or on my land line 404-221-1131 the next day'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
moSearch = phoneNumRegex.search(message)
moFindAll = phoneNumRegex.findall(message)
print(moSearch.group())
for i in range(len(moFindAll)):
    print("Phone number found: " + moFindAll[i])

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not correct phone-number length
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing firest dash
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber: 
    print('Could not find a valid phone number')
