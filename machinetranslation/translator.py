from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Function to translate English text to French.

    Parameters:
    english_text (str): Text in English to be translated to French

    Returns:
    str: Translated text in French
    """
    return MyMemoryTranslator(source='english', target='french').translate(english_text)

def french_to_english(french_text):
    """
    Function to translate French text to English.

    Parameters:
    french_text (str): Text in French to be translated to English

    Returns:
    str: Translated text in English
    """
    return MyMemoryTranslator(source='french', target='english').translate(french_text)
