'''
a = 10
b = 2
c = a ^ b
print(c)
'''

'''
plain_text = "hello"
key = "k"

cipher_text = ""

cipher_text = bytes(ord(character) ^ ord(key) for character in (plain_text))
print(cipher_text)


decipher_text = "".join(chr(byte ^ ord(key)) for byte in cipher_text)
print(decipher_text)

'''
plain_text = "Hello"
key = "key"

cipher_text = b""

for key_index, input_index in enumerate(plain_text):
    cipher = ord(input_index) ^ ord(key[key_index % len(key)])
    cipher_text += bytes([cipher])
print(cipher_text)

deciphered_text = ""
for key_index, cipher_index in enumerate(cipher_text):
    deciphered = chr(cipher_index ^ ord(key[key_index % len(key)]))
    deciphered_text += deciphered
#print(deciphered_text)


#getting the key 

key = b""
deciphered_text = deciphered_text.encode()
print(deciphered_text)

encode = []
for cipher_string, deciphered_string in zip(cipher_text,deciphered_text):
    encode.append(cipher_string ^ deciphered_string)
key = bytes(encode)
print(key)