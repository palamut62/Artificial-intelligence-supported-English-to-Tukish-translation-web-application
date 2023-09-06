from deep_translator import MyMemoryTranslator
from gtts import gTTS
def english_to_french(english_text):
    """
    Function to translate English text to French.

    Parameters:
    english_text (str): Text in English to be translated to French

    Returns:
    str: Translated text in French
    """
    return MyMemoryTranslator(source='english', target='turkish').translate(english_text)

def french_to_english(french_text):
    """
    Function to translate French text to English.

    Parameters:
    french_text (str): Text in French to be translated to English

    Returns:
    str: Translated text in English
    """
    return MyMemoryTranslator(source='turkish', target='english').translate(french_text)
def text_to_speech(text):
    """
    Function to translate  text to speech.

    Parameters:
    text (str): Text to be translated to speech

    Returns:
    str: Translated text in speech
    """

    # Seslendirmek istediğin metin
    metin = text

    # Metni Türkçe olarak seslendir
    tts = gTTS(text=metin, lang='tr')

    # Ses dosyasını kaydet
    tts.save("merhaba.mp3")

    # Ses dosyasını oynat (Linux ve MacOS için)
    os.system("start /c merhaba.mp3")
