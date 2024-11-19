import numpy as np
from sympy import Matrix

# Helper function to convert a letter to its corresponding integer value
def letter_to_int(letter):
    return ord(letter) - ord('A')

# Helper function to convert an integer value back to a letter
def int_to_letter(value):
    return chr(value + ord('A'))

# Helper function to convert a string to a vector of integers
def string_to_vector(string):
    return [letter_to_int(char) for char in string]

# Helper function to convert a vector of integers back to a string
def vector_to_string(vector):
    return ''.join(int_to_letter(num % 26) for num in vector)

# Given cipher and known plaintext
cipher_text = "VBIDUXANLFPYPUSFGPIDTYUHDY"
known_plaintext = "THEF"

# Step 1: Create vectors from the known plaintext and corresponding cipher
plain_vector = np.array(string_to_vector(known_plaintext)).reshape(1, 4)
cipher_vector = np.array(string_to_vector("VBID")).reshape(1, 4)

# Step 2: Construct matrices and solve for the key
plain_matrix = Matrix(plain_vector)
cipher_matrix = Matrix(cipher_vector)

# Calculate the inverse of the plaintext matrix in mod 26
plain_matrix_inv = plain_matrix.inv_mod(26)

# Calculate the key matrix
key_matrix = (cipher_matrix * plain_matrix_inv) % 26

# Step 3: Decrypt the full cipher text using the key matrix
key = np.array(key_matrix).astype(int)
decrypted_text = []

for i in range(0, len(cipher_text), 4):
    block = string_to_vector(cipher_text[i:i+4])
    decrypted_block = np.dot(key, block) % 26
    decrypted_text.extend(decrypted_block)

# Convert the decrypted integers back to letters
plain_text = vector_to_string(decrypted_text)

# Output the results
print("Key Matrix:")
print(key_matrix)
print("\nDecrypted Plaintext:")
print(plain_text)

# Save the key and plaintext to files
with open("key.txt", "w") as key_file:
    key_file.write(str(key_matrix))

with open("plain.txt", "w") as plain_file:
    plain_file.write(plain_text)
