person = {
    "name": "Adamz Musa", "gender": "Male", "age": "20", "address": "Jalingo", "phone": "07044908801"
}
key = input("What information do you want to know about the person? ").lower()

result = person.get(key, "That info is not available")
print(result)

