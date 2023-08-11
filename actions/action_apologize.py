


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionApologize(Action):
    def name(self) -> Text:
        return "action_apologize"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Respond with an apology message
        dispatcher.utter_message(text="I'm sorry, but I didn't understand that. Can you please rephrase your question?")
        return []
