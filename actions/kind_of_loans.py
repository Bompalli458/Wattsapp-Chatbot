from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from typing import Dict, Text, Any, List

from rasa_sdk.executor import CollectingDispatcher


class ActionUtterApplyLoans(Action):
    def name(self) -> Text:
        return "kind_of_loans"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your custom logic to handle the 'utter_apply_loans' action
        # For example, you can provide a message guiding the user on how to apply for loans
        dispatcher.utter_message(text="What kind of loan Do you want to apply ?")
        dispatcher.utter_message(text=" 1. Personal Loan")
        dispatcher.utter_message(text=" 2. Business Loan")
        dispatcher.utter_message(text=" 3. StartUp Loan")

        return []



