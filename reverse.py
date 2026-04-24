import stdio

# Read all strings from standard input into a list.
a = stdio.readAllStrings()

# Write the strings in reverse order.
for i in range(len(a) - 1, -1, -1):
    stdio.write(a[i] + ' ')
stdio.writeln()
