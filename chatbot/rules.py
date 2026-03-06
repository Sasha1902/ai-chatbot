def get_rule_response(tokens):
    greetings = ["hallo", "hi", "hey"]
    farewells = ["tschüss", "auf wiedersehen", "bye"]
    help_words = ["hilfe", "support", "fragen"]

    text = " ".join(tokens).lower()

    if any(word in text for word in greetings):
        return "Hallo! Wie kann ich helfen?"
    elif any(word in text for word in farewells):
        return "Auf Wiedersehen! Viel Erfolg beim Lernen."
    elif any(word in text for word in help_words):
        return "Ich beantworte Fragen zu KI, ML und Deep Learning."
    else:
        return None