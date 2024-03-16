names = ["ryan", "yonatan"]
names.append("maor") #add a new value(value)
print(names)
names.clear() #clear the list
names.append("alon")
print(names)

#----------------------------------------------------------------------------------------------------------------

for i in range(1, 10, 2): #a for loop that start from 1 to 10 in jumps of 2
    print(i)

#----------------------------------------------------------------------------------------------------------------
    
try: #trying the code
    age = input("enter your age")
    age = int(age)
except ValueError as e: #if the code in "try" is not working there is a value error and we called the name of the error "e". now do the code that under this line
    print("invild value")
    print(e)# print the error


print("exit")


#----------------------------------------------------------------------------------------------------------------

customer = { #A dictionary type variable
    "name" : "ryan shaar", "age" : 17, "email" : "blabla@gmail.com"
}

print(customer)
print(customer["email"])


#----------------------------------------------------------------------------------------------------------------