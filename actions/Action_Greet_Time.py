from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List

from rasa_sdk.executor import CollectingDispatcher


class ActionGreetBasedOnTime(Action):
    def name(self) -> Text:
        return "action_greet_based_on_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_time = datetime.now().time()
        hour = current_time.hour

        if 5 <= hour < 12:
            greeting_message = "Good morning! 🌞"
        elif 12 <= hour < 18:
            greeting_message = "Good afternoon! 🌤️"
        else:
            greeting_message = "Good evening! 🌙"

        # Get the sender's name from the metadata (Twilio "whatsapp" channel)
        # metadata = tracker.current_state()["metadata"]
        # name = metadata.get("whatsapp", {}).get("From")
        #
        # # If name is not available, use a default name (e.g., "User")
        # if not name:
        #     name = "User"
        name="User"

        dispatcher.utter_message(text=f"Hello {name} {greeting_message} How can I assist you today?" )
        return []
