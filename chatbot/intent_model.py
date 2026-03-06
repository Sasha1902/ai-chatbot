# chatbot/intent_model.py
import json
import random
from difflib import SequenceMatcher
from nlp.preprocessing import preprocess

class IntentModel:
    def __init__(self, json_path):
        # JSON-Datei laden
        with open(json_path, encoding="utf-8") as f:
            self.intents = json.load(f)["intents"]

        # Patterns vorbereiten
        for intent in self.intents:
            intent["patterns"] = [" ".join(preprocess(p)) for p in intent["patterns"]]

        # Shortcuts für schnelle Fach-Intent-Erkennung
        self.shortcuts = {
            "ki": "ki_erklären",
            "ml": "ml_erklären",
            "dl": "dl_erklären"
        }

    def predict_intent(self, text):
        clean_text = " ".join(preprocess(text)).lower()

        # 1️⃣ Shortcuts zuerst
        for shortcut, tag in self.shortcuts.items():
            if shortcut in clean_text:
                return tag, 1.0

        # 2️⃣ Fuzzy Matching
        best_intent = None
        best_score = 0.0

        for intent in self.intents:
            for pattern in intent["patterns"]:
                score = SequenceMatcher(None, clean_text, pattern.lower()).ratio()
                if score > best_score:
                    best_score = score
                    best_intent = intent["tag"]

        return best_intent, best_score

    def predict_response(self, text):
        intent, score = self.predict_intent(text)

        if intent and score >= 0.55:
            for i in self.intents:
                if i["tag"] == intent:
                    return random.choice(i["responses"])

        return "Dazu habe ich leider keine Informationen. Meinst du vielleicht KI, ML oder DL?"