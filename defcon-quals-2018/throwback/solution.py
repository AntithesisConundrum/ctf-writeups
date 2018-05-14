# The given ciphertext
text = "Anyo!e!howouldsacrificepo!icyforexecu!!onspeedthink!securityisacomm!ditytop!urintoasy!tem!"
# Our space-prepended alphabet
alpha = " abcdefghijklmnopqrstuvwxyz" # Note the space at index 0

# Split the text and convert to lengths
splat = text.split("!") # this ends with an empty string due to the trailing !
lens = [len(x) for x in splat[:-1]]

# Convert to the alphabet and print!
letters = [alpha[i] for i in lens]
print "".join(letters)
