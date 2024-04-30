#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import math

def note_to_frequency(note):
    A4 = 440.0
    N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    n = note[:-1]
    o = int(note[-1])
    i = N.index(n)
    d = -9 + (o - 4) * 12 + i
    q = d / 12
    return A4 * (2 ** q)

if __name__ == "__main__":
    for o in range(0, 9):
        for n in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']:
            no = n + str(o)
            f = note_to_frequency(no)
            print(f"{no: >3} : {f: >10.4}")

