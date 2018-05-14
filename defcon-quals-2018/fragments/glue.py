import itertools
from subprocess import call

# Read the executable
broken_file = open("broken", "rb")
broken_text = broken_file.read()
broken_file.close()
broken_list = broken_text.split("X"*807)

if len(broken_list) != 2: # Error checking
    print "ERROR: splat incorrectly"

# These are the parts before and after the X's
firsthalf = broken_list[0]
secondhalf = broken_list[1]

# Read all the fragments
fragments = []
for i in xrange(1, 9):
    frag = open("fragment_"+str(i)+".dat", "rb")
    fragments.append(frag.read())
    frag.close()

filename = "newGuess"
# Iterate through each possible permutation
for order in itertools.permutations(fragments):
    lump = "".join(order)

    # We write our guess to newGuess, then try to execute it.
    f = open(filename, "wb")
    f.write(firsthalf+lump+secondhalf)
    f.close()
    try:
        #call("chmod u+x newGuess")
        call("./"+filename)
    except Exception as e:
        pass

# Prints "welcOOOme" at somewhere just past the 39000th iteration
