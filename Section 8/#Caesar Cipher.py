from timeit import repeat


print('''

░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

''')
repeat_program = True
while repeat_program == True:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction = input("Type 'encode' to decrypt , type 'decode' to decrypt.\n").lower()
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number :\n"))
    shift %= 26
    
    def caecar(plain_text, shift_amount,cipher_direction):
        encoded_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in plain_text:
            if letter not in alphabet:
                encoded_text += letter
            else:
                index_now = alphabet.index(letter)
                encoded_text += alphabet[index_now+shift_amount]
        print(f"The encoded text is {encoded_text}")

    caecar(text,shift,direction)
    repeat_or_not = input("Do you want to repeat ? (Y/N) :").upper()
    if repeat_or_not == "N":
        repeat_or_not = False

'''
def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for encode in plain_text:
        index_now = alphabet.index(encode)
        encoded_text += alphabet[index_now+shift_amount]
    print(f"The encoded text is {encoded_text}")

def decrypt(plain_text, shift_amount):
    decoded_text = ""
    for decode in plain_text:
        index_now = alphabet.index(decode)
        decoded_text += alphabet[index_now-shift_amount]
    print(f"The decoded text is {decoded_text}")
'''


    