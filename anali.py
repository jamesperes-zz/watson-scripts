from watson_developer_cloud import ToneAnalyzerV3
from pprint import pprint as print
import operator


def analisa(texto):
    tone_analyzer = ToneAnalyzerV3(
        username='USERNAME',
        password='PASSWORD',
        version='2016-02-11')

    anali = tone_analyzer.tone(text=texto)

    emocao = []
    lingaguem = []
    tendencia = []

    for obj in anali['document_tone']['tone_categories']:
        if obj['category_id'] == 'emotion_tone':
            for an in obj['tones']:
                tone = an['tone_name']
                score = an['score']
                chave = (tone, score)
                emocao.append(chave)
        elif obj['category_id'] == 'writing_tone':
            for an in obj['tones']:
                tone = an['tone_name']
                score = an['score']
                chave = (tone, score)
                lingaguem.append(chave)
        else:
            for an in obj['tones']:
                tone = an['tone_name']
                score = an['score']
                chave = (tone, score)
                tendencia.append(chave)

    a = max(emocao, key=lambda item: item[1])
    b = max(lingaguem, key=lambda item: item[1])
    c = max(tendencia, key=lambda item: item[1])
    print(a)
    print(b)
    print(c)
