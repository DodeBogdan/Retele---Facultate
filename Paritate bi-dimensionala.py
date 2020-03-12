import sys

def verify_input(input):
    if len(input) % 7 is not 0:
        return False
    for index in range(len(input)):
        if input[index] is not '0' and input[index] is not '1':
            return False
    return True


def verify_paritate(input):
    numberOfOne = 0
    for index in input:
        if index == '1':
            numberOfOne += 1
    return numberOfOne % 2


def transform_matrix(input):
    matrix = []
    string = input[0]
    for index in range(1, len(input)):
        if index % 7 == 0:
            matrix.append(string)
            string = ''
        string += input[index]
    matrix.append(string)
    return matrix


def transform_line(matrix):
    new_matrix = []
    for index in matrix:
        index += str(verify_paritate(index))
        new_matrix.append(index)
    return new_matrix


def transform_column(matrix):
    string = ''
    new_matrix = matrix
    for index in range(len(matrix[0])):
        numberOfOne = 0
        for word in matrix:
            if word[index] is '1':
                numberOfOne += 1
        string += str(numberOfOne % 2)
    new_matrix.append(string)
    return new_matrix


first_message = '110100101010011010111'
if not verify_input(first_message):
    sys.exit()

first_matrix = transform_matrix(first_message)
print("Cadru nemodificat: " + str(first_matrix))
first_matrix = transform_line(first_matrix)
print("Matricea modificata pe linii: " + str(first_matrix))
first_matrix = transform_column(first_matrix)
print("Cadru transmis: " + str(first_matrix))
print()

second_message = '111100101010011010111'
if not verify_input(second_message):
    sys.exit()

second_matrix = transform_matrix(second_message)
print("Cadru nemodificat: " + str(second_matrix))
second_matrix = transform_line(second_matrix)
print("Matricea modificata pe linii: " + str(second_matrix))
second_matrix = transform_column(second_matrix)
print("Cadru transmis: " + str(second_matrix))
print()

if first_matrix is not second_matrix and first_message is not second_message:
    print("S-au gasit erori!")
else:
    print("Nu s-au gasit erori!")


