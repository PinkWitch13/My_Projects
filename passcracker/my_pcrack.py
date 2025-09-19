import string
import random



def example_pass_breaker():

    with open("rASCIndomizer/passcracker/example_pass.txt", "r") as file:
        mpass = file.read()
    i = 1
    chars = ["a", "b", "c"]
    max_pass_len = 3
    max_combi = 3**3
    atempt = 0
    combinations = []

    while i < max_combi:
        to_try = "".join(random.sample(chars, max_pass_len))
        combinations.append(to_try)
        print(f"{to_try=}")
        print(f"{combinations=}")
        atempt+=1
        if to_try == mpass:
            print(f"Pasword broken! Your password is {mpass}, guest at {atempt=}")
            break
        else:
            i+=1
    
# example_pass_breaker()




def rASCIndomizer():

    with open("rASCIndomizer/passcracker/example_pass.txt", "r") as file:
        mpass = file.read()
    
    chars = [string.ascii_letters,string.digits]
    ch_number = len(chars)
    i = 1
    max_combi = 3**3
    atempt = 0
    combinations = []

    while i <= max_combi:
        for ch in range(ch_number):
            to_try = "".join(random.sample(chars, i))
            combinations.append(to_try)
            print(f"{to_try=}")
            #print(f"{combinations=}")
            atempt+=1
            if to_try == mpass:
                print(f"Pasword broken! Your password is {mpass}, guest at {atempt=}")
                break
            else:
                i+=1
                continue

rASCIndomizer()

# # import math

# chars = ["a", "b", "c"]

# chars = list(string.ascii_letters + string.digits)
# cl = len(chars)
# mcn = cl**cl
   

# i = 1
# atempt = 0
# checked_combi = list()

# with open("My_Projects/passcracker/example_pass.txt", "r") as file:
#     mpass = file.read()

# while i <= mcn:
#     for p, char in enumerate(chars):
#         to_try = "".join(random.sample(chars, i))
#         checked_combi.append(to_try)
#         if to_try in checked_combi:
#             continue
#         else:
#             checked_combi.append(to_try)
#             atempt+=1
#             if to_try == mpass:
#                 print(f"Password broken! Your password is {mpass}")
#                 break
#             else:
#                 i+=1
#                 print(to_try, f"{atempt=}")


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

# chars = ["a", "b", "c"]