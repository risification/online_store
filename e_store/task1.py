customers = ['brad', 'jolie', 'johny', 'sooronbai', 'sooronbai', 'sadyr', 'sadyr', 'emma', 'sooronbai',
             'brad', 'almazbek', 'roza', 'roza', 'kurmanbek', 'toby', 'tony', 'robert', 'askar', 'robert', 'chris',
             'chris']


import random
import math
list1 = random.sample(range(1,1000000),600000)

a = list1.index(max(list1))
b = list1.index(min(list1))
if a >b:
    c = a - b
else:
    c = b -a
print(c)

fact = math.factorial(400000)
result = fact / (fact*math.factorial(10))
print(result)