import tkinter as tk
from gtts import gTTS
from playsound import playsound

# Window frame
frame = tk.Tk()
frame.title("Text To Speech Test")
frame.geometry("170x100")

# Main function
def ttspeech():
    input = entry.get()
    speech = gTTS(text=input, lang="ru")
    speech.save(r'G:\speech.mp3')
    playsound(r'G:\speech.mp3')

# Input statement label
input_text = tk.Label(frame, text="Enter The Text: ")
input_text.grid(row=0, column=0)

# Input entry function
entry = tk.Entry(frame)
entry.grid(row=1, column=0)

# Button
btn_enter = tk.Button(frame, text="Test", command = ttspeech)
btn_enter.grid(row=1, column=1)

frame.mainloop()