def bubbleSort(lst):
    for bb in range(len(lst)-1, 0, -1):
        for i in range(bb):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i];
    return lst

list = [27, 0, 71, 70, 27, 63, 90];
print(bubbleSort(list));
