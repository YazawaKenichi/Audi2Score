#!/usr/bin/env python3
# coding : utf-8

import sys
sys.path.append("..")
from scripts import preload
import wave

def separate_channels(input_file, left_output_file, right_output_file):
    try:
        with wave.open(input_file, 'rb') as wave_file:
            num_channels = wave_file.getnchannels()
            if num_channels != 2:
                print("Error: Input file is not stereo.")
                return

            frame_rate = wave_file.getframerate()
            num_frames = wave_file.getnframes()

            left_channel = wave.open(left_output_file, 'wb')
            right_channel = wave.open(right_output_file, 'wb')

            left_channel.setnchannels(1)
            left_channel.setsampwidth(wave_file.getsampwidth())
            left_channel.setframerate(frame_rate)

            right_channel.setnchannels(1)
            right_channel.setsampwidth(wave_file.getsampwidth())
            right_channel.setframerate(frame_rate)

            for i in range(num_frames):
                frames = wave_file.readframes(1)
                left_channel.writeframes(frames[:2])  # left channel
                right_channel.writeframes(frames[2:])  # right channel

            left_channel.close()
            right_channel.close()
            print("Channels separated successfully.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    VERSION = 1.0

    args = preload.Args("Wave Form Plotter", version = VERSION, description = "Plot wave from audio file with For FFT.")
    args.parser.add_argument("input", metavar = "PATH")
    arg = args.get()

    input_file = arg.input
    basename = "".join(input_file[:input_file.rfind(".")])
    left_output_file = basename + "(L).wav"
    right_output_file = basename + "(R).wav"

    separate_channels(input_file, left_output_file, right_output_file)

