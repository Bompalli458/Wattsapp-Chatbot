from typing import Any, Text, Dict, List, Union

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class PersonalLoanStatus(Action):
    """Form action for collecting personal loan status information."""

    def name(self) -> Text:
        return "action_personal_loan_status"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # Check if the form is active and slots are filled
        # if tracker.active_form.get("name") == "personal_loan_status_form":
        #     aadhar_number = tracker.get_slot("aadhar_number")
        #     pan_number = tracker.get_slot("pan_number")
        #     phone_number = tracker.get_slot("phone_number")

            # Perform validation of the slot values, if needed
        # aadhar_number="467809028779"
        phone_number="6281668227"
        # pan_number="GWDPB0032C"


        response = requests.get(f'http://localhost:8058/efundzz/personalloan/status/{phone_number}')

        # print(response)


                # Check the response status code
        if response.status_code == 200:

            loan_status = response.text
            dispatcher.utter_message(text=f"Your personal loan status: {loan_status}")
        else:
            dispatcher.utter_message(text="Sorry, an error occurred while retrieving the loan status. Please try again later.")

            # Clear the slots after form submission


        # Return an empty list if the form is not active
        return []
