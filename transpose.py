import stdarray
import stdio
import sys

# Accept m (int) and n (int) as command-line arguments.
m = int(sys.argv[1])
n = int(sys.argv[2])

# Read m x n floats from standard input into a 2D list.
a = stdarray.create2D(m, n, 0.0)
for i in range(m):
    for j in range(n):
        a[i][j] = stdio.readFloat()

# Compute the transpose (n x m).
b = stdarray.create2D(n, m, 0.0)
for i in range(n):
    for j in range(m):
        b[i][j] = a[j][i]

# Write the transpose as standard output.
for i in range(n):
    for j in range(m):
        if j > 0:
            stdio.write(' ')
        stdio.write(b[i][j])
    stdio.writeln()
