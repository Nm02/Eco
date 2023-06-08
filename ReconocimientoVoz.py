import speech_recognition as sr

recognizer=sr.Recognizer() #Creo variable para el recognizer (Reconocimiento de voz)

mic=sr.Microphone() #Creo una variable para guardar mi microfono


#Escucha y reconoce la entrada del micro
with mic as source:
    audio =recognizer.listen(source)

text=recognizer.recognize_google(audio,language="Es")#Reconoce el contenido de la variable audio utilizando como parametro el lenguaje español

print(f"has dicho: {text}")



