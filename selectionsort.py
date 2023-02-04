def sort(numbers):

    for i in range(9):
        minpos = i

        for j in range(i,10):
            if numbers[j] < numbers[minpos]:
                minpos = j
        
        swap = numbers[i]
        numbers[i] = numbers[minpos]
        numbers[minpos] = swap

        print(numbers)

numbers = [77, 93, 56, 98, 41, 17, 80, 7, 39, 57]
sort(numbers)

print(numbers)

//code complete