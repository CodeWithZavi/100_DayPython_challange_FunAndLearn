noman = (1,"zavain",12.5)



data = "Zavian", 21, "Engineer" #packing
name, age,job = data  #unpacking

numbers = (1, 4, 2, 3)

print(numbers.count(2))  # how many times
print(numbers.index(1) ) # position  

#Index:   0        1        2  ( in touples)
#Value:  Python   AI   Cybersecurity
#Index:  -3      -2       -1

print("\n")

def square():
    a,b,c = 2,3,1
    return a*2, b*2, c*2;

print(square())



def even(num):
    if num % 2 ==0:
        return True
    else :
        return False
    
print(even(4))
print(even(5))  # None

   