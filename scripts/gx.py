#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

def audifft(audio_file):
    # wavファイルを読み込む
    sample_rate, audio_data = wavfile.read(audio_file)
    # フーリエ変換を行う
    fft_output = fft(audio_data)
    # フーリエ変換の結果を周波数に変換
    freqs = np.fft.fftfreq(len(fft_output), 1/sample_rate)
    return freqs, np.abs(fft_output)

def plot_frequency_spectrum(audio_file):
    # 振幅スペクトルの計算
    _, amplitude_spectrum = audifft(audio_file)

    # プロット
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:len(freqs)//2], amplitude_spectrum[:len(freqs)//2])
    plt.title('Frequency Spectrum of audio')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.xlim(20, 20000)
    plt.show()

if __name__ == "__main__":
    VERSION = 1.01

    args = preload.Args("Wave Form Plotter", version = VERSION, description = "Plot wave from audio file with For FFT.")
    args.parser.add_argument("input", metavar = "PATH")
    arg = args.get()

    audio_file = arg.input
    plot_frequency_spectrum(audio_file)

