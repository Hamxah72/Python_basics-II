blog_posts = ["", "The ten coolest functions in python.", "How to make HTTP requests in python.", "", "A tutorial about data types in python."]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print("-----------------------")

myString = "This is a string"

for char in myString:
    print(char)

print("------------------------")

for x in range(0,10):
    print(x)

print("------------------------")

person = {
    "Name": "Aishah M Sani", "Age": 20, "Gender": "Female"
}
person["Religion"] = "Islam"
person["Marital_status"] = "Single"
for key in person:
    print(key, ":", person[key])

print("------------------------")

blog_posts = {
    "Python": ["The ten coolest functions in python.", "How to make HTTP requests in python.", "A tutorial about data types in python."], "Javascript": ["Namespace in Javascript.", "New function available in ESG."]
    }

for category in blog_posts:
    print("Post about", category)
    for post in blog_posts[category]:
        print(post)