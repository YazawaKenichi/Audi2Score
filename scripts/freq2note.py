#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import math
from numpy import sign

VERSION = 1.0

def frequency_to_note(x):
    # 基準音の設定
    A4 = 440.0
    C4 = A4 * (2 ** (-9 / 12))
    # 基準音からの単純な距離
    distanceA = 12 * math.log2(x / A4)
    distanceC = 12 * math.log2(x / C4)
    # 基準音からの距離（何半音階分離れているか）
    da = round(distanceA)
    dc = round(distanceC)
    # ピアノの音階におけるノート名
    N = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    # 入力と基準との間に何半音あるか
    _in = ((da > 0) - (da < 0)) * abs(da) % 12 
    # 入力と基準との間に何オクターブあるか
    o = 4 + math.floor(dc / 12)
    return N[_in] + str(o)

if __name__ == "__main__":
    args = preload.Args("Wave Form Plotter", version = VERSION, description = "Plot wave from audio file with For FFT.")
    args.parser.add_argument("freq", metavar = "FREQUENCY")
    arg = args.get()
    f = float(arg.freq)

    print(f"{frequency_to_note(f)}")

