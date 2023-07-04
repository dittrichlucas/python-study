"""
SOLUÇÃO COPIADA
https://www.geeksforgeeks.org/array-rotation/
"""
# arr.reverse()
# print(arr)
arr = [1, 3, 2, 4, 8]
size = len(arr)
index = size - 1
iterator = int(size / 2)

for i in range(0, iterator):
    tmp = arr[index]
    arr[index] = arr[i]
    arr[i] = tmp
    iterator -= 1

print(arr)
