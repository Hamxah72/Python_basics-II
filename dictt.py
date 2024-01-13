person = {
    "first_name": "Ishaq", "last_name": "Hamza", "birth_year": "2001", "place_of_birth": "Nigeria", 
}
print(person)
print(type(person))

print(person["last_name"])
person["marital_status"] = "Single"
print(person)

person["children"] = ["Adamz", "Danny"]
print(person)
person["children"].append("Aisha")
print(person)

# print(person["age"])
print(person.get("age", "invalid property"))
person["age"] = "22"
print(person)

print(person.clear())