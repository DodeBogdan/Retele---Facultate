import sys

def xor(polynomials, message):
    if len(polynomials) > len(message):
        return
    for index in range(len(polynomials)):
        if polynomials[index] == message[index]:
            message = message[:index] + '0' + message[index + 1:]
        else:
            message = message[:index] + '1' + message[index + 1:]
    return message


def remove_zeros(message):
    if message is None:
        return
    index = 0
    while index < len(message) and message[index] == '0':
        index += 1
    message = message[:0] + message[index:]
    return message


def verify_polynomials(polynomials):
    if len(polynomials) == 0:
        return False
    if polynomials[0] == '0':
        return False
    if polynomials[-1] == '0':
        return False
    return True


def verify_input(input):
    for index in range(len(input)):
        if input[index] != '0' and input[index] != '1':
            return False
    return True

def program(copy, polynomial):

    result = copy

    while result is not None and len(result) > grade:
        result = xor(polynomials, result)
        result = remove_zeros(result)

    copy = copy[::-1]

    if result is not None and len(result) != 0:
        copy = xor(result, copy)

    copy = copy[::-1]
    return copy, result

#print("Enter message: ")
message = "11"  # input()
print("Message is: ", message)

if not verify_input(message):
    print("Input was incorrect!")
    sys.exit()

#print("Enter polynomials: ")
polynomials = '1011'  # input()
print("Polynom is: " + polynomials)

if not verify_input(polynomials):
    print("Input was incorrect!")
    sys.exit()

if not verify_polynomials(polynomials):
    print("The polynomials is incorrect!")
    sys.exit()

print("The polynomials is correct.")

grade = len(polynomials) - 1
print("Grade is: " + str(grade))

copy = message
copy += '0' * grade
print("Message after concat with 0 * grade: " + copy)

copy, result = program(copy,polynomials)

print("Do you want to modify the result? y/n")
answer = input()

print("Message before result: " + copy)

if answer == 'y':
    copy = copy.replace('0','1',1)
    print("Message after modify: " + copy)

copy, result = program(copy,polynomials)

print("The result message is: " + str(copy))
print("The result is: " + str(result))

if result is not '':
    print("Message is display with error!")
else:
    print("Message is display correctly!")
