def binary_search(target_list, target_num):
    count = 0
    low = 0
    high = len(target_list) - 1
    mid = (high + low) // 2
    res = target_list[mid]
    while True:
        if res > target_num:
            high = mid - 1
        elif res < target_num:
            low = mid + 1
        else:
            break
        mid = (high + low) // 2
        res = target_list[mid]
        count += 1
        print(res)
    return [res, count]

num_list = list(range(0, 100000000))
print(binary_search(num_list, 200))

