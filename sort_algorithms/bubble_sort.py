data = input("Enter array that should be sorted: ")

array = list(map(int, data.split()))

for i in range(len(array)):
    swapped = False
    for j in range(len(array)-i-1):
        if(array[j]> array[j+1]):
            array[j], array[j+1] = array[j+1],array[j]
            swapped = True

    if not swapped:
        break

print(array)