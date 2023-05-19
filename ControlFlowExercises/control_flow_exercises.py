# # 1a
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# y = 0
# last_number = 5
# for i in x:
#     if y < last_number:
#         print(i)
#         y += 1


# # 1b
# for i in x:
#     if i % 2 == 0:
#         print(i)


# # 1c
# for i, n in enumerate(x):
#     if i < 5 and n % 2 == 0:
#         print(n)


# # 2a
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
# for name in names:
#     print(name[0])


# # 2b
# space_index = list()
# for name in names:
#     space_index.append(name.index(" "))
# print(space_index)


# # 2c
# initials = []
# for name in names:
#     initials.append(name[0] + name[name.index(" ") + 1])
# print(initials)

# # 2c 
initials = []
# for name in names:
#     initials.append(name[0] + ". " + name[name.index(" ") + 1])
# print(initials)


# # 3a - convert back to list?
# list_of_lists = [[1,5,7,3,44,4,1],
#                  ["A", "B", "C"],
#                  ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
#                  ["one", "Two", "Three", "Four"]]
# for list in list_of_lists:
#     list_set = set(list)
#     list_unique = []
#     for i in list_set:
#         list_unique.append(i)
#     print(list_unique)


# # 4a
# while True:
#     x = int(input("Input a number greater than 100: "))
#     if x <= 100:
#         continue
#     else:
#         break
# print(x)
   

# # 4b
while True:
    x = int(input("Input a number greater than 100: "))
    if x <= 100:
        continue
    else:
        break
factor = 2
prime = True
while factor < x:
    if x % factor == 0:
        prime = False
        break
    else:
        factor += 1
if prime == True:
    print("prime")
else:
    print("not prime")
    