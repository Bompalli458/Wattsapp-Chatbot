# from typing import Any, Text, Dict, List
#
# import mysql.connector
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
#
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
#
# class ExtractDetailsAction(Action):
#     def name(self) -> Text:
#         return "action_extract_details"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print(mysql.connector.__version__)
#         name = None
#         phone_number = None
#         for entity in tracker.latest_message.get("entities", []):
#             if entity["entity"] == "name":
#                 name = entity["value"]
#                 logger.debug(name)
#             elif entity["entity"] == "phone_number":
#                 phone_number = entity["value"]
#                 logger.debug(phone_number)
#         return [SlotSet("name", name), SlotSet("phone_number", phone_number)]
