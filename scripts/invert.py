#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import math

def note_to_frequency(note):
    A4_frequency = 440.0
    note_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    # ノート名とオクターブに分割
    note_name = note[:-1]
    octave = int(note[-1])
    # A4からの半音数を計算
    distance_from_A4 = (octave - 4) * 12 + note_names.index(note_name)
    # A4の周波数に2^(1/12)を距離から掛けて求める
    frequency = A4_frequency * math.pow(2, distance_from_A4 / 12)
    return frequency

# テスト
note = "A4"
print("Note:", note)
print("Frequency:", note_to_frequency(note), "Hz")

# 任意の音階を入力として与えてテスト
custom_note = "C5"
print("\nNote:", custom_note)
print("Frequency:", note_to_frequency(custom_note), "Hz")


