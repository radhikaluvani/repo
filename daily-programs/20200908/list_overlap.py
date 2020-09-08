import random
a = random.sample(range(1, 50), 14)
b = random.sample(range(1, 50), 19)
c = print([i for i in a for j in b if i == j])