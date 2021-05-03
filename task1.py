# print(sum(map(int, input('Iveskite skaiciu: '))))

number = input('Iveskite skaiciu: ')

number_sum = 0

for symbol in number:
    number_sum += int(symbol)
    
print(number_sum)

