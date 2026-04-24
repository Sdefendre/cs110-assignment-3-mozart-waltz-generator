import math
import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Read two n-dimensional lists x and y of floats from standard input.
x = stdio.readAllFloats()
y = x[n:]
x = x[:n]

# Calculate the sum of the squares of the differences.
total = 0.0
for i in range(n):
    total += (x[i] - y[i]) ** 2

# Write the Euclidean distance as standard output.
stdio.writeln(math.sqrt(total))
