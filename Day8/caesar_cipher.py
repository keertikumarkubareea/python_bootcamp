"""
Day 8: Final capstone project - building a Caesar Cipher to encrypt and decrypt text

Additional practice: modify the encrypt and the decrypt functions into a single function that takes a 3rd argument
'direction' that determines whether it is an encrypt or a decrypt

"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(m: str, s: int) -> str:
    m = list(m.lower())
    for char_index in range(len(m)):
        if m[char_index] in alphabet:
            index = alphabet.index(m[char_index])
            shifted_index = (index + s) % len(alphabet)
            m[char_index] = alphabet[shifted_index]
    return "".join(m)


def decode(cipher: str, s: int) -> str:
    cipher = list(cipher.lower())
    for char_index in range(len(cipher)):
        if cipher[char_index] in alphabet:
            index = alphabet.index(cipher[char_index])
            shifted_index = (index - s) % len(alphabet)
            cipher[char_index] = alphabet[shifted_index]
    return "".join(cipher)


caesar = True
while caesar:
    print("Please enter 'encode' to encrypt and 'decode' to decrypt: ")
    operation = input().lower()

    while operation != "encode" and operation != "decode":
        operation = input("Please either enter 'encode' or 'decode': ")

    shift = int(input("Please enter your shift value: "))
    message = input("Please enter your message: ")

    if operation == "encode":
        cipher_text = encode(m=message, s=shift)
        print(f"Your ciphertext is as follows: {cipher_text}")
    else:
        true_message = decode(cipher=message, s=shift)
        print(f"Your message is as follows: {true_message}")

    redo = input("Do you want to go again? 'yes' or 'no': ").lower()
    while redo != "yes" and redo != "no":
        redo = input("Please enter either 'yes' or 'no' to go again or not: ")
    if redo == "yes":
        caesar = True
    else:
        caesar = False
