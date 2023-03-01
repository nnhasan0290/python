import numpy as np
from numpy import random

arr = np.array([2, 3, 4, 5, 6, 7])

# per = random.permutation(arr)

random.shuffle(arr)

print(arr)