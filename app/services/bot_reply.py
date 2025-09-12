import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.extract_topics import extract_topics
import traceback

def bot_reply(user_query: str):
    try:
        response, images = extract_topics(user_query)
    except Exception as e:
        response = "Sorry chatbot offline it seems!😓"
        images = {}
        print(f"Error occured")
        traceback.print_exc()

    return response, images