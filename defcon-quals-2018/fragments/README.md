# Fragments (aka ELF Crumble) (102)
## Problem
We're given an executable and eight "fragments", which you can
find in [given_files](./given_files). The executable is broken, and we
need to piece it back together.

## Approach
Opening the executable in a text editor shows that 807 bytes have been overwritten
with "X". The sum of the sizes of all the executables is also 807, so it seems likely that
we just have to order the fragments correctly and place them back in the executable.

There is a nice, high-level way to do this by examining the sizes of the functions
and the objdumps of the files... but I want my brain free to focus on other challenges, so 
brute force it is.

## Solution
Solved with a simple python script, [glue.py](./glue.py). Note that this needs to be run on a
32-bit machine; my Kali VM worked.

```Python
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
```