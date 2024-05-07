"""
Day 8: Final capstone project - building a Caesar Cipher to encrypt and decrypt text
"""


def encode(m: str, s: int) -> str:
    # TODO
    return ""


def decode(cipher: str, s: int) -> str:
    # TODO
    return ""


caesar = True

while caesar:
    print("Please enter 'encode' to encrypt and 'decode' to decrypt: ")
    operation = input().lower()

    while operation != "encode" and operation != "decode":
        operation = input("Please either enter 'encode' or 'decode': ")

    shift = int(input("Please enter your shift value: "))
    message = input("Please enter your message: ")

    if operation == "encode":
        cipher_text = encode(message, shift)
        print(f"Your ciphertext is as follows: {cipher_text}")
    else:
        true_message = decode(message, shift)
        print(f"Your message is as follows: {true_message}")

    redo = input("Do you want to go again? 'yes' or 'no': ").lower()
    while redo != "yes" and redo != "no":
        redo = input("Please enter either 'yes' or 'no' to go again or not: ")
    if redo == "yes":
        caesar = True
    else:
        caesar = False
