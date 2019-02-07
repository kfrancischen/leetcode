# Brian Kernighan algorithm
# this algorithm computes the number of 1's in an integer
# this algorithm also tells aways to delete the trailing 1 one by one

def count_set_bits(n):
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count


n = 11
print count_set_bits(n)
