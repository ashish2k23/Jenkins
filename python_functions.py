import os


def print_name(name, age):
    return print(f"My name is {name} and age {age}")


name = os.getenv("input1")
print_name(name, 40)
print_name('Akansha', 36)

