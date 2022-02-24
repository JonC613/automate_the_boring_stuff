from genericpath import getsize
import os

print(os.path.join('folder1','folder2','folder3','file.png'))
print(os.sep)
print(os.getcwd())
os.chdir('C:\\temp\\MS')
print(os.getcwd())
print(os.path.abspath('spam.png'))
print(os.path.abspath('..\\..\\spam.png'))
print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs('C:\\temp\\MS\\spam.png'))
print(os.path.relpath('C:\\folder1\\folder2\\spam.png', 'c:\\folder1'))
print(os.path.basename('C:\\temp\\MS\\spam.png'))
print(os.path.dirname('C:\\temp\\MS\\spam.png'))
print(os.path.exists('C:\\temp\\MS\\spam.png'))
print(os.path.exists('C:\\windows\\system32\\calc.exe'))
print(os.path.isfile('C:\\windows\\system32\\calc.exe'))
print(os.path.isdir('C:\\windows\\system32\\calc.exe'))
print(os.path.getsize('C:\\windows\\system32\\calc.exe'))
print(os.listdir('C:\\temp\\sxs'))


totalSize = 0
for filename in os.listdir('C:\\temp\\BI'):
    if not os.path.isfile(os.path.join('c:\\temp\\bi',filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\temp\\bi',filename))

print(totalSize)

os.makedirs('C:\\temp2\\temp3\\temp4')