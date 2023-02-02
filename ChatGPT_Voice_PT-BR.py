import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pygame
import requests
import os
import random

def mic_result():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio,language='pt-BR')

        print("Você disse: " + frase)

    except sr.UnkownValueError:

        print("Não entendi")

    return frase

def post_gpt(frase):

    api_key = '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'

    headers = { "Authorization": "Bearer " + api_key }

    data = { "model": "text-davinci-003",
            "max_tokens": 1000,
            "prompt": frase }

    response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers).json()
    result = response.get("choices", "")[0].get("text", "")
    return result

def cria_audio2(audio):

    tts = gTTS(audio,lang='pt-br')

    file = str(random.randint(0, 9999)) + '.mp3'

    tts.save(file)

    print("Estou aprendendo o que você disse...")

    playsound(file)

def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    
    file = str(random.randint(0, 9999)) + '.mp3'

    tts.save(file)
    
    pygame.init()
    print("Estou aprendendo o que você disse...")
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
        
    pygame.quit()
    os.remove(file)

def main():
    frase = mic_result()
    resultado_gpt = post_gpt(frase)
    cria_audio(resultado_gpt)

if __name__ == '__main__':
    main()