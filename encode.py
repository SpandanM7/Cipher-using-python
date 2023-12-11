import random

class SubstitutionCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.!? "
        self.shuffle_alphabet()

    def shuffle_alphabet(self):
        random.seed(42)  # For reproducibility
        self.key = list(self.alphabet)
        random.shuffle(self.key)
        self.key = ''.join(self.key)

    def encode(self, message):
        encoded_message = ''.join([self.key[self.alphabet.find(char)] for char in message])
        return encoded_message


cipher = SubstitutionCipher()

message_to_encode =input("Enter your message: ")
encoded_message = cipher.encode(message_to_encode)
print(f"Original Message: {message_to_encode}")
print(f"Encoded Message: {encoded_message}")
print(f"Key: {cipher.key}")  
