words=[2,3,4,5]
Odd=None
Even=None
def Separate(words):
	for word in words:
		if (word%2 == 0):
			Even=word
		else:
			Odd=word
	return Even
	return Odd	

Result=Separate(words)
print(Result)
