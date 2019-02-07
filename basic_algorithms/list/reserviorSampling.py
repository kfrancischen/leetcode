from random import randint
def reserviorSampling(data, k):
    result = []
    for i in range(0, k):
        result.append(data[i])

    for i in range(k, len(data)):
        j = randint(0, i - 1)
        if j < k:
            result[j] = data[i]

    return result

data = [i for i in range(0, 100)]
print reserviorSampling(data, 10)
