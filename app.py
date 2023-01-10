from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai


def ask_chatgpt_question(prompt):
    openai.api_key = os.environ.get("OPENAI_API_TOKEN")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text


app = Flask(__name__)


@app.route("/", methods=["POST"])
# chatbot logic
def bot():

    # user input
    user_msg = request.values.get('Body', '')
    from_user_number = request.values.get('From', '')
    profile_name = request.values.get('ProfileName', '')
    print(request.values)
    if '@ai' in user_msg.lower():
        prompt = user_msg.replace(
            '@ai,', '').replace('@ai ,', '').replace('@ai ', '').replace('@ai', '')
        ai_response = ask_chatgpt_question(prompt)

        response = MessagingResponse()
        response.message(ai_response)
        return str(response)
