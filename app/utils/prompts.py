from langchain.prompts import PromptTemplate

extract_topics_prompt = PromptTemplate(
    template="""
You are an AI that extracts the main topics, objects, or themes from user requests for image searches.
User Request: {user_input}

Output schema:
    TopicList: list of topics extracted from user_input
    exists: 
        - True if the user is actually talking about finding images
        - False if the user is just having a general greeting
    response: 
        - Respond to the user in a witty manner if it is just a greeting or something similar
        - If the user is talking about finding images, respond appropriately listing what you think he should search for when searching for images.
        - Tell them that you'll find those for him


Example 
Input: I want to find some cool pictures of X
Output: Use provided pydantic schema to produce output
    TopicList: ["X", "Y", "Z"]
    exists: True
    response: To find cool X pictures I would ideally search for phrases like X, Y etc. on open source image services. Let me find those for you!!
""",
    input_variables=["user_input"]
)