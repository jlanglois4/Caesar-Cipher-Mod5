CAPITAL_UPPER = 90
CAPITAL_LOWER = 65
LOWERCASE_UPPER = 122
LOWERCASE_LOWER = 97


def is_uppercase(character, shift):
    char = ord(character)
    if CAPITAL_LOWER <= char <= CAPITAL_UPPER:
        new_value = char + shift
        if new_value > CAPITAL_UPPER:
            difference = new_value - CAPITAL_UPPER
            new_value = CAPITAL_LOWER + difference - 1
        return chr(new_value)
    else:
        new_value = char + shift
        if new_value > LOWERCASE_UPPER:
            difference = new_value - LOWERCASE_UPPER
            new_value = LOWERCASE_LOWER + difference - 1
        return chr(new_value)


message = input("Enter message: ")

shift = ""
condition = False
while not condition:
    shift = int(input("Number of characters to shift (1 - 26): "))
    if 1 <= shift <= 26:
        condition = True
        message_char_list = list(message)
    else:
        print("Enter valid number")

new_char_list = []
for character in message_char_list:
    new_char = is_uppercase(character, shift)
    new_char_list.append(new_char)

print(''.join(new_char_list))
