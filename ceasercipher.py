def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result

print("Enter The Plain Text : ",end="")
text = input()
print("Enter The Shift Size : ",end="")
s = int(input())
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
