# Python program to extract digits from string

# take string
string = "kn4ow5pro8am2"

# print original string
print("The original string:", string)

# using join() + filter() + isdigit()
num1 = ''.join(filter(lambda i: i.isdigit(), string))
num2 = ''.join(filter(lambda i: i.isdigit(), string))

# print extract digits
print("Extract Digits:", num1)
print("Extract Digits:", num2)