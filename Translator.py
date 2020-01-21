import tkinter as tk
from googletrans import Translator


frame = tk.Tk()

frame.title("Translator Test ")
frame.geometry("370x100")

def trans() :
    input = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(input, dest="fr")
    Tranlated_Text = tk.Label(framae, text=f'Translation : {translation.text}', bg='green')
    TRanslated_Text.grid(row=1, column=1)

label = tk.Label(frame, text="Text to  Translate :")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0,column=1)

button = tk.Button(frame, text = "Translate", command=trans)
button.grid(row=0, column=2)

frame.mainloop()
