# def recursive_linear(arr, x, index):
#     if index > len(arr) - 1:
#         msg = print('not found')
#         return msg
#     if arr[index] == x:
#         msg = print('found')
#         return msg

#     index += 1
#     recursive_linear(arr, x, index)


# array = [1, 2, 3, 4, 5]
# n = -5
# i = 0

# recursive_linear(array, n, i)

def test_array():
    arr = [1, 4, 6, 3, 7]
    arr.sort()
    arr.pop(0)
    arr.append(4)
    arr.extend(arr)

    print(arr)


test_array()
