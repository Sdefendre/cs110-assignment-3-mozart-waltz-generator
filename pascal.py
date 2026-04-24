import stdarray
import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Create a 2D array for Pascal's triangle with n + 1 rows.
p = stdarray.create2D(n + 1, n + 1, 0)

# Fill in the values using the recurrence relation.
for i in range(n + 1):
    p[i][0] = 1
    p[i][i] = 1
    for j in range(1, i):
        p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

# Write Pascal's triangle as standard output.
for i in range(n + 1):
    for j in range(i + 1):
        if j > 0:
            stdio.write(' ')
        stdio.write(p[i][j])
    stdio.writeln()
