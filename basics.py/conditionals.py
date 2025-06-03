#code makes a condition, if it's raining, i'll take an umbrella else, i'll stand in the rain.
#using if and else 
#if condition:
    # do this if condition is True
# elif another_condition:
#     # do this instead if the first isn't true but this is
# else:
#     # do this if none of the above are True

weather = "sunny"

if weather == "sunny":
    print("Let's hit the beach!")
elif weather == "rainy":
    print("Grab your umbrella")
else:
    print("Netflix and code")        

#exhibit B
is_nice = False
prays_for_me = False

if is_nice and prays_for_me:
    print("He's a green light!")
elif is_nice:
    print("He's a beige")
elif prays_for_me:
    print("We standing on beige")    
else:
    print("Girl,run!")    


#Nested if is like an inner thought, a condition inside a condition.

age = 18
has_ID = False

if age >= 18:
    if has_ID:
        print("You can enter")
    else:
        print("No ID,no entry")
else:
    print("Too young, come back in due years.")        


#Operator + Conditionals
temp = 25
if temp > 30 or temp < 10:
    print("Extreme weather alert") 
else:
    print("Weather's chill")       

#Python conditionals are the moral compass of your code — they decide who gets the blessings and who gets the else.    