from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class CustomAction(Action):
    def name(self) -> Text:
        return "action_custom"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



        # Retrieve the buttons from the utterance
        # latest_message = tracker.latest_message
        # print(latest_message)
        #
        # buttons = tracker.latest_message.get('buttons', [])
        # print(buttons)
        #
        # # Extract the payload values
        # payloads = [button.get('payload') for button in buttons]
        #
        # # Perform actions based on the payload values
        # if '/check_status' in payloads:
        #     # Logic for checking loan status
        #     dispatcher.utter_message(text="You have selected 'Check Status'.")
        #     # Additional actions or logic for checking loan status
        # elif '/apply_loan' in payloads:
        #     # Logic for applying loans
        #     dispatcher.utter_message(text="You have selected 'Apply Loans'.")
        #     # Additional actions or logic for applying loans
        # else:
        #     # Handle unknown button payloads
        #     dispatcher.utter_message(text="Sorry, I couldn't recognize your selection.")
        # print(buttons)
        #
        # # Extract the payload values
        # payloads = [button.get('payload') for button in buttons]
        #
        # # Perform actions based on the payload values
        # if '/check_status' in payloads:
        #     # Logic for checking loan status
        #     dispatcher.utter_message(text="You have selected 'Check Status'.")
        #     # Additional actions or logic for checking loan status
        # elif '/apply_loan' in payloads:
        #     # Logic for applying loans
        #     dispatcher.utter_message(text="You have selected 'Apply Loans'.")
        #     # Additional actions or logic for applying loans
        # else:
        #     # Handle unknown button payloads
        #     dispatcher.utter_message(text="Sorry, I couldn't recognize your selection.")





        buttons=[
            {"payload":'/apply_efundzz_loan{"content_type":"apply"}', "title":"Apply Efundzz Loan"},
            {"payload":'/status_efundzz_loan{"content_type":"status"}', "title":"Status Efundzz Loan"}
        ]
        dispatcher.utter_message(text=" Hello!! How can i assist you today ", buttons=buttons)

        return []
