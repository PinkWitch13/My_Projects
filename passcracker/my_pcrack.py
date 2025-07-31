# import string
import random
# import math

with open("My_Projects/passcracker/example_pass.txt", "r") as file:
    mpass = file.read()
    print(mpass)

# chars = list(string.printables)
# char_len = len(chars)
# max_pass_len = math.pow(char_len, char_len)

# i = 1

# for i in max_pass_len:
#     posi_pass = set()


# l = 1

# while l <= max_pass_len:
#     try_combi = set()
#     for c in range(l):
#         try_pass = str(random.shuffle(chars))
#         try_combi.add(try_pass)
#         print(try_combi)
# print("CANNOT BREAK PASSWORD :(")

chars = ["a", "b", "c"]
max_pass_len = 3

max_combi = 3**3

i = 1
print(f"'{mpass}'")
while i < max_combi:
    to_try = "".join(random.sample(chars, max_pass_len))
    if to_try == mpass:
        print(f"Pasword broken! Your password is {mpass}")
        break
    else:
        i+=1
        print(to_try, mpass)