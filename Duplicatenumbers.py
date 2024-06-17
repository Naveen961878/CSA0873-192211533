def remove_duplicates_sorted_array(arr):
    if not arr:
        return []  
    unique_elements = [arr[0]]  
    last_seen_element = arr[0]  
    for num in arr:
        if num != last_seen_element:
            unique_elements.append(num)  
            last_seen_element = num 
    return unique_elements
sorted_array = [15,14,14,14,25,32,32,31]
unique_elements = remove_duplicates_sorted_array(sorted_array)
print("Unique elements:", unique_elements)
