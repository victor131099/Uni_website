
# Running this python code will execute a random user test.

import random

random_num = random.randint(1, 8)
print(random_num)
random_user = 'user{}.py'.format(random_num)

exec(open('Users/' + random_user).read())
