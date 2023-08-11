import logging
from sanic import Blueprint, response
from rasa.core.channels import RestInput, UserMessage
import json

logger = logging.getLogger(__name__)

class TwilioInput(RestInput):
    @classmethod
    def name(cls) -> str:
        return "twilio"

    def blueprint(self, on_new_message):
        twilio_webhook = Blueprint("twilio_webhook", __name__)

        @twilio_webhook.route("/webhooks/twilio/webhook", methods=["POST"])
        async def receive(request):
            payload = json.loads(request.body.decode("utf-8"))
            sender = payload.get("From")  # Get the WhatsApp number (name) of the sender
            text = payload.get("Body")
            intent = text.lower()  # Use the message text directly as the intent name
            metadata = {
                "client": "twilio",
                "whatsapp": {
                    "From": sender,
                    "Body": text,
                },
            }
            if text.startswith("/"):
                metadata["status"] = "action"
            else:
                metadata["status"] = "user"

            # Include the sender's WhatsApp number as the user name
            if sender:
                metadata["user"] = sender

            await on_new_message(UserMessage(
                text, self.output_channel, sender, input_channel=self.name(),
                metadata=metadata
            ))
            return response.text("")

        return twilio_webhook
