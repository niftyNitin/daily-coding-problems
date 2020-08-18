import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

# Driver code
stream = [9, 10, 15, 17, 25, 55]
n = len(stream)

# use different seed value for every run
print("Random number is", pick(stream))
