a = 200
res = hex(a)
print(res)

string = b"hello"
print(string.hex())

print(ord("A"))
print(chr(65))
print(float.hex(3.9))


print(hex(ord("A")))


#converting string into hex
output = ""
input = "kishore"
for i in range(len(input)):
    output += hex(ord(input[i])).lstrip("0x")
print(output, type(output))

#converting hex into string
output = ""
hex_data = "6b6973686f7265"
for hex in range(0, len(hex_data), 2):
    output += chr(int(hex_data[hex:hex+2], 16))
print(output)

#another easy way to convert hex into string is 
hex_data = "6b6973686f7265"
output = bytes.fromhex(hex_data).decode()
print(output)


#encoding & decoding
text = "Helloé"
print(text.encode("ascii",errors='replace') )
print(text.encode())
print(bytes(text, 'utf-8'))

text = "Helloé"
text = text.encode()
print(text.decode())


#base64 encoding
import base64
string = "secure@123"
enc_string = base64.b64encode(string.encode()).decode()
print(enc_string)

dec_string = base64.b64decode(enc_string.encode()).decode()
print(dec_string)