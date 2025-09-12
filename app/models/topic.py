from pydantic import BaseModel,Field
from typing import List

class TopicList(BaseModel):
    topic_list: List[str] = Field(
        description="List of topics that can be used to search for images catered to the user's needs",
        example="[mountains, hills, cool monutain peaks]",
        min_items = 4
    )
    exists: bool = Field(
        description="True if the query is talking about searching images, False if just general greeting"
    )
    response: str = Field(
        description="Appropriate response for the user depending on if he asked for a greeting or for images"
    )
    