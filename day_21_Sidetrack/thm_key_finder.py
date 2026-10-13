
hex_data = "113f7531432d1e4b23442411592152231b592d4a"
cipher_text = bytes.fromhex(hex_data)
plain_text = "THM{thisisafakeflag}".encode()
key = b""

encode = []
for cipher, plain in zip(cipher_text,plain_text):
    encode.append(cipher ^ plain)
key = bytes(encode)
print(key)


'''

flag_2 = "3c1b2e123f003a100038093502022e0e3f020e36"
flag_1 = "667c0f03075a5d31110053522313165458231f0e"
key = "uSLFE"

flag_1 = bytes.fromhex(flag_1)
deciphered_text = ""
for i in range(len(flag_1)):
    deciphered_char = chr(flag_1[i] ^ ord(key[i % len(key)]))
    deciphered_text += deciphered_char
print(deciphered_text)

'''