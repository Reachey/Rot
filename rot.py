#ROT
str = input()
for i in range(26):
	dec = ""
	for c in str:
		if c.isalpha():
			if ord(c) + i > 122 or c.isupper() and ord(c) + i > 90:
				dec += chr(ord(c) + i - 26)
			else:
				dec += chr(ord(c) + i)
		else:		#if not alpha then just copy char without change
			dec += c
	print("ROT%d:" %i, dec)