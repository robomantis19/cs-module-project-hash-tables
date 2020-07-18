"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

for i in range(0, len(q) - 3): 
    total = f(q[i]) + f(q[i+1]) + f(q[i+2]) - f(q[i+3])
    print(total)
