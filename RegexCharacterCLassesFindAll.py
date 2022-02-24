import re
from unicodedata import name
resume = '''
JANE SOMEBODY
123 Anywhere Street, City, State
555-000-0000
janesomebody@emailprovider.com

PROFILE

State the type of job you are seeking and highlight several of your most important, impressive and marketable skills.

SUMMARY OF SKILLS

- Include your most marketable skills and accomplishments here.
- Ensure the skills you list are relevant to the type of job you are seeking.
- Be as specific as possible.
- Ensure that this section is full of the keywords employers will likely use when sorting resumes.
- If keywords are commonly stated more than on way, you must use both forms of the word (for example, Master of Business Administration and MBA)

WORK EXPERIENCE

Administrative Assistant, ABC Company, City, State, 2006 to present
- Use a combination of verbs and nouns to describe job duties and accomplishments that are most relevant to the work you are currently seeking.
- Don't forget to include a variety of targeted keywords
- List jobs in reverse chronological order; your most recent job goes first.

Administrative Assistant, XYZ Company, City, State, 2000 to 2006
- Continue to use verbs and nouns to describe job duties and accomplishments that are most relevant to the work you are currently seeking and target important keywords.

Customer Service Representative, Another Company, City, State, 1998 to 2000
- Continue to use verbs and nouns to describe job duties and include important keywords.
- Normally you should only include your most recent ten years of work experience on your resume. There are exceptions, but typically employers are most interested in your most recent experience, and going back more than ten years on your resume can age you.

EDUCATION

Administrative Assistant Certificate, Any College, City, State
442-112-3311
VOLUNTEER EXPERIENCE

- Only include this section if it adds information that is relevant to the job you are seeking.
- You may also include hobbies here, but only if they are positive and relevant to the job you are seeking.

REFERENCES
Your Momma - 402-417-6494
available upon request
'''
phoneRegex = re.compile('\\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.search(resume))
print(phoneRegex.findall(resume))

digitRegex1 = re.compile(r'\d')

print (digitRegex1.search("1"))

lyrics = '''Fluffhead was a man, with a horrible disease,  he could not find no cure,  won't you help him if you please,  4 realz.  2001 is good too.'''

fluffRegex = re.compile(r'\d+\s\w+')
x = fluffRegex.findall(lyrics)
print(x)

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Apples, Peaches, Pumpkin Pie'))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Apples, Peaches, Pumpkin Pie'))

vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Apples, Peaches, Pumpkin Pie'))

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there Bucky!'))

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('He Said, Hello there Bucky!'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('1234123412341252356845609345860945680352134580349582034580256782034958'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('1234123412341252356845609345860945680352134580349582034580256782034958!'))

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat fat rat with a mat'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat fat rat with a mat'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Jonathan Last Name: Chester'))

nonGreedyRegex = re.compile(r'<(.*?)>')
print(nonGreedyRegex.findall('<To serve wooks> for dinner>'))

greedyRegex = re.compile(r'<(.*)>')
print(greedyRegex.findall('<To serve wooks> for dinner>'))

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))

dotStar = re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)
print(vowelRegex.findall('Apples, Peaches, Pumpkin Pie'))

vowelRegex = re.compile(r'[aeiou]',re.I)
print(vowelRegex.findall('Apples, Peaches, Pumpkin Pie'))