bandMembers = {'leadGuitar': 'Trey', 'bassGuitar': 'Mike', 'keyboards': 'Page', 'drums': 'Fish'}
print ("On Lead Guitar: " + bandMembers['leadGuitar'])

spam = {12345: 'Luggage Combination', 42: "The Answer"}
print (spam[12345])

print(list(bandMembers.keys()))
print(list(bandMembers.values()))
print(list(bandMembers.items()))
print(bandMembers.keys())


for k in bandMembers.keys():
    print(k)

for v in bandMembers.values():
    print(v)

for i in bandMembers.items():
    print(i)

for k, v in bandMembers.items():
    print(k, v)


print (bandMembers.get('leadGuitar', "Buzzy"))
print (bandMembers.get('secondGuitar', "Buzzy"))

