import stdarray
import stdio
import stdrandom
import sys

# Accept trials (int) as command-line argument.
trials = int(sys.argv[1])

# Run trials experiments and count the total number of people needed.
total = 0
for t in range(trials):
    # Track which birthdays have been seen.
    hasBirthday = stdarray.create1D(365, False)
    count = 0
    while True:
        # Pick a random birthday.
        birthday = stdrandom.uniformInt(0, 365)
        count += 1
        if hasBirthday[birthday]:
            break
        hasBirthday[birthday] = True
    total += count

# Write the average number of people needed.
stdio.writeln(total // trials)
