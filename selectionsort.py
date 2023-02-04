def sort(numbers):

    for i in range(99):
        minpos = i

        for j in range(i,100):
            if numbers[j] < numbers[minpos]:
                minpos = j
        
        swap = numbers[i]

