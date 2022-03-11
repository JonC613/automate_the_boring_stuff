hellofile = open('c:\\temp2\\Hello.txt')
contentString = hellofile.read()
print (contentString)
hellofile.close()
hellofile = open('c:\\temp2\\Hello.txt')
contentList = hellofile.readlines()
print (contentList)
hellofile.close()

hellofileWrite = open('c:\\temp2\\HelloWrite.txt', 'w')
hellofileAppend = open('c:\\temp2\\HelloAppend.txt', 'a')

for num in range(10):
    hellofileWrite.write('Hello!!_' + str(num) + '\n')
hellofileWrite.close()

for num in range(10):
    hellofileAppend.write('Hello!!_' + str(num) + '\n')
hellofileAppend.close()