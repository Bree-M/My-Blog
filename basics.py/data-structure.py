#list & tuples is python storage basket
#lists are versatile and tuples cannot be changed or edited like lists can.

#declaring a list
fruits = ["apple", "banana", "mango"]
print(fruits[0])#accessing fruits according to where they are in the list
print(fruits[-1])#shows the last item (total number of items subtract one)

fruits[1] = "kiwi"
print(fruits)#replaces the first item on the list wuth kiwi

#adding to the list
fruits.append("pineapple")

#inserts the fruits to the specified position in the list.
fruits.insert(1, "grapes")

#removing from the list
fruits.remove("apple")#removes apple
fruits.pop()#removes last item from the list
fruits.pop(1)#removes itema at index 1

#sorting alphabetically
fruits.sort()

#reverses the order
fruits.reverse()
print(fruits)

#getting the number of items
print(len(fruits))

#checking if item exists
if "banana" in fruits:
    print("Banana in the bunch")
else:
    print("Houston we got a problem")    

#TUPLES
# this is a list but a fixed one, you cannot add,remove or replace.

#declaring a tuple
colors = ("red", "blue", "green")     

#exhibit A
name, age = ("Renee", 23)
print(name)
print(age)

#Lists are for moods that change.
# Tuples are for promises you made and meant to keep.

playlist = ["Afrobeats", "Amapiano", "Pop"]
playlist.append("EDM")

genres = ("Hip-Hip","Soul", "RnB")#cannot change

print("Genres:", genres)
print("Playlist:", playlist)

#DICTIONARIES & SETS

