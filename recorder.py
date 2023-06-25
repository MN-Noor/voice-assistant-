# pip install sounddevice
# pip install wavio
#pip install pyaudio
import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write
import time
import gsp
import codex

freq=48000
duration=5
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
 
sd.wait()
 
# timestamp string to generate audio files every time with differnt names
timestamp = time.strftime("%Y%m%d-%H%M%S")
f_name = "rec"
file_name = f"{f_name}_{timestamp}.wav"
print(file_name) 
# Convert the NumPy array to audio file
wv.write(file_name, recording, freq, sampwidth=2)
transcript=gsp.transcription(file_name)
prompt ="Postgres SQL tables, with their properties:"+transcript
Query=codex.generate_sql_query(prompt)
print (Query)


