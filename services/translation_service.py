from deep_translator import GoogleTranslator

def translate_text(text, dest_lang):
    try:
        translation = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translation
    except Exception as e:
        print(f"Translation error: {e}")
        return text
