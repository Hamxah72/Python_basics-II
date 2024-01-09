
band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items 
print(band["vocals"])
print(band.get("guitar"))

print(band.keys())
print(band.values())

band2 = dict(band)
print("Good Copy!")
print(band2)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# SETS

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

nums.add(9)
print(nums)

morenums = {5,6,7,8}
nums.update(morenums)
print(nums)

# You can use update on sets,lists, and tuples too

# Merge two sets to create 2 
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates 
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)