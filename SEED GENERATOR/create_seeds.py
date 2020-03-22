# Generate List of 100 Seeds

import random

with open('seeds.txt', 'w') as f:
    for i in range(100):
        f.write(str(random.randrange(-9223372036854775808,
                                     9223372036854775807)) + '\n')
