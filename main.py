# main.py
from chatbot.intent_model import IntentModel
from chatbot.dialog_manager import DialogManager

def run():
    intent_model = IntentModel("data/intents.json")
    dialog_manager = DialogManager(intent_model.intents)

    print("Chatbot gestartet (exit zum Beenden)")
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Tschüss!")
            break

        response = dialog_manager.get_response(user_input, intent_model)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run()