import stdaudio
import stdio
import sys

# Accept filename (str) as command-line argument.
filename = sys.argv[1]

# Read all integers from standard input (the 32-measure waltz sequence).
measures = stdio.readAllInts()

# Validate: exactly 32 measures.
if len(measures) != 32:
    stdio.writeln('A waltz must contain exactly 32 measures')
    sys.exit()

# Validate: minuet measures (first 16) must be from [1, 176].
for i in range(16):
    if measures[i] < 1 or measures[i] > 176:
        stdio.writeln('A minuet measure must be from [1, 176]')
        sys.exit()

# Validate: trio measures (last 16) must be from [1, 96].
for i in range(16, 32):
    if measures[i] < 1 or measures[i] > 96:
        stdio.writeln('A trio measure must be from [1, 96]')
        sys.exit()

# Build the waltz audio by concatenating the .wav files.
waltz = []
for i in range(16):
    wav = stdaudio.read('data/M' + str(measures[i]))
    for sample in wav:
        waltz.append(sample)
for i in range(16, 32):
    wav = stdaudio.read('data/T' + str(measures[i]))
    for sample in wav:
        waltz.append(sample)

# Save the waltz to the specified file.
stdaudio.save(filename, waltz)
