# Youtube URL: https://youtu.be/mBgy0oSQu94
# ✅ Exercise 1 - Let's generate 10 values between 5 and 50. Store those values on a list.random

# my_list = []

# for _ in range (10):
#   rand_num = random.randint(5, 50)
#   my_list.append(rand_num)

# print(my_list)

# ✅ Exercise 2 - Let's generate 20 odd values between 0 and 100
# my_list = []

# for _ in range(20):
#   num = random.randrange(0, 100, 2)
#   my_list.append(num)

# print(my_list)

# ✅ Exercise 3 - Generate 10 random numbers multiple of 5
# for _ in range(10):
#   rand_num = random.randint(1, 10)*5
#   print(rand_num)

# ✅ Exercise 4 - Let's generate a list with 20 sequential numbers. You have to present it in a ramdon order (Randomized).

import random
# from random import shuffle

# some_nums = [i for i in range(1, 21)]
# print(some_nums)
# random.shuffle(some_nums)
# print("Randomized: \n ", some_nums)

# Using Generator expression:
# some_nums2 = list(i for i in range(1, 11))
# print(some_nums2)
# random.shuffle(some_nums2)
# print("Randomized: \n ", some_nums2)

# Using For Loop:
my_list = []
for i in range(1,21):
   my_list.append(i)
print(my_list)
random.shuffle(my_list)
print("Randomized: \n ", my_list)