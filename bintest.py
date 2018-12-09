import binascii

filename = 'binaryfilesample.dat'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))