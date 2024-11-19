# %% [markdown]
# | Field      | Information                         |
# |------------|-------------------------------------|
# | **Author** | Abdelaziz Nematallah                |
# | **Date**   | 2/11/2024                           |
# | **Desc**   | This notebook is to solve the first part of lab1 |
# 
# #### Problem description: 
# *  Cryptanalysis based on knowledge of the ciphertext only, i.e. without knowing any part of
#  the plaintext, is the most difficult type of analysis. A method that can always be used is ex
# haustive key search, where every key is tried out. For this lab you were provided a file called
#  Subst-Rijndael.crypt, which contains the binary data of a text that has been encrypted
#  twice, using monoalphabetic substitution first and then the AES algorithm in CBC mode. The AES
#  encryption used a weak key, where from the 128bit key only the first 16bits were chosen and the
#  rest of the key was padded with zeros. Here, the initialization vector (IV) is the first block of the
#  ciphertext

# %% [markdown]
# ### Solution steps
# 1. Since the encryption was done by two encryption algorithms:
#    1. monoalphabetic 
#    2. AES
# 2. Then to decrypt it correctly we need to apply the decryption in the reverse order
#    1. AES decryption
#    2. monoalphabetic decryption
# 

# %% [markdown]
# ## Task 1.1: Brute-force Weak AES
# *  Thanks to the small key space, a brute-force attack on Subst-Rijndael.crypt becomes
#  a reasonable technique to break the outer AES encryption layer. Write a short prototype script
#  to automate the attack. To this end, you must find a criterion that allows you to automatically
#  distinguish the right key from wrong ones. The decryption shall be computed and stored in
#  Subst.txt (in plaintext format) for further processing in the next step. Furthermore, you should
#  save the discovered AES key in aes.key as a hexadecimal text string.
#  Hints:
#  1. Notice that there are already many implementations (libraries) available to apply AES
#  encryption and decryption, e.g., PyCryptodome to interface with Python.
#  2. Take a look at Shannon entropy. How can it help to find out the correct key among all
#  possible combinations?

# %% [markdown]
# ### Solution steps: 
# 1. since the used key is weak, which consists of only 16 bits, so we need to apply brutefroce attack and try the all 2^16 possible keys
# 2. then we need to evaluate the Shannon entropy which indicates that natural language text should have lower entropy compared with the other random text. 
# 3. so we calculate the shanon entropy after decryption of each key, and select the key with the minimum value of shanon entropy. 
# 4.  finally, we can get the correct key and decrypt the ciphertext, and store the corresponding plaintext, and the key. 
# 

# %%
# importing libraries
from Crypto.Cipher import AES
import struct
import math

# %%
def calculateShanonEntropy (data): 
    '''
        This method is responsible for evaluating shanon entropy for data sequence
        Logic: 
            if no data return 0 
            iterate over the unique items in the data, and evaluate its entropy using shanon equation :
                p(x) = # times x appeared / total length
                entropy -= p(x) * log2(p(x)) // high entropy means more randomness. 
            return entropy
    '''
    if not data:
        return 0
    entropy = 0 
    for item in set(data): 
        p = data.count(item) / len(data)
        entropy -= p * math.log(p, 2)
    return entropy

# %%
def AESBruteForceAttack(fileName):
    '''
        This method is to apply the brute force attack. 
        Logic: 
            1. open the file. 
            2. initialize the Initial vector with the first 16 bytes 
            3. create dummy variables to store the results in.
            4. iterate over the 2^16 possible keys. 
                4.1. construct the 128bits key by adding the possible key then pad it with 14 zeros bytes. 
                4.2. try to decrypt the cipher text using this key.
                4.3. evaluate the entropy of the decrypted file. 
                4.4. if the entropy is less than the best entropy
                    4.4.1. assign the new entropy as the best entropy
                    4.4.2. assign the best plain text to the current plain text
                    4.4.3. assign the best key to the current key. 
            5. store the best key and best plain text in a file.
    '''
    # Read encrypted file
    with open(fileName, 'rb') as f:
        cipherText = f.read()
    
    iv = cipherText[:16]  # Assuming IV is the first 16 bytes
    encryptedData = cipherText[16:]  # Rest is the encrypted content
    
    # Variables to store best key and plaintext based on entropy
    bestEntropy = float('inf')
    bestPlaintext = None
    bestKey = None

    # Try all 16-bit keys (0x0000 to 0xFFFF)
    for keyCandidate in range(0x10000):
        # Convert to a 128-bit key with padding: 0x0000 + 0's
        # struct.pack is used to convert the data into specific binary format. 
        # ">H" is the format string:
            # > specifies big-endian byte order (meaning the most significant byte comes first).
            # H indicates an unsigned short integer (16 bits).
        # our keyCandidate is 2 bytes (16 bits). 
        key = struct.pack(">H", keyCandidate) + b'\x00' * 14
        
        # AES decryption with CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            decrypted_data = cipher.decrypt(encryptedData)
            
            # Check entropy
            entropy = calculateShanonEntropy(decrypted_data)
            if entropy < bestEntropy:
                bestEntropy = entropy
                bestPlaintext = decrypted_data
                bestKey = key
        except ValueError:
            # AES decryption failed (in case padding is incorrect)
            continue

    # Write best decryption output
    if bestPlaintext and bestKey:
        with open("Subst.txt", "wb") as f:
            f.write(bestPlaintext)
        
        with open("aes.key", "w") as f:
            f.write(bestKey.hex())

        print("Decryption successful!")
        print("AES key found:", bestKey.hex())

    else:
        print("No valid key found.")



# %%
# now lets try to apply this on our encryption file 
print('attack started')
AESBruteForceAttack("Subst-Rijndael.crypt")

# it took around 30 seconds which means that we compute 2184.53 keys per second, and this number varies depending on processing power.
