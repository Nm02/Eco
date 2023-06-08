import speech_recognition as sr
import pyttsx3, pywhatkit

#Dice algo
def talk(text:str='hola'):
    engine.say(text)
    engine.runAndWait()

#Escucha a travez del microfono
def listen()->list:
    try:
        with mic as source:
            print('Escuchando...')
            audio=listener.listen(source) #Empieza a escuchar
            msg=listener.recognize_google(audio,language="Es")#Reconoce el contenido de la variable audio utilizando como parametro el lenguaje español
            msg=msg.lower()
            # print(msg)
            # msg="quiero que eco reproduzca algo"
            if name in msg:
                msg=msg.split()
                poss=msg.index(name)
                msg=msg[poss+1:]

            else:
                msg=[]

    except Exception as E:
        msg=[]

    return msg

#Funcion principal del bot
def run_Aura():
    comando=listen()
    if len(comando)>0:
        if comando[0]=='reproduce':
            comando.remove('reproduce')
            music=' '.join(comando)
            print('reproduciendo',music)
            talk('reproduciendo '+ music)
            pywhatkit.playonyt(music)
        else:
            talk('Disculpe, no lo entendi')

name = 'eco' #Nombre de la ia

mic=sr.Microphone() #Creo una variable para guardar mi microfono
listener=sr.Recognizer() #Creo variable para el recognizer (Reconocimiento de voz)
engine=pyttsx3.init() #Inicializo pyttsx3

voices=engine.getProperty('voices') #Obtiene las voces disponibles
engine.setProperty('voices',voices[0].id) #Setea la voz segun el indice: 0=Sabina (español de mexico), 1=Helena (español de españa) y 2 Zira (Ingles)

if __name__=="__main__":
    run_Aura()
