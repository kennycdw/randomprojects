import random
import pandas as pd

def blackorwhite(n):
    a = []
    for i in range(n):
        b = random.randint(1, 2)
        a.append(b)
    return a


def rockpaperscissors(n):
    a = []
    for i in range(n):
        b = random.randint(1, 3)
        a.append(b)
    return a

def blacksimulation(x, n):
    a = 0
    if n == 1:
        return('not valid bro')
    for i in range(x):
        if blackorwhite(n).count(1) == n / 2:
            a = a + 1
    return a / x * 100

# x refers to the total sample size you want to test (you want it to be as large as possible) and n refers to the number of players on the court


def rocksimulation(x, n):
    a = 0
    if n == 1:
        return('not valid bro')
    for i in range(x):
        c = rockpaperscissors(n)
        if c.count(1) == n / 2 or c.count(2) == n / 2 or c.count(3) == n / 2:
            a = a + 1
    return a / x * 100

def rockseries(n):
    z=[]
    for i in range(n):
        if (i+1)%2==0:
            a=rocksimulation(100000,i+1)
            z.append(a)
    return z

def blackseries(n):
    z=[]
    for i in range(n):
        if (i+1)%2==0:
            a=blacksimulation(100000,i+1)
            z.append(a)
    return z



blackseries(100)

