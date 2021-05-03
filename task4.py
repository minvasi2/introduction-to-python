class God:
    def __init__(self, name, points, count):
        self.name = name
        self.points = points
        self.count = count

def read_data(file_name):
    output_data = []
    
    with open(file_name, 'r') as file:
        for line in file:
            tokens = line.split()
            name = tokens[0]
            points = 0
            even_count = 0
            throws = [int(item) for item in tokens[1:]]
            for number in throws:
                if number % 2 == 0:
                    points += number
                    even_count += 1
                else:
                    points -= number
            
            output_data.append(God(name, points, even_count))
        
    return output_data

def get_best(input_data):
    index = 0
    
    for i, data in enumerate(input_data[1:], start = 1):
        if data.points > input_data[index].points or data.points == input_data[index].points and data.count > input_data[index].count:
            index = i
    
    return index

'''
Hermis 6 1 2
Afrodite 6 6 2
Hera 2 6 6
'''
file_name = 'u2.txt'
data = read_data(file_name)
best = get_best(data)  

print(data[best].name, data[best].points)