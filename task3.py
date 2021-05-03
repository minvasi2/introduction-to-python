'''
6 3 2 8 0 5 4 9 1 3
'''
file_name = 'u1.txt'

input_arr = []
with open(file_name, 'r') as file:
    # input_arr = list(map(int, next(file).split()))
    for line in file:
        for item in line.split():
            input_arr.append(int(item))

output_arr = input_arr + [0] * len(input_arr)

for i, number in enumerate(input_arr, start = 1):
    for index in range(i, 10 - number + i):
        output_arr[index] += 1

print(output_arr)