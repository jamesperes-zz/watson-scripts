
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

def som(texto):
    text_to_speech = TextToSpeechV1(
        username='USERNAME',
        password='PASSWORD',
        x_watson_learning_opt_out=True)  # Optional flag


    with open(join(dirname(__file__), 'output.ogg'), 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(texto, accept='audio/ogg', voice="pt-BR_IsabelaVoice"))