alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesor(start_text, shift_amount, shift_direction):
    end_text = ""
    if shift_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        pos = alphabet.index(letter) + shift_amount
        end_text += alphabet[pos]
    print(f"Here is the {shift_direction}d result: {end_text}")

from art import logo
print(logo)


should_not_end = True

#start the cipher
while should_not_end:
    shift_direction = input("Type 'encode' for encrypt, type 'decode' to decrypt:\n")
    start_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number: "))

    shift_amount = shift_amount % 26
    caesor(start_text, shift_amount, shift_direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == 'no':
        should_not_end = False
        print("Goodbye")


'''encoded_message = []
decoded_message = []

def encode_message(message, shift_number):
    for letter in message:
        pos = alphabet.index(letter) + shift_number
        encoded_message.append(alphabet[pos])
    return ''.join(encoded_message)

def decode_mesaage(message, shift_number):
    for letter in message:
        pos = alphabet.index(letter) - shift_number
        decoded_message.append(alphabet[pos])
    return "".join(decoded_message)

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if action == 'encode':
    message = input("Enter the text:\n")
    shift_number = int(input("Enter the shift number: "))
    encrypted_message = encode_message(message, shift_number)
    print(f"Here's the encoded result: {encrypted_message}.")
elif action == 'decode':
    message = input("Enter the text:\n")
    shift_number = int(input("Enter the shift number: "))
    decrypted_message = decode_mesaage(message, shift_number)
    print(f"Here's the encoded result: {decrypted_message}.")
else:
    print("Invalid action.")'''