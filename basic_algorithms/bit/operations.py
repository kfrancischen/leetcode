# delete the last 1 in the binary form

def deleteLastOne(n):
    return n & (n -1)

# this returns the value of n*2 (can change 1 to m to get 2**m)
def multiplyByTwo(n):
    return n << 1

# this returns the value of n/2 (can change 1 to m to get 2**m)
def dividedByTwo(n):
    return n >> 1

# check whether it is an odd number
def checkOdd(n):
    return n & 1 == 1

# get the m-th bit of n (from left to right)
def getmthBit(m, n):
    return (n >> (m-1)) & 1

# set the m-th bit of n to 0 (from left to right)
def setmthBitToZero(m, n):
    return n & ~(1 << (m-1))

# if x == a, x = b; if x == b, x = a
def exchange(a, b, x):
    return a ^ b ^ x

# remove the last set bit:
def removeLastSetBit(n):
    return n - (n & (-n))

# add 1 to the last set bit: 1011 -> 1100, 1001->1010
def addOneToLastSetBit(n):
    return n + (n & (-n))

n = 10
print deleteLastOne(n)
print multiplyByTwo(n)
print dividedByTwo(n)
n = 11
print checkOdd(n)

n = 8
m = 2
print getmthBit(m ,n)

n = 7
m = 2
print setmthBitToZero(m, n)

x = a = 3
b = 2
print exchange(a, b, x)

n = 10
print removeLastSetBit(n)
print addOneToLastSetBit(n)
