def bubblesort(list):
    while True:
        done = True
        for index in range(len(list)-1):
            if list[index] > list[index + 1]:
                list[index], list[index + 1] = list[index + 1], list[index]
                done = False
        if done:
            return list