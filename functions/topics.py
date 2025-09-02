import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.models import llm
from pydantic_models.topic import TopicList
from utils.prompts import extract_topics_prompt
from functions.unsplash_api import search_unsplash

def call_llm(user_query: str):
    user_prompt = extract_topics_prompt.format(user_input=user_query)

    structured_llm = llm.with_structured_output(TopicList)
    result = structured_llm.invoke(user_prompt)

    return result
    
def extract_topics(user_query: str):
    print("Calling LLM to understand intent of the user..")
    result = call_llm(user_query)
    result = result.model_dump()

    if result["exists"]==False:
        print("User likely asking something generic")
        return result["response"], None
    else:
        topics = result["topic_list"]
        print(f"Running Unsplash for the list of topics:\n{topics}")

        pics_dict={}
        for topic in topics:
            pictures_response = search_unsplash(topic)
            pictures = [pic['urls']['regular'] for pic in pictures_response]

            pics_dict[topic] = pictures
            print(f"{len(pictures)} found for {topic}")

        return result["response"], pics_dict
    
# reponse, pics = extract_topics('Find me some cool pictures of mountains')
# print(f"\nResponse: {reponse}")