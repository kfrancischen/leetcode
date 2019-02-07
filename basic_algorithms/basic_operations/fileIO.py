
import os.path

fileName = 'test.txt'

# read by line
print "the first"
with open(fileName) as f:
    for line in f:
        print line

# read by bulk
print "the second"
with open(fileName) as f:
    print f.read()



# read by buffer size:
print "the third"
buffersize = 1024
with open(fileName) as f:
    while True:
        buf = f.read(buffersize)
        if not buf:
            break
        print buf


if os.path.exists('tes.txt'):
    print "yes"
else:
    print "no"
