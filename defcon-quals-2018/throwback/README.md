# Throwback
## Problem
The original file is ["text"](./text), a 90-byte long string: 
`Anyo!e!howouldsacrificepo!icyforexecu!!onspeedthink!securityisacomm!ditytop!urintoasy!tem!`.

## Approach
Since this is all that we're given, it's pretty likely that this is a stenography challenge.
Let's start by trying to figure out what the original message would be. It's likely
`Anyone who would sacrifice policy for execution speed thinks security is a commodity
to pour into a system!`, replacing letters `nwltisoos`. Note that this replaces all of the 
exclamation points except the last.

Well, it turns out that the flag isn't `nwltisoos`, and there's no obvious caesar encryption
or permutation that works (though it permutes to "solwtions", which messed with me for a
while).

Let's try... the letters before/after the exclamation points.
Before: `oeou kmpym`, after: `ehi osdut `. Neither works.

Thinking of this as a stenography tactic... it's not usually a good steno tactic to require
your hidden message to rely on the plaintext it's encoded in. (You then need to find a
specific plaintext that works, which kind of weakens the point of using steno in the
first place.) So let's consider the positions of the exclamation points, rather than the
letters around them.

It's at this point that a hint was released: `The flag is in the format ([a-z ]+)`.
That means that we should probably be looking for numbers less than 26. That rules
out the absolute position of exclamation points (since the last one is at byte 89), so
let's look at the number of letters before each exclamation point.

That gives us `4 1 18 11 0 12 15 7 9 3`, which, converted from a 0-indexed alphabet,
gives `ebslamphjd`. When we decrypt that with caesar of 1, we get `darkzlogic` - and
`dark logic` is the flag! So why didn't we get that outright?

## Solution
Instead of using a 0-indexed alphabet (where 0 maps to a, 1 to b, etc), we should've
used a 1-indexed alphabet with zero mapping to a space (since spaces are explicitly
allowed in the hint).

Here's a script for the entire process (downloadable as [solution.py](./solution.py):
```Python
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
```