import shelve

shelfFile = shelve.open('C:\\temp2\\mydata')
shelfFile ['songs'] = ['Carini', 'Fluffhead', 'Mango Song']
shelfFile.close()

shelfFile = shelve.open('C:\\temp2\\mydata')
shelfFileContents = shelfFile['songs']
print (shelfFileContents)
print (shelfFile.keys())
print (list(shelfFile.keys()))
print (list(shelfFile.values()))