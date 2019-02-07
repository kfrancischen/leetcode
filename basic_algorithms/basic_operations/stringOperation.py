def reverseString(s):
    return s[::-1]


def changeToBinary(num):
    return "{0:b}".format(num)

def binaryToInt(s):
    return int(s, 2)

def toLowerCase(s):
    return s.lower()

def toUpperCase(s):
    return s.upper()

def leftFind(s, char):
    return s.find(char)

def rightFind(s, char):
    return s.rfind(char)

def checkDigit(s):
    return s.isdigit()

def checkAlphabet(s):
    return s.isalpha()

def checkAlphaNumeric(s):
    return s.isalnum()







s = "hello word"
s_upper = "HELLO WORLD"
num = 10
print reverseString(s)
print changeToBinary(num)
print binaryToInt('1010')
print toLowerCase(s_upper)
print toUpperCase(s)
print leftFind(s, 'o')
print rightFind(s, 'o')
print checkDigit('1010')
print checkAlphabet("helloworld")
print checkAlphaNumeric(s)
