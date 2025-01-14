

# Introduction to Cyber Security - Secret Key Cryptography Lab
This document outlines the first three tasks from the lab exercise on secret key cryptography. And you will find the solution of each task clearly explained in English in each folder you can check solution of 
* task1 in folder ./task01/bruteforce_aes_and_break_monoalphabetic_cipher.ipynb
* task2 in folder ./task02/writeup.ipynb
* task3 in folder ./task03/Writeup.ipynb

---

## Task 1: Ciphertext-only Analysis
### Description
Perform a ciphertext-only cryptanalysis on the file `Subst-Rijndael.crypt`, which has been encrypted using monoalphabetic substitution followed by AES encryption in CBC mode. The AES key has only 16 significant bits, padded with zeros.

### Subtasks
1. **Brute-force Weak AES**:
   - Implement a brute-force attack to break the AES encryption using the weak key.
   - Write a script to automate the attack and save the decrypted output as `Subst.txt`.
   - Save the discovered AES key in a file named `aes.key` as a hexadecimal string.
   - **Hints**: 
     - Use libraries like PyCryptodome for AES decryption.
     - Consider using Shannon entropy to identify the correct key.

2. **Hill-Climbing Method for Monoalphabetic Substitution**:
   - Break the inner monoalphabetic substitution using a hill-climbing algorithm.
   - Implement a method to initialize the key through frequency analysis.
   - Develop an iterative process to optimize the key and improve decryption accuracy.
   - Save the final plaintext in `Plain.txt` and the substitution key in `subst.key`.

---

## Task 2: Find the Right Algorithm
### Description
Given the ciphertext `cipher.crypt` and two plaintext files (`plaintext1.txt` and `plaintext2.txt`), find an encryption scheme and two keys such that:
- Decrypting with key `k1` yields `plaintext1.txt`.
- Decrypting with key `k2` yields `plaintext2.txt`.

### Requirements
- Identify an appropriate encryption scheme and generate keys `k1` and `k2`.
- Submit the keys as `k1.key` and `k2.key` containing the binary data.
- Write a brief explanation in `Writeup.md` on how you determined the keys and algorithm.
- If a script is developed, include it as `cipher_keys.{py | cc | ...}`.

---

## Task 3: Partial Known Plain-Text Analysis
### Description
Decrypt `XOR.zip.crypt`, which was encrypted with a 96-bit XOR key. Use a known-plaintext attack to recover the key and decrypt the file.

### Requirements
- Submit the XOR key as `XOR.key` (hexadecimal string).
- Provide a brief explanation in `Writeup.md` detailing your decryption process.
- Include any supporting scripts as `XOR_decrypter.{py | cpp | *}`.
