import random, string

# returns a 100 character ascii string which is a given percentage uppercase
def random_case_string(percent_uppercase, n = 100):
    numUpper = int(n * percent_uppercase)
    numLower = n - numUpper

    s = ""

    for i in range(numUpper):
        s += random.sample(string.ascii_uppercase, 1)[0]

    for i in range(numLower):
        s += random.sample(string.ascii_lowercase, 1)[0]

    return s

def percent_upper_case(s):
    num_upper = sum(map(str.isupper, s))
    percent_upper = float(num_upper) / float(len(s))
    return (s, percent_upper)
