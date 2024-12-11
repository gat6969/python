# 1. Create a tuple of 5 fruits
fruits_tuple = ('apple', 'banana', 'cherry', 'mango', 'orange')
print("Original tuple:", fruits_tuple)

# 2. Convert the tuple into a list and add a new fruit
fruits_list = list(fruits_tuple)  # Convert tuple to list
fruits_list.append('grape')  # Add a new fruit
print("After adding a new fruit:", fruits_list)

# 3. Create another list of berries and merge both lists
berries = ['blueberry', 'strawberry', 'raspberry']
merged_list = fruits_list + berries  # Merge both lists
print("Merged list:", merged_list)

# 4. Convert the updated list back into a tuple
updated_tuple = tuple(merged_list)  # Convert list back to tuple
print("Updated tuple:", updated_tuple)

# 5. Print the tuple in sorted manner
sorted_tuple = tuple(sorted(updated_tuple))  # Sort the tuple
print("Sorted tuple:", sorted_tuple)

# 6. Find the index of a particular fruit in the tuple
index_of_mango = updated_tuple.index('mango')  # Find the index of 'mango'
print("Index of 'mango' in the tuple:", index_of_mango)
