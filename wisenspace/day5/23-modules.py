# 1. how to call module
# simplest
import random

t1 = random.random()
print(t1)

t2 = random.randint(1, 10)
print(t2)

"""
# don't want to specify module name
from random import randint
t1 = randint(1, 39)
print(t1)
"""
"""
from random import *
t1 = randint(1, 33)
print(t1)
"""

# alias
"""
import random as r
t1 = r.randint(1, 10)
print(t1)
"""

# ---
# 2. built-in-modules
# random, datetime, math, os, sys

"""
import random, datetime, math, os, sys

print(math.pi)
print(datetime.date.today())
print(datetime.datetime.now())
"""
"""
from datetime import datetime, date, time

d = date(2019, 5, 1)
t = time(12, 30)

t1 = datetime.combine(d, t)
print(t1)
"""
