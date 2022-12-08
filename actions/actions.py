# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import json
import string
import random

class SubmitToDatabase(Action):

    def name(self) -> Text:
        return "action_submit_to_database"

    def run(
        self,
        dispatcher:CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
     ) -> List[Dict]:

        quantity = tracker.get_slot("quantity")
        order_item = tracker.get_slot("order_items")
        name = tracker.get_slot("name")
        phone = tracker.get_slot("phone")
        address = tracker.get_slot("address")

        pesanan = {
            "name" : name,
            "order_item": order_item,
            "quantity" : quantity,
            "phone" : phone,
            "address" : address
        }

        # Serializing json
        json_object = json.dumps(pesanan, indent=4)

        # Make order_id
        chars = string.ascii_uppercase + string.digits
        pesanan_id = ''.join(random.choice(chars) for _ in range(6))

        # Writing to sample.json
        with open(f"./output/{pesanan_id}.json", "w") as outfile:
            outfile.write(json_object)
 
        dispatcher.utter_message(text="Pesanan Berhasil Diproses!")

        return []




