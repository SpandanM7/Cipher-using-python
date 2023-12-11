class SubstitutionCipher:
    def __init__(self, key):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.!? "
        self.key = key

    def decode(self, encoded_message):
        decoded_message = ''.join([self.alphabet[self.key.find(char)] for char in encoded_message])
        return decoded_message

# Example usage for decoding:
klpd=input("Enter the encoded message: ")
bsdk=input("Enter the key: ")
decoded_cipher = SubstitutionCipher(bsdk)

decoded_message = decoded_cipher.decode(klpd)
print(f"Decoded Message: {decoded_message}")
