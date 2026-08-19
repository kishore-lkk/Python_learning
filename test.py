limit = int(input("enter the limit: "))

output = 1
previous_1 = 0
previous_2 = 0

if limit >= 0:
    print(0)

while output < limit:
    previous_2 = output
    print(output)
    output = previous_1 + previous_2
    previous_1 = previous_2
