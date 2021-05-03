'''
15 41
1 2 3 4
22 11 24
'''

file_name = 'varzos.txt'

with open(file_name, 'r') as file:
    resistance_total = 0
    
    for line in file:
        tokens = line.split()
        
        suma = 0
        
        for t in tokens:
            suma += 1 / int(t)
        
        resistance_total += 1 / suma
        
    print(round(resistance_total, 2))
