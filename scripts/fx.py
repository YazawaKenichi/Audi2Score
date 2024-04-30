#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.append("..")
from scripts import preload

import numpy as np
import matplotlib.pyplot as plt
import wave

def plot_waveform(audio_file):
    # オーディオファイルを読み込む
    with wave.open(audio_file, 'rb') as wf:
        # サンプル数を取得
        num_frames = wf.getnframes()
        # サンプルレートを取得
        sample_rate = wf.getframerate()
        # オーディオの長さを計算
        duration = num_frames / float(sample_rate)

        # オーディオデータを読み込む
        audio_data = wf.readframes(num_frames)
        # オーディオデータをnumpy arrayに変換
        audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # 時間軸を生成
    time = np.linspace(0, duration, num_frames)

    # 振幅のグラフを描画
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_array, color='b')
    plt.title('Waveform of audio')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    VERSION = 1.0

    args = preload.Args("Wave Form Plotter", version = VERSION, description = "Plot wave from audio file.")
    args.parser.add_argument("input", metavar = "PATH")
    arg = args.get()

    audio_file = arg.input
    plot_waveform(audio_file)

