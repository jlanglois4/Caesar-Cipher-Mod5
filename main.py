CAPITAL_UPPER = 90
CAPITAL_LOWER = 65
LOWERCASE_UPPER = 122
LOWERCASE_LOWER = 97


def get_shift():
    shift = 0
    condition = False
    while not condition:
        shift = int(input("Number of characters to shift (1 - 26): "))
        if 1 <= shift <= 26:
            condition = True
        else:
            print("Enter valid number")
    return shift


message = input("Enter message: ")
shift = get_shift()

encrypted_message = ""

for letter in message:
    if letter == ' ':
        encrypted_message += letter
    else:
        if letter.isupper():
            char = ord(letter)
            char_index = ord(letter) - CAPITAL_LOWER
            new_index = (char_index + shift) % 26
            new_char = new_index + CAPITAL_LOWER
            new_letter = chr(new_char)
            encrypted_message += new_letter
        else:
            char = ord(letter)
            char_index = ord(letter) - LOWERCASE_LOWER
            new_index = (char_index + shift) % 26
            new_char = new_index + LOWERCASE_LOWER
            new_letter = chr(new_char)
            encrypted_message += new_letter
print("Encrypted:", encrypted_message)
decrypted_message = ""

for letter in encrypted_message:
    if letter == ' ':
        decrypted_message += letter
    else:
        if letter.isupper():
            char = ord(letter)
            char_index = ord(letter) - CAPITAL_LOWER
            new_index = (char_index - shift) % 26
            new_char = new_index + CAPITAL_LOWER
            new_letter = chr(new_char)
            decrypted_message += new_letter
        else:
            char = ord(letter)
            char_index = ord(letter) - LOWERCASE_LOWER
            new_index = (char_index - shift) % 26
            new_char = new_index + LOWERCASE_LOWER
            new_letter = chr(new_char)
            decrypted_message += new_letter
print(f"Decrypted: {decrypted_message}")
