import sys, random
import pyperclip

for l in range(10):
    x = random.randint(1,10)
    print(x)    
    if x == 10:
        pyperclip.copy('Hello World')
        print(pyperclip.paste())
        print("Goodbye")
        sys.exit()


