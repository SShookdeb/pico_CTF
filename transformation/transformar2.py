
#!bin/bash/python3
hex_string = '7069636f4354467b31365f626974735f696e73743334645f6f665f385f64353263366239337d'
bytes_object = bytes.fromhex(hex_string) #Convert to bytes object.
ascii_string = bytes_object.decode("ASCII") #Convert to ASCII representation.
print(ascii_string)