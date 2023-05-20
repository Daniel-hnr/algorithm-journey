def find_smallest(arr:list):
    smallest_num = arr[0]
    smallest_num_index = 0
    for i in arr:
        if i < smallest_num:
            smallest_num = i
            smallest_num_index = arr.index(i)
    return smallest_num_index
def sort(arr:list):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[find_smallest(arr)])
        arr.pop(find_smallest(arr))
    return new_arr


print(sort([5,848,11,4,21,4,15,18,184,8,9,10,15,484,48,5,4,7,484,595,48]))