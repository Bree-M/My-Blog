#knowing data types is knowing how to control your data
#variables are storage containers and data types are the ingredients.
#int,float,str,bool,list,tuples,dict and sets are the various datatypes.
#Data types tell Python what your data can do. Treat them right, and they’ll carry your whole program.

age = "23" #conversions like these changing string to and integer
year = 2025
converted_age = int(age) 

print(int(age) + 1)

birth_year = "2001"
current_year = 2025

age = current_year - int(birth_year) #changed string to integer.
print("You are", age,"years old.")
