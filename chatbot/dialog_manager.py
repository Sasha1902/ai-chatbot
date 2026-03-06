# chatbot/dialog_manager.py
import difflib
from nlp.preprocessing import preprocess

RULE_RESPONSES = {
    "greetings": ["hallo","hi","hey","guten tag","guten morgen","servus","halloo"],
    "farewell": ["tschüss","auf wiedersehen","bye","bis bald","bis später"]
}

class DialogManager:
    def __init__(self, intents):
        self.intents = intents
        self.last_intent = None
        self.last_suggestion = None

    def get_response(self, text, intent_model):
        # Text vorverarbeiten
        clean_tokens = preprocess(text)
        clean_text = " ".join(clean_tokens)

        # Fachliche Intents vorhersagen
        intent, prob = intent_model.predict_intent(clean_text)
        if prob > 0.5:
            self.last_intent = intent
            return intent_model.predict_response(clean_text)

        # Regelbasierte Antworten
        lowered = text.lower()
        for greeting in RULE_RESPONSES["greetings"]:
            if difflib.get_close_matches(lowered, [greeting], n=1, cutoff=0.75):
                return "Hallo! Wie kann ich helfen?"
        for farewell in RULE_RESPONSES["farewell"]:
            if difflib.get_close_matches(lowered, [farewell], n=1, cutoff=0.75):
                return "Tschüss! Bis bald."

        # Fuzzy-Suggestion
        all_patterns = [p for intent in self.intents for p in intent["patterns"]]
        match = difflib.get_close_matches(clean_text, all_patterns, n=1, cutoff=0.75)
        if match:
            self.last_suggestion = match[0]
            return f"Meinst du '{match[0]}' statt '{text}'?"

        # Fallback
        return "Dazu habe ich leider keine Informationen. Meinst du vielleicht KI, ML oder DL?"