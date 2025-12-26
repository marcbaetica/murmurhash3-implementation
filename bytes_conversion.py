items = [i for i in range(255)]

'''
print(bytes([0]))
print(bytes([0, 1]))
print(bytes([255]))
# print(bytes([256]))   # ValueError: bytes must be in range(0, 256)
'''

b = bytes([65, 66, 67])
print(b)


item = bytes([1])
print(item)
print(type(item))
# print(item[1])

print('A'.encode('utf-8'))

item = 'A'
print(item)
print(item.encode('utf-8'))

print(type(ord(item)))
print(ord(item))
print(ord(b'A'))
print(type(ord(item)))
print(type(ord(b'A')))

num = 65
print(num)
print(str(num), type(str(num)))
print(str(num).encode(), type(str(num).encode()))

b_num = str(num).encode()
print(chr(num), type(chr(num)))
# print(chr(str(num)), type(chr(str(num))))
# print(chr(b_num), type(chr(b_num)))
print()

def p(item):
    print(item, type(item))

p(num)
p(str(num).encode())
p(chr(num))
p(hex(num))
p(bin(num))

print()

num = 'a'
p(num)
p(ord(num))
p(hex(ord(num)))
p(bin(ord(num)))
p(bin(ord(num))[2:])

# Bytes are esentially sequences of numbers.
# ord('one_char_str') gives the int value of the char (unicode code point of the char... ascii value for standard ascii chars 1-127). This is also known as an ordinal value as chars are ordered sequences (e.g., 'A' is 1st, 'B' is 2nd). This means that ord(C)-ord(A)=2 ordinal points away. 
# It's a key concept in statistics, representing ordered categories (ordinal data) distinct from nominal (no order) and interval/ratio (equal spacing) data. 
# Ordered and differences are equal/meaningful (e.g., temperatures in Celsius/Fahrenheit, height). 
# chr(int) is the opposite of ord. Takes in an int and returns the single character string representation of the Uicode code point. Input must be int; not str or bytes.
# hex, bin, int: convert between the different representations. Must start at int via ord.
# The results of bin() and hex() are strings with 0b and 0x prefixes, respectively.

