alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Enter alphabets only!")
decode = input("Enter text to be decrypted: ").replace(" ", "").casefold()
assert decode.isalpha(), "/* only alphabets allowed */"
shift = int(input("How many characters was the text shifted: "))
decrypted_l = ""

for i in decode:
    index_l = (alphabets.index(i) - shift) % 26
    decrypted_l += alphabets[index_l]

print(f"{decode} when shifted {shift} characters to the left: {decrypted_l}")
