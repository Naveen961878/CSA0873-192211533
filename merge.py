def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0 
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list
list1 = [1, 2, 4]
list2 = [0, 3, 6]
merged_list = merge_sorted_lists(list1, list2)
print("Merged List:", merged_list)
second_largest = merged_list[-2]
print("2nd Largest Number:", second_largest)
four_smallest = merged_list[:4]
print("4 Smallest Numbers:", four_smallest)
reverse_order = merged_list[::-1]
print("Numbers in Reverse Order:", reverse_order)
