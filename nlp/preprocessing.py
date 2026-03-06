# nlp/preprocessing.py
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Synonyme / Abkürzungen
SYNONYM_MAP = {
    "kiu": "ki",
    "mpl": "ml",
    "mlö": "ml",
    "mlo": "ml",
    "mmmml": "ml",
    "dpl": "dl",
    "dplp": "dl",
    "ddlldp": "dl",
    "dlp": "dl",
    "klö": "ki"
}

# Deutsche Stopwords
STOPWORDS = set(stopwords.words("german"))

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # Kleinbuchstaben
    text = text.lower()

    # Sonderzeichen entfernen
    text = re.sub(r"[^a-zäöüß0-9\s]", "", text)

    # Tokenisierung
    tokens = word_tokenize(text, language="german")

    # Stopwords entfernen
    tokens = [t for t in tokens if t not in STOPWORDS]

    # Lemmatisierung
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    # Synonyme/Abkürzungen ersetzen
    tokens = [SYNONYM_MAP.get(t, t) for t in tokens]

    return tokens