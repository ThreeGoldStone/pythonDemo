nums = [50000, 1, 5, 9, 4, -2, 55, 98, 1000, 500, 1, 40000]
nums2 = [50000, 40000, 1000, 500, 98, 55, 9, 5, 4, 1, 1, -2]


def bubble_sorting(lst):
    count = 0
    count_swap = 0
    lenth = len(lst)
    for i in range(lenth):
        for j in range(i, lenth):
            i_value = lst[i]
            j_value = lst[j]
            count += 1
            if i_value < j_value:
                count_swap += 1
                lst[i], lst[j] = j_value, i_value
    print(count, count_swap)


def bubble_sorting_better(lst):
    count = 0
    count_swap = 0

    lenth = len(lst)
    for i in range(lenth):
        flag = False
        for j in range(lenth - i - 1):
            i_value = lst[j]
            j_value = lst[j + 1]
            count += 1
            if i_value < j_value:
                count_swap += 1
                flag = True
                lst[j], lst[j+1] = j_value, i_value
        if not flag:
            break
    print(count, count_swap)


print(nums2)
# bubble_sorting(nums)
bubble_sorting_better(nums)
print(nums)
