from pydub import AudioSegment
import librosa
import numpy as np
import soundfile as sf

# Function to apply echo
def apply_echo(audio_segment: AudioSegment, delay_ms=500, decay=0.6):
    echo = audio_segment - 30  # Reduce volume for the echo
    combined = audio_segment.overlay(echo, position=delay_ms)
    return combined

# Function to change pitch
def change_pitch(y, sr, n_steps):
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=n_steps)
    return y_shifted

# Function to change tempo
def change_tempo(y, factor):
    y_stretched = librosa.effects.time_stretch(y, factor)
    return y_stretched

def process_audio(file_path, output_path, echo_delay=500, pitch_steps=0, tempo_factor=1.0):
    # Load the audio file with pydub
    audio = AudioSegment.from_file(file_path)
    
    # Apply echo using pydub
    audio_with_echo = apply_echo(audio, delay_ms=echo_delay)

    # Export intermediate file to be processed by librosa
    temp_file = "temp.wav"
    audio_with_echo.export(temp_file, format="wav")
    
    # Load the audio file with librosa for pitch and tempo manipulation
    y, sr = librosa.load(temp_file, sr=None)

    # Change pitch
    y_pitch_shifted = change_pitch(y, sr, pitch_steps)

    # Change tempo
    y_final = change_tempo(y_pitch_shifted, tempo_factor)

    # Save the final output
    sf.write(output_path, y_final, sr)
    print(f"Processed audio saved as {output_path}")

# Example usage
file_path = "atiendoboludos.mp3"
output_path = "output_audio.wav"
process_audio(file_path, output_path, echo_delay=600, pitch_steps=2, tempo_factor=1.5)