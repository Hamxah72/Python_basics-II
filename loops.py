value = 0
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equals to " + str(value))

names = ["Hamxah","Aisha","Adamz","Danny"]
# for x in names:
#     print(x)

# for x in "Misissippi":
#     print(x)
# for x in names:
#     if x == "Adamz":
#         break
#     print(x)

# for x in names:
#     if x == "Adamz":
#         continue   
#     print(x)

# for x in range(100):
#     print(x)
# for x in range(2,8):
#     print(x)
# for x in range(0,101,3):
#     print(x)
# else:
#     print("Glad that's over!")

names = ["Hamxa","Aisha","Adamz","Danny"]
actions = ["codes","Eats","Sleeps"]
for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")