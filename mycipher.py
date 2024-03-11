import sys

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Convert to uppercase
            char = char.upper()
            # Shift letters
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += shifted
    return encrypted_message

def print_blocks(message):
    for i in range(0, len(message), 5):
        print(message[i:i+5], end=" ")
        if (i+5) % 50 == 0:  # Print 10 blocks per line
            print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift>")
        sys.exit(1)
    
    shift = int(sys.argv[1])
    
    message = input("Enter your message: ")
    
    encrypted_message = caesar_cipher(message, shift)
    
    print("Encrypted message:")
    print_blocks(encrypted_message)

if __name__ == "__main__":
    main()
