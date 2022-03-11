import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('Width and Height need to be greater than 1')
    print (symbol * width)

    for i in range (height-2):
        print(symbol + (' ' * (width -2)) + symbol)

    print (symbol * width)


try:
    boxPrint('*', 1, 1)
    raise Exception('This is an error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback info was written to error_log.txt')


#boxPrint('*', 10, 10)
#boxPrint('*', 1, 1)

