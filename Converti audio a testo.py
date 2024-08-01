import PySimpleGUI as sg
import speech_recognition as sr
import pyperclip

sg.theme('DarkBlue14') 
sg.set_options(font=('Helvetica', 14))

layout = [[sg.Text("Parlato a testo")],
          [sg.Multiline (size=(70, 20), key="-OUTPUT-")],
          [sg.Button("Registra", button_color=('white', 'gray'), border_width=10),
           sg.Button("Copia", button_color=('white', 'blue'), border_width=10),
           sg.Button("Esci", button_color=('white', 'red'), border_width=10)]]

window = sg.Window("Parlato a testo", layout)

while True:
    event, values = window.read()

    if event == "Esci" or event == sg.WIN_CLOSED:
        break
    elif event == "Registra":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=10000)  # Imposta un timeout alto
        try:
            text = r.recognize_google(audio, language='it-IT')  # Imposta la lingua su italiano
            window["-OUTPUT-"].update(text)
        except sr.UnknownValueError:
            window["-OUTPUT-"].update("Non ho capito...")
        except sr.RequestError as e:
            window["-OUTPUT-"].update(f"Errore: {e}")
    elif event == "Copia":
        text = values["-OUTPUT-"]
        pyperclip.copy(text)

window.close()
