import sys

max_count = ['0', 0]
for row in sys.stdin:
    count = 0
    row = row.split('=')
    row[-1] = row[-1][:-1:]
    for num in row:
        if int(num) % 2 != 0:
            count += 1
    if count > max_count[1]:
        max_count = [row, count]

max_count_nch = []
for i in max_count[0]:
    if int(i) % 2 != 0:
        max_count_nch.append(i)


print(max_count_nch)