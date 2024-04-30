#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import numpy as np
import wave

def generate_sine_wave(freq, duration, sample_rate = 44100, amplitude = 32767):
    _amplitude = 32767 * amplitude
    # サンプル数を計算
    num_samples = int(sample_rate * duration)

    # サイン波を生成
    time = np.linspace(0, duration, num_samples)
    sine_wave = _amplitude * np.sin(2 * np.pi * freq * time)

    return sine_wave.astype(np.int16)

def save_wav(filename, data, sample_rate=44100, num_channels=1, sample_width=2):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(num_channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())

if __name__ == "__main__":
    VERSION = 1.0

    args = preload.Args("GenWAV", version = VERSION, description = "Generate single wave audio file.")
    args.parser.add_argument("-f", "--freq", default = 440, dest = "freq", metavar = "FREQUENCY", type = float, help = "[float] Frequency of generat wave. Default : 440")
    args.parser.add_argument("-d", "--duration", default = 5, dest = "duration", metavar = "DURATION", type = float, help = "[float] Duration of generat wave. Default : 5; Unit : second")
    args.parser.add_argument("-a", "--amplitude", default = 1, dest = "amplitude", metavar = "AMPLITUDE", type = float, help = "[float] Amplitude of generat wave. Default : 1; Range : 0 <= Amplitude <= 1;")
    args.parser.add_argument("-s", "--sample", default = 44100, dest = "sample", metavar = "SAMPLE_RATE)", type = int, help = "[ int ] Sample Rate of generate wave. Default : 44100")
    args.parser.add_argument("output", metavar = "PATH", )
    arg = args.get()

    freq = arg.freq
    duration = arg.duration
    amplitude = arg.amplitude
    sample = arg.sample
    filename = arg.output

    sine_wave = generate_sine_wave(freq, duration, sample_rate = sample, amplitude = amplitude)
    save_wav(filename, sine_wave)

