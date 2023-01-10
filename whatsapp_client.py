# import os
# import requests

# import json


# class WhatsAppWrapper:

#     API_URL = "https://graph.facebook.com/v15.0/"
#     API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN")
#     NUMBER_ID = os.environ.get("WHATSAPP_NUMBER_ID")

#     def __init__(self):
#         self.headers = {
#             "Authorization": f"Bearer {self.API_TOKEN}",
#             "Content-Type": "application/json",
#         }
#         self.API_URL = self.API_URL + self.NUMBER_ID

#     def send_template_message(self, template_name, language_code, phone_number):

#         payload = json.dumps({
#             "messaging_product": "whatsapp",
#             "to": phone_number,
#             "type": "template",
#             "template": {
#                 "name": template_name,
#                 "language": {
#                     "code": language_code
#                 }
#             }
#         })

#         response = requests.request("POST", f"{self.API_URL}/messages", headers=self.headers, data=payload)

#         assert response.status_code == 200, "Error sending message"

#         return response.status_code
    
#     def process_webhook_notification(self, data):
#         """_summary_: Process webhook notification
#         For the moment, this will return the type of notification
#         """
#         print(data)
#         response = []

#         for entry in data["entry"]:

#             for change in entry["changes"]:
#                 response.append(
#                     {
#                         "type": change["field"],
#                         "from": change["value"]["metadata"]["display_phone_number"],
#                     }
#                 )
#         # Do whatever with the response
#         return response
    
    
# import os
# from flask import Flask, jsonify, request
# from flask import render_template
# from whatsapp_client import WhatsAppWrapper

# app = Flask(__name__)

# VERIFY_TOKEN = os.environ.get('WHATSAPP_HOOK_TOKEN')

# @app.route("/")
# def hello_world():
#     return render_template("index.html")

# @app.route("/send_template_message/", methods=["POST"])
# def send_template_message():
#     """_summary_: Send a message with a template to a phone number"""

#     if "language_code" not in request.json:
#         return jsonify({"error": "Missing language_code"}), 400

#     if "phone_number" not in request.json:
#         return jsonify({"error": "Missing phone_number"}), 400

#     if "template_name" not in request.json:
#         return jsonify({"error": "Missing template_name"}), 400

#     client = WhatsAppWrapper()

#     response = client.send_template_message(
#         template_name=request.json["template_name"],
#         language_code=request.json["language_code"],
#         phone_number=request.json["phone_number"],
#     )

#     return jsonify(
#         {
#             "data": response,
#             "status": "success",
#         },
#     ), 200
    
# @app.route("/webhook/", methods=["POST", "GET"])
# def webhook_whatsapp():
#     """__summary__: Get message from the webhook"""
#     print(request.get_json())
#     if request.method == "GET":
#         if request.args.get('hub.verify_token') == VERIFY_TOKEN:
#             return request.args.get('hub.challenge')
#         return "Authentication failed. Invalid Token."

#     client = WhatsAppWrapper()

#     response = client.process_webhook_notification(request.get_json())

#     # Do anything with the response
#     # Sending a message to a phone number to confirm the webhook is working
#     print(response)

#     return jsonify({"status": "success"}, 200)

    