#!/usr/bin/env python3
# coding : utf-8

import librosa
import numpy as np
import music21

def extract_pitch(file_path):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Calculate onset strength
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Detect peaks in onset strength
    peaks = librosa.util.peak_pick(onset_env, pre_max=20, post_max=20, pre_avg=50, post_avg=50, delta=0.2, wait=1)

    # Convert peak indices to time stamps
    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr)

    # Extract pitches from peaks
    pitches = librosa.core.hz_to_midi(librosa.core.pitch.piptrack(y=y, sr=sr)[0])

    # Create a music21 Stream
    stream = music21.stream.Stream()

    # Convert pitches to music21 notes
    for peak in peaks:
        # Debugging: Output the content of pitches[peak]
        print(pitches[peak])

    # Convert pitches to music21 notes
    for peak in peaks:
        # Select pitch corresponding to the peak
        pitch_value = pitches[peak]
        # Convert pitch to music21 note
        note = music21.note.Note(float(pitch_value))
        stream.append(note)

    return stream

def save_sheet_music(stream, output_path):
    stream.write('midi', output_path)

# Example usage
file_path = '../output/audio.wav'
output_path = '../score.mid'
pitch_stream = extract_pitch(file_path)
save_sheet_music(pitch_stream, output_path)

