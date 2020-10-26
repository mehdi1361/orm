from googletrans import Translator

def get_translate(text, src, dest):
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text
