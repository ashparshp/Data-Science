import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia"]
print(states_of_america)
print(states_of_america[0])
print(states_of_america[-1])

states_of_america.append("AngelaLand")
print(states_of_america)

states_of_america.extend(["AshparshLand", "Jack Bauer Land"])
print(states_of_america)

states_of_america.insert(1, "Jack Bauer Land")
print(states_of_america)

states_of_america.remove("Jack Bauer Land")
print(states_of_america)

# Challenge: Who's Paying the Bill?
friends = ["Angela", "Jack", "Michael", "John", "Jack", "Lily", "Jack"]
whose_turn = random.choice(friends)
print(f"{whose_turn} is going to buy the meal today!")

# Example: Sorting the list
states_of_america.sort()
print("Sorted list of states:", states_of_america)

# Example: Reversing the list
states_of_america.reverse()
print("Reversed list of states:", states_of_america)

# Example: Counting occurrences of an element
count_jack = friends.count("Jack")
print(f"Jack appears {count_jack} times in the friends list")

# Example: Finding the index of an element
index_of_georgia = states_of_america.index("Georgia")
print(f"Georgia is at index {index_of_georgia} in the states list")


# List Errors
# IndexError: list index out of range
# states_of_america[50]

# IndexError: list index out of range
# states_of_america[10] = "New York"

# AttributeError: 'str' object has no attribute 'append'
# states_of_america.append("New York")

# AttributeError: 'str' object has no attribute 'extend'
# states_of_america.extend("New York")
