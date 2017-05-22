"""Sample code to use the IBM Watson Speech to Text API.
See more at https://blog.rmotr.com.
"""

from watson_developer_cloud import SpeechToTextV1
from anali import analisa
from traduz import traduz
from som import som

IBM_USERNAME = "USERNAME"
IBM_PASSWORD = "PASSWORD"

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD)
audio_file = open("sillas2.ogg", "rb")

texto_recebido = ''

result = stt.recognize(audio_file, content_type="audio/ogg",
                       continuous=True, timestamps=False,
                       max_alternatives=1)
for obj in result['results']:
    for texto in obj['alternatives']:
        texto_recebido = texto_recebido + texto['transcript']
    # print(result)

print(texto_recebido)
analisa(texto_recebido)
traduz(texto_recebido)
som(traduz(texto_recebido))