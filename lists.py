
users = ["Hamxah", "Adamz", "iliya", "Fideh"]

data = ["Hamxah", "22"]

users[2:2] = ["Danny", "Muhammad"]
print(users)

users[1:3] = ["Aisha", "Musa"]
print(users)
users.remove("Musa")
print(users)

users[1:2] = ["isa"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [89,54,24,98,12,4,1,2]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# global sorted func
print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
mylist = list(["Danny", 17, True])
print(mylist)

mytuple = (("Hamxah",22,True))
anothertuple = (1,2,3,4,7)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Sadeeq")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)










