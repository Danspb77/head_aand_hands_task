import random

def sort_massives(main_mas):

    for element in range(0,len(main_mas),2):
        main_mas[element]=merge_sort(main_mas[element])
    for element in range(1,len(main_mas),2):
        main_mas[element]=merge_sort(main_mas[element])
        main_mas[element]= main_mas[element][::-1]

    return main_mas

def merge_sort (arr):
    # базовый случай: если массив состоит из одного элемента или пуст, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # разделяем массив пополам
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # рекурсивно сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # сливаем отсортированные половины
    return merge_arrays(left_sorted, right_sorted)
    

def merge_arrays(left, right):
    merge_array=[]
    l=len(left)
    r=len(right)
    i=0
    j=0
    while i<l and j <r:
        if left[i]<=right[j]:
            merge_array.append(left[i])
            i+=1
        else:
            merge_array.append(right[j])
            j+=1
    while i <l:
        merge_array.append(left[i])
        i+=1
    while j <r:
        merge_array.append(right[j])
        j+=1
    return merge_array

def create_massives(n):
    # this massive will contain little massives
    main_mas=[]
    
    # generate lens of little massives  
    numbers = list(range(1, n+1))
    random.shuffle(numbers)

    # generate n little massives
    for i in range(n):
        m=[]
        # choose len of little massive
        little_mas_len=numbers[i]


        # fill little massive
        for j in range(1,little_mas_len+1):
            a=random.uniform(1,10)
            m.append(a)
        main_mas.append(m)
    main_mas=sort_massives(main_mas)    
    return main_mas

print(create_massives(5))






print(merge_arrays([3,9],[2,3,6]))

