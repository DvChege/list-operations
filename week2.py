# Step 1: Create an empty list
my_list = []
print("Initial list:", my_list)

# Step 2: Append elements to the list
elements_to_append = [10, 20, 30, 40]
for item in elements_to_append:
    my_list.append(item)
print("After appending 10, 20, 30, 40:", my_list)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# Step 4: Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element
removed_element = my_list.pop()
print(f"After removing the last element ({removed_element}):", my_list)

# Step 6: Sort the list in ascending order
my_list.sort()
print("After sorting the list in ascending order:", my_list)

# Step 7: Find and print the index of the value 30
try:
    index_of_30 = my_list.index(30)
    print("Index of 30:", index_of_30)
except ValueError:
    print("Value 30 is not in the list.")
