import stdarray
import stdrandom
import stdio

# Read the 11 x 16 minuet table from standard input.
minuet = stdarray.create2D(11, 16, 0)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# Read the 6 x 16 trio table from standard input.
trio = stdarray.create2D(6, 16, 0)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

# Generate 16 minuet measures by rolling two dice for each.
for j in range(16):
    dice1 = stdrandom.uniformInt(1, 7)
    dice2 = stdrandom.uniformInt(1, 7)
    total = dice1 + dice2
    # Row index is total - 2 (dice sum ranges from 2 to 12).
    stdio.write(str(minuet[total - 2][j]) + ' ')

# Generate 16 trio measures by rolling one die for each.
for j in range(16):
    die = stdrandom.uniformInt(1, 7)
    # Row index is die - 1 (die ranges from 1 to 6).
    stdio.write(str(trio[die - 1][j]) + ' ')

stdio.writeln()
