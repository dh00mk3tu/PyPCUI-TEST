import tkinter as tk
from googletrans import Translator


frame = tk.Tk()

frame.title("Translator Test ")
frame.geometry("570x100")

def trans_fr() :
    input = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(input, dest="fr")
    Translated_Text = tk.Label(frame, text=f"Translation fr : {translation.text}", bg='green')
    display = tk.Entry(frame)
    Translated_Text.grid(row=1, column=1)

def trans_ru() :
    input = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(input, dest="ru")
    Translated_Text = tk.Label(frame, text=f"Translation ru : {translation.text}", bg='yellow')
    display = tk.Entry(frame)
    Translated_Text.grid(row=2, column=1)

label = tk.Label(frame, text="Text to Translate :")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0,column=1)

btn_french = tk.Button(frame, text = "Translate to French", command=trans_fr)
btn_french.grid(row=0, column=2)

btn_ru = tk.Button(frame, text = "Translate to Russian", command=trans_ru)
btn_ru.grid(row=0, column=3)

frame.mainloop()
