file = open('file_test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

#alternative method which is better at exception handling
with open('file_test.txt', mode = 'r') as file:
    data = file.readline()

    print(data)