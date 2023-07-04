intervals = [
    [1, 5],
    [3, 9],
    [4, 8],
    [10, 13]
]
point = 4
count_point = 0
for interval in intervals:
    count = interval[0]
    while count <= interval[1]:
        if count == point:
            count_point += 1
            break
        count += 1

print(count_point)
