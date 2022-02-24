def lenFunc(string):
    print (string +  ' has ' + str(len(string)) + ' letters in it.')

def div42by (diveBy):
    try:
        return 42 / diveBy
    except ZeroDivisionError:
        print('Error:  You divided by Zero')

def numCatsFunc(numCats):
    try:
        if int(numCats) >= 4:
            print("that is a lot of cats")
        elif int(numCats) < 0:
            print("cmon, you can't have negative cats")
        else:
            print("that isn't too many cats")
    except ValueError:
        print("you didn't enter a number")


print("How many cats you got?")
a = input()
numCatsFunc(a)

#lenFunc('dog')
#lenFunc('rate')

#print (div42by(2))
#print (div42by(12))
#print (div42by(0))
#print (div42by(12))adsf