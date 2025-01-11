# bubble sort
# go through each element to check current element is greater than next element
# after first iteration we get largest element at the end. so dont need to check that again.


def sort_ls(list: list) -> list:
    for i in range(len(list)-1, 0, -1):  # Loop from the end of the list to the start
        for j in range(0, i):  # Loop through the list up to the unsorted part
            if list[j] > list[j+1]:  # Swap if the current element is greater than the next one
                list[j], list[j+1] = list[j+1], list[j]
    print(list)  # Print the sorted list

ls = [2, 6, 5, 4, 55, 2, 3, 69, 13, 15]
sort_ls(ls)
# 
#  here multiple swaping takeplace in each iteration- less memmory and cpu efficient  