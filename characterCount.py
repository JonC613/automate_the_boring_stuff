import pprint 

message = '''
Fluffhead was a man
With a horrible disease
Could not find no cure
Won't you help him if you please?
Fluff came to my door
Fluff came to New York (two parts)
Askin' me for change
His eyes were clear and pure
But his mind was so deranged
Fluff went to a banker
Askin' for some bills
The banker said, "I ain't got that
But I sure got some powerful pills.'''

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

fhtext = pprint.pformat(count)
print(fhtext)
