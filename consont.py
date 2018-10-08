n = input("Enter the alphabet: ")

if n in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % n)
elif n== 'y':
	print("They are vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % n) 
