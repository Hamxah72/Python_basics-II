
def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(18,2)   
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Hamxah", "Adamz", "Fideh", "Moh")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items   (first="Ishaq", last="Hamxah")

    