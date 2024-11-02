import sounddevice as sd
from scipy.io.wavfile import write
import subprocess


def record_audio():
# Set recording parameters
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording

    print("Recording...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Finished recording.")

# Save the recording as a WAV file
    write('output.wav', fs, myrecording)

# Convert WAV to MP3 using lameenc
    subprocess.call(["lame", "-V2", "output.wav", "output.mp3"])
