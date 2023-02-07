# ChatGPT_Voice_PT-BR

O projeto ChatGPT_Voice tem primeiramente o intuito de tornar a interação do usuário com o ChatGPT uma conversa natural e também atender usuários que tenham dificuldade para digitar no teclado ou que possuam alguma deficiência visual. O código utiliza a API do ChatGPT para obter as respostas geradas pelo microfone e então as informações são enviadas e transformadas pela biblioteca do Google Voice (gTTS) em áudio para o usuário. 

# Instruções

Instale as bibliotecas necessárias para o funcionamento do programa, as instruções estarão abaixo com seus respectivos comandos e sites para a instalação.
Obtenha uma chave da API do ChatGPT, disponível no site da OpenAI: https://openai.com/api/
Crie uma conta para obter o acesso.
Após fazer o login, clique em "Personal" na parte superior direita do site.
Acesse a aba "View API Keys"
Clique em "Create a new secret key" para gerar uma chave de acesso.
Copie a chave que aparecer e dentro do script, na linha 31, expanda a função "post_gpt" e cole o código da chave em "api_key".
Execute o script e espere a mensagem "Diga alguma coisa" aparecer no terminal. Quando ocorrer, fale algo para o microfone e a resposta será reproduzida em áudio. O processo continuará rodando até que o programa não receba nada pelo microfone, então ele se encerrará automaticamente.

# Instalação e versões das bibliotecas

speech_recognition, gTTS, playsound, pygame, requests, os, random
Versões utilizadas: SpeechRecognition: v3.9.0, gTTS: v2.3.1, playsound: v1.3.0, pygame: v2.1.2, requests: v2.27.1, os (built-in), random (built-in)
Sistema operacional utilizado: Windows 10

Para instalar cada biblioteca, copie e cole os seguintes comandos no seu prompt:

speech_recognition: pip install SpeechRecognition
gTTS: pip install gTTS
pygame: python3 -m pip install -U pygame --user
requests: python -m pip install requests

# Licença de uso

Este projeto está sob licença MIT. Leia o arquivo LICENSE.txt para mais detalhes.

Licenças das bibliotecas utilizadas:

- speech_recognition: 
Autor: Anthony Zhang;
Licença BSD; 
link: https://pypi.org/project/SpeechRecognition/
licença: https://github.com/Uberi/speech_recognition/blob/master/LICENSE.txt

- gTTS:
Autor: Pierre Nicolas Durette;
Licença MIT;
link: https://pypi.org/project/gTTS/;
licença: https://gtts.readthedocs.io/en/latest/license.html

- playsound:
Autor: Taylor Marks;
Licença MIT;
link: https://pypi.org/project/playsound/
licença: https://github.com/TaylorSMarks/playsound/blob/master/LICENSE

- pygame: 
Autor: Pete Shinners; 
Licença LGLP; 
link: https://www.pygame.org/docs/; 
licença: https://www.pygame.org/docs/LGPL.txt

- requests:
Autor: Kenneth Reitz;
Licença ASL;
link: https://pypi.org/project/requests/;
licença: https://www.apache.org/licenses/LICENSE-2.0
