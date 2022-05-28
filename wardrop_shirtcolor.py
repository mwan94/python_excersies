 #Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
  #Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clot, col in wardrobe.items():
	for diff in col:
		
		print("{} {}".format(diff, clot))
