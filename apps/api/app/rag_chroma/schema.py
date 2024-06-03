from langchain_core.pydantic_v1 import BaseModel

# Add typing for input
class Question(BaseModel):
    __root__: str