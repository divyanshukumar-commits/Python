def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


greet("Divyanshu")
print(get_greeting("Divyanshu"))

message = get_greeting("Divyanshu")
file = open("content.txt", "w")
file.write(message)
