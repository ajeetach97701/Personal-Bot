from dotenv import load_dotenv, find_dotenv
import os
import json
import requests
import re


import redis
import pprint
import uvicorn
import nest_asyncio
from mdprint import mdprint
import email.message, smtplib
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveJsonSplitter
from langchain.schema import Document
import json ,csv
from pathlib import Path


from enum import Enum
from models.milvus import drop_collection


from typing import Optional

from fastapi import FastAPI
from langchain.schema import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.callbacks.manager import get_openai_callback
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap
from langchain_community.document_loaders import TextLoader
from pydantic import BaseModel, Field
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import CharacterTextSplitter

from langchain_chroma import Chroma
from langchain_milvus import Milvus
from queue import Queue
from models.model import get_embeddings



from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.output_parsers.json import JsonOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import RedisChatMessageHistory

from Schema.queryInput import *
from Schema.prompts import *
    
from models.localdata import localdata
from models.vars import DELETE_HISTORY_QUERYS

from models.redis import getData,setData,deleteData,flushAll



REDIS_SERVER=os.getenv('REDIS_SERVER')  or 'localhost'


string_parser= StrOutputParser()
json_parser = JsonOutputParser()




# host = os.getenv('HOST') 
# port = os.getenv('PORT') 



name = os.getenv("NAME")



from math import radians, sin, cos, sqrt, atan2

