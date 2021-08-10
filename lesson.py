import random

print("HELLO!!")

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[i] > array[j] :
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
    return array



array = []
for i in range(10):
    array.append(random.randint(0, 10))
print(array)
new_array = bubble_sort(array)
print(new_array)