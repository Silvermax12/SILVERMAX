#Program for encrypting and decrypting using ceasar cipher algorithm
import random

def max(message, offset):
    result = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + offset) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def Max_decipher(encrypted_message, offset):
    return max(encrypted_message, -offset)

#this where the user is asked whether they want to encrypt or decrypt
choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()

while choice not in ["encrypt", "decrypt"]:
    print("Please enter 'encrypt' or 'decrypt'.")
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()

if choice == "encrypt":
    #so the inputing of the message and shift number from the user for encryption
    plaintext = input("Enter the word u wanna encrypt: ")
    shift = int(input("Enter the shift number: "))

    #Encryption
    encrypted_text = max(plaintext, shift)
    print(f"Encrypted: {encrypted_text}")
    
    #Ask if they wanna decrypt
    decrypt_choice = input("Do you also want to decrypt? (yes/no): ").lower()
    
    if decrypt_choice == "yes":
        decrypted_text = Max_decipher(encrypted_text, shift)
        print(f"Decrypted: {decrypted_text}")

elif choice == "decrypt":
    #Inputing of the message and shift number from the user for decryption
    encrypted_text = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))

    #Decryption
    decrypted_text = Max_decipher(encrypted_text, shift)
    print(f"Decrypted: {decrypted_text}")

else:
    print("Please enter 'encrypt' or 'decrypt'.")
print("All Hail Silvermax")