
 
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class QueryRequest(BaseModel):
    query: str =  Field(description="Query to be passed as an argument. Always use this")
    senderId: str =  Field(description="Sender id to be passed as an argument. Always use this")
    streaming:bool = Field(description="Streaming bool value to be passed as an arguement. Always use this.")
   
  

class QueryInput(BaseModel):
    query: str =  Field(description="Query to be passed as an argument. Always use this")
   
  

