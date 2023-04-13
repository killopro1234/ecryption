print(chr(71), chr(101),
chr(101), chr(107),
chr(115), chr(32),
chr(102), chr(111),
chr(114),chr(32),
chr(71), chr(101),
chr(101), chr(107),
chr(115))

numbers = [17, 38, 79]
 
for number in numbers:
     
    # Convert ASCII-based number to character.
    letter = chr(number)
    print("Character of ASCII value", number, "is ", letter)
    
print(chr(400))