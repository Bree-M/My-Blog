#rollercoaster of code
#the two types of loops is the for loop and while
#python starts counting from 0, in for loop it loops through things like a list and string and others.

for i in range(5):
    print("I love you Renee")

#while loop is when you're not sure how many times to loops it, the loop will keep on as long as the condition is true.

count = 0

while count < 3:
    print("Yes we still going")
    count += 1

#to make sure the loop stops in case of forgetting, a break is included
#break skips the loop
# continue skips the iteration and continues
# pass is a placeholder

for i in range (5):
    if i == 3:
        break
    print(i)    

chores = ["dishes", "laundry","sweep", "feed cats"]

for task in chores:
    if task == "feed cats":
        print("peak of the day")
    else:
        print(f"Ugh... gotta do the {task}")    