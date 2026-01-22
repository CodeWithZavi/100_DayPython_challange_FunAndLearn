# # # # # # # # # # #all these are basic concepts in python programming so no need to write them down will write the important ones only

# # # # # # # # # # # a = input("Enter a number: ")
# # # # # # # # # # # b = input("Enter another number: ")
# # # # # # # # # # # name = input("Enter your name: ")

# # # # # # # # # # # print(f"Hello, {name}! The sum of {a} and {b} is {int(a) + int(b)}.")

# # # # # # # # # # # a = int(input("Enter a number: "))
# # # # # # # # # # # name  = str(input("Enter your name: "))
# # # # # # # # # # # print(a,name)

# # # # # # # # # # # name =  "Sardar Zavian" # - it count from backside
# # # # # # # # # # # # print(name[0:6])
# # # # # # # # # # # # print(name[-5:-1])
# # # # # # # # # # # # print(name[0:-3])
# # # # # # # # # # # # print(name[-6:]) 
# # # # # # # # # # # # print(name[-6:len(name)])

# # # # # # # # # # # # print(name[1:8])
# # # # # # # # # # # ok = "harry"
# # # # # # # # # # # print(ok[-4:-2])

# # # # # # # # # # name = "saradr Zavian"   
# # # # # # # # # # print(name.split(" ")) #makes a list by splitting the string at spaces
# # # # # # # # # # print(name.replace("sardar", "Sardar")) #replaces sardar with Sardar
# # # # # # # # # # print(name.lower()) #makes all letters lowercase    


# # # # # # # # # if 3>1:
# # # # # # # # #     print("3 is greater than 1")
# # # # # # # # # print("This is not part of if statement")
# # # # # # # # # # spaces matter in if else in python

# # # # # # # # def time(hour):
# # # # # # # #     if hour<12:
# # # # # # # #         return "Good morning"
# # # # # # # #     elif hour<18:
# # # # # # # #         return "Good afternoon"
# # # # # # # #     else:
# # # # # # # #         return "Good evening"

# # # # # # # # print(time(10))

# # # # # # # Match case featrure in python 3.10 and above
# # # # # # def day_message(day):
# # # # # #     match day:
# # # # # #         case "Monday":
# # # # # #             return "Start of the work week!"
# # # # # #         case "Wednesday":
# # # # # #             return "Midweek already!"
# # # # # #         case "Friday":
# # # # # #             return "Last workday of the week!"
# # # # # #         case _:
# # # # # #             return "Just another day."
        
# # # # # # print(day_message("Monday"))  # it works like switch case in C

# # # # # for k in range(5):  # prints 0 to 4
# # # # #     print(k)

# # # # Person = {
# # # #     "name": "Sardar Zavian",
# # # #     "age": 20,
# # # #     "city": "Islamabad" 
# # # # }
# # # # for p in Person:
# # # #    print(f"{p}: {Person[p]}")  # prints key and value both

# # # # for k in range(1,12,4):  # prints from 1 to 11 with a step of 4
# # # #     print(k)

# # # for i in range(5,10,2):  # prints from 5 to 9
# # #     if i==3:
# # #         continue  # skips the current iteration when i is 3
# # #     print(i)

# # l = (1,2,3,4,5)  # tuple
# # for item in l:
# #     print(item)

# # list = {"apple", "banana", "cherry"}  # set
# # print(item)

# # l=[1,3,1,41]
# # print(l)
# # l.append(6)  # adds 6 at the end of list
# # l.sort()
# # print(l)
# # l.sort(reverse=True)  # sorts in descending order
# # print(l)
# # l.remove(3)  # removes first occurance of 3 
# # print(l)

# # #:
# # m = l  # both m and l point to the same list
# # m.append(9)
# # print("l:",l)   //

# t = {1,2,3}
# p = [1,2,3]
# l = (1,2,3)
# d = { "a":1, "b":2, "c":3 }
# print(type(t))
# print(type(p))
# print(type(l))
# print(type(d))  


