import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

my_sequential = list()
for i in range(10):
    my_sequential.append(i+1)

# """
# Print a message to the console indicating whether each value of
# `number` is in the `my_randoms` list.
# """
# for number in range(1, 6):
#     if my_randoms.count(number) >= 1:
#         print(f"my_randoms list contains {number}")
#     else:
#         print(f"my_randoms list does not contain {number}")


num_list = range(1,10)

for number in num_list:
    contains = False
    for ranNum in my_randoms:
        if ranNum == number:
            contains = True
    print(
        f"my_randoms list {f'does contain {number}' if contains else f'does not contain {number}'}"
    )