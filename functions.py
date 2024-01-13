def say_hello(person1, person2):
    print("Hello " + person1 + "," + " how are you doing? " + person2 + " is waiting for you.")

say_hello("Hamxah" , "Adamz")
say_hello("Danny", "Aisha")

def fahr2celsius(fahr):
    celcius = (5 * (fahr -32)) / 9
    return celcius

input("Celcius: ", round(fahr2celsius(100),2))
print("kelvin: ", round(fahr2celsius(100) + 273.5 ,2))
