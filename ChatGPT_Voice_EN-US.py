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
        print("Say something: ")
        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio,language='en-US')

        print("You said: " + frase)

    except sr.UnkownValueError:

        print("I didn't understand")

    return frase

def post_gpt(frase):

    api_key = '' #insert your API key inside the string

    headers = { "Authorization": "Bearer " + api_key }

    data = { "model": "text-davinci-003",
            "max_tokens": 1000,
            "prompt": frase }

    response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers).json()
    result = response.get("choices", "")[0].get("text", "")
    return result

def cria_audio2(audio):

    tts = gTTS(audio,lang='en-us')

    file = str(random.randint(0, 9999)) + '.mp3'

    tts.save(file)

    print("I'm thinking...")

    playsound(file)

def cria_audio(audio):
    tts = gTTS(audio,lang='en-us')
    
    file = str(random.randint(0, 9999)) + '.mp3'

    tts.save(file)
    
    pygame.init()
    print("I'm thinking...")
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
        
    pygame.quit()
    os.remove(file)

def main():
    context = ""
    while True:
        try:
            frase = mic_result()
            prompt = context + frase
            resultado_gpt = post_gpt(prompt)
            if resultado_gpt.startswith('!'):
                resultado_gpt = resultado_gpt[1:]
            elif resultado_gpt.startswith('?'):
                resultado_gpt = resultado_gpt[1:]
            cria_audio(resultado_gpt)
            context = resultado_gpt
        except:
            print('Ok, thanks for the chat!')
            break

if __name__ == '__main__':
    main()