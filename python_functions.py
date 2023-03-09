import os


def print_name(name, age):
    return print(f"My name is {name} and age {age}")


TaskID = os.environ('TASK_ID')
print(TaskID)
print_name('Ashish', 40)
print_name('Akansha', 36)
