alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Enter alphabets only!")
encode = input("Enter text to be encrypted: ").replace(" ", "").casefold()
assert encode.isalpha(), "/* only alphabets allowed */"
shift = int(input("How many characters would you like to shift: "))
encrypted_r = ""

for i in encode:
    index_r = (alphabets.index(i) + shift) % 26
    encrypted_r += alphabets[index_r]

print(f"{encode} when shifted {shift} characters to the right: {encrypted_r}")
