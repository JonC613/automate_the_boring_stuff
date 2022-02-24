from distutils.spawn import spawn


bandMembers = ['Trey','Page','Fishman','Mike']
a = bandMembers.index('Page')

print (a)

bandMembers.append('Dave')
bandMembers.insert(1, 'Billy')

print (bandMembers)

bandMembers.remove('Billy')

print(bandMembers)

numbers = [4,2,3,1]

numbers.sort()

print (numbers)

bandMembers.sort(reverse=True)
print(bandMembers)

words = ['Dog','apple','Banana','craft']
words.sort()
print (words)
words.sort(key=str.lower)
print (words)
