from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
import os
from models.new_handler import NewCallbackHandler

from queue import Queue
tool_queue = Queue()
tool_handler = NewCallbackHandler(queue=tool_queue) 


api_key = os.getenv('OPENAI_API_KEY')





def get_llm(model:str='gpt-3.5-turbo'):
    llm = ChatOpenAI(api_key=api_key, streaming=True, callbacks = [tool_handler])
    return llm
  
    
def get_embeddings(name:str = None):
    if name == "openai":
        embeddings=OpenAIEmbeddings(api_key=api_key)
        return embeddings 
    else:
        return "Only Open ai embeddings works for now."