total_number = 1
while total_number < 10:
    print(total_number)
    total_number += 1


# The while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
at_goal = True
count = 0
while at_goal != False:
    print("You have not reached the goal yet")
    if count > 10:
        at_goal = False
    count += 1
print("You have reached the goal")

# The above code can be written as:
at_goal = False
while not at_goal:
    print("You have not reached the goal yet")
    if count > 10:
        at_goal = True
    count += 1
print("You have reached the goal")
