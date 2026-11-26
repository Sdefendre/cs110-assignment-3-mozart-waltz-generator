# Mozart Waltz Generator

Python programs that compose a random waltz with Mozart's *Musikalisches Würfelspiel* (musical dice game) and render it to an audio file.

## What it does

- **`waltz_sequence.py`** reads Mozart's 11×16 minuet table and 6×16 trio table. For each of the 16 minuet measures it rolls two dice, and for each of the 16 trio measures it rolls one die. It prints the 32 measure numbers that make up the waltz.
- **`waltz_file.py`** reads a 32-measure sequence and validates it: exactly 32 measures, minuet measures in 1–176, trio measures in 1–96. It then joins the matching measure recordings into one `.wav` file.

```sh
python3 waltz_sequence.py < mozart.txt | python3 waltz_file.py
```

The measure `.wav` files and the `mozart.txt` table came with the course materials and aren't included here.

## Concepts

2D arrays, simulating randomness, input validation, and audio sample processing.

Also included are warm-up exercises: `birthday`, `distance`, `pascal`, `reverse` and `transpose`.

## Running it

These programs use the standard libraries from *Introduction to Programming in Python* (Sedgewick, Wayne & Dondero): `stdio`, `stdarray`, `stdrandom` and friends. Put those modules on your `PYTHONPATH`, then run the scripts with Python 3.

## Course

CS110 Introduction to Computing, UMass Boston, Spring 2026 (instructor: Swami Iyer). The instructor supplied the starter code and course libraries. My approach and notes for each problem are in [`notes.txt`](notes.txt).
