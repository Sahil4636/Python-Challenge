first_name = "Sahil"
Last_name = "Dhanvij"
country = "India"
City = "Nagpur"
age = "21"
is_married = False
skills = ["Python", "Excel", "SQL", "Power Bi", "Tableau"]
Person_info = {
    'firstname': 'Sahil',
    'Lastname':'Dhanvij',
    'Country': 'India',
    'City': 'Nagpur'
}

print(len("Hello, World!"))

print("First Name:" , first_name)
print("First Name Length:",len(first_name))
print("Last Name:", Last_name)
print("Last Name Length :", len(Last_name))
print("Country:", country)
print("City:", City)
print("Age:", age)
print("Is Married:", is_married)
print("Skills:", skills)
print("Person Information:",Person_info )

# Declaring Multiple Variable in a Line

First_name, last_name, Country, Age, Is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 21, True
print(First_name, last_name, Country, Age, Is_married)
print('First name:', First_name)
print('Last name:', last_name)
print('Age:', Age)
print('Married:', Is_married)

# Data Types 
print(type(10)) # Int
print(type(3.14)) # Float
print(type(1+5j)) # complex 
print(type("Hello")) # string
print(type([1,2,3])) # list
print(type({'name':"Sahil"})) # dictionary
print(type({9.8, 3.14, 2.7})) # tuple
print(type(True)) # Boolean
print(type(zip([1,2],[2,3])))