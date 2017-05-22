# coding=utf-8

from watson_developer_cloud import LanguageTranslatorV2


def traduz(texto):
    language_translator = LanguageTranslatorV2(
        username='USERNAME',
        password='PASSWORD')

    traducao = language_translator.translate(texto, source='en', target='pt-br')

    print(traducao)

    return traducao
