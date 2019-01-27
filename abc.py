# import numpy as np
import random

list_answer = []

local = []

list_show = []


for i in range(0,64):
    while True:
        result = random.randint(1,64)
        if result not in list_show and result not in list_answer:
            list_show.append(result)
            break

print( list_show)