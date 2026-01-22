file = open ("ali.txt", "r")
with open("ali.txt", "r") as file:  
    content = file.read()
    print(content)

with open("ali.txt", "w") as file:
    file.write("Hello, World!")

with open("ali.txt", "a") as file:
    file.write("\nAppended line.")
file.close()

