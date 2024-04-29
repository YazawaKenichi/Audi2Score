#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import wave

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=32767):
    # サンプル数を計算
    num_samples = int(sample_rate * duration)

    # サイン波を生成
    time = np.linspace(0, duration, num_samples)
    sine_wave = amplitude * np.sin(2 * np.pi * freq * time)

    return sine_wave.astype(np.int16)

def save_wav(filename, data, sample_rate=44100, num_channels=1, sample_width=2):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(num_channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())

if __name__ == "__main__":
    freq = float(input("生成するサイン波の周波数を入力してください（Hz）: "))
    duration = float(input("生成するサイン波の長さを入力してください（秒）: "))
    filename = 'audio.wav'

    sine_wave = generate_sine_wave(freq, duration)
    save_wav(filename, sine_wave)

    print(f"{filename} が生成されました。")

