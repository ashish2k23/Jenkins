import os


def print_name(name, age):
    return print(f"My name is {name} and age {age}")


TaskID = os.environ['TASK_ID']
ApplicationName = os.environ['APPLICATION_NAME']
print(TaskID)
print(ApplicationName)
print_name('Ashish', 40)
print_name('Akansha', 36)
