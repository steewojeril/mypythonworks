# first find the min value .
# then swap that value with first . so fist value fixed. then do the same thing for remaining

#  here swaping takeplace at once in an iteration

def sort_ls(list: list) -> list:
    for i in range(len(list)):
        min_pos = i  # Assume the current position has the smallest value
        for j in range(i + 1, len(list)):  # Check the rest of the list
            if list[j] < list[min_pos]:  # Find the minimum value
                min_pos = j
        # Swap the smallest value found with the element at index i
        list[i], list[min_pos] = list[min_pos], list[i]

    print(list)

ls = [2, 6, 5, 4, 55, 2, 3, 69, 13, 15]
sort_ls(ls)
