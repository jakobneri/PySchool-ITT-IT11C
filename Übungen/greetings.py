name = input("Please enter your name: ")
vorname = input("Please enter your first name: ")
akademisch = input("Please enter your academic title (optional): ")

def greetings(name, vorname, akademisch=""):
    print(f"Hello, {akademisch} {vorname} {name}, welcome to the greetings module!")
    print("Have a great day!")
    print("Goodbye!")

greetings(name, vorname, akademisch)
print("")
greetings(name, vorname)