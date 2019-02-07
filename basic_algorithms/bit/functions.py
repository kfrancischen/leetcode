# this function computes the sum of two positive numbers

def getSumPositive(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a


# this function computes the subtraction of two positive numbers
def getSubstractionPositive(a, b):
    while b:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1

    return a

# this function returns the negative number of a: -a
def getNegative(a):
    return ~a + 1

# this function computes the sum of two integers

def getSum(a, b):
    if a * b < 0:
        if a > 0:
            return getSum(b, a)
        if getSumPositive(~a, 1) == b: # -a == b
            return 0
        if getSumPositive(~a, 1) < b: # -a < b
            return getSumPositive(~getSumPositive(getSumPositive(~a, 1), getSumPositive(~b, 1)), 1) # -add(-a, -b)

    return getSumPositive(a, b)

print getSumPositive(1,2)
print getSum(-3, 4)
print getSum(-100, 1)
print getSubstractionPositive(10, 2)
print getNegative(-4)
