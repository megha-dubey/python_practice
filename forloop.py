for i in range(0, 7):

	if (i <= 3):

		for j in range(0, i+1):

			print("* ", end="")

		print("\r")
  
	else: 
		for x in range(i-1,6):
			print("* ", end="")
		print("\r")
