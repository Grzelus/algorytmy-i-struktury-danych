data = input("Enter array that should be sorted: ")

array = list(map(int,data.split()))

for i in range(len(array)-1):
    min_index  = i
    for j in range(i+1, len(array)):
        if(array[j] < array[min_index]):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]



print(array)