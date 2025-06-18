original_array = [1,2,4,6,5]
new_array = [x + 2 for x in original_array if x + 2 > 5]

print("Original_array:",original_array)
print("New_array:", new_array)