import re
import unicodedata


def clean_html(text, normalize=False):
    if text is None:
        return None

    clean_text = re.sub('<br>', '\n', text)
    clean_text = re.sub('</br>', '\n', clean_text)
    clean_text = re.sub('<.*?>', '', clean_text)
    clean_text = re.sub(' +', ' ', clean_text)
    if normalize:
        clean_text = unicodedata.normalize("NFKD", clean_text)
    return clean_text
