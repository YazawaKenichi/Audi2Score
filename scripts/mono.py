#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import numpy as np
import matplotlib.pyplot as plt
import wave

def convert_to_mono(input_file, output_file):
    try:
        with wave.open(input_file, 'rb') as wave_file:
            num_channels = wave_file.getnchannels()
            if num_channels != 2:
                print("Error: Input file is not stereo.")
                return

            frame_rate = wave_file.getframerate()
            num_frames = wave_file.getnframes()

            mono_channel = wave.open(output_file, 'wb')
            mono_channel.setnchannels(1)
            mono_channel.setsampwidth(wave_file.getsampwidth())
            mono_channel.setframerate(frame_rate)

            for i in range(num_frames):
                frames = wave_file.readframes(1)
                mono_channel.writeframes(frames[:2])  # take the left channel only

            mono_channel.close()
            print("Conversion to mono completed successfully.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    VERSION = 1.0

    args = preload.Args("Wave Form Plotter", version = VERSION, description = "Plot wave from audio file with For FFT.")
    args.parser.add_argument("input", metavar = "PATH")
    arg = args.get()

    input_file = arg.input
    basename = "".join(input_file[:input_file.rfind(".")])
    output_file = basename + "-mono.wav"

    convert_to_mono(input_file, output_file)

