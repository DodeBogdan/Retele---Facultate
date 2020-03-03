def xor(polynomials, message):
    for index in range(len(polynomials)):
        if polynomials[index] == message[index]:
            message = message[:index] + '0' + message[index + 1:]
        else:
            message = message[:index] + '1' + message[index + 1:]
    return message


def remove_zeros(message):
    index = 0
    while message[index] == '0' and index < len(message) - 1:
        index += 1
    message = message.replace('0', '', index)
    return message


def verify_polynomials(polynomials):
    if len(polynomials) == 0:
        return False
    if polynomials[0] == '0':
        return False
    if polynomials[-1] == '0':
        return False
    return True


print("Enter message: ")
message = input()

print("Enter polynomials: ")
polynomials = input()

if not verify_polynomials(polynomials):
    print("The polynomials is incorrect!")
else:

    print("The polynomials is correct.")

    grade = len(polynomials) - 1

    copy = message

    copy += '0' * grade
    result = copy

    while len(result) >= grade:
        # if len(result) != 0:
        result = xor(polynomials, result)
        result = remove_zeros(result)

    copy = copy[::-1]

    if len(result) != 0:
        copy = xor(result, copy)

    copy = copy[::-1]
    print("The result message is: " + copy)
    print("The result is: " + result)
