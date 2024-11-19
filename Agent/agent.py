from Libs.libs import *
from langchain.callbacks import get_openai_callback
from Tools.tools__init__ import *

REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'

from models.model import get_llm, tool_handler

llm = get_llm()
import os
from dotenv import load_dotenv
load_dotenv()
name = os.getenv("NAME")


def generate_response(request_data):        
    # llm = ChatOpenAI(api_key=api_key, temperature=0.7, streaming=True, callbacks = [tool_handler])
    print("Agent query:", request_data.query)
    prompt_agent = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                
               You are {name}. Greet the user Politely and always use the tool to answer the queries related to {name}. Remember you are {name}, a human being not a AI Assistant.
               Except for Hi, and hello. Always tools you have to answer the user queries.
                """
            
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ],
    )
    senderId = request_data.senderId


    toolsInstance = GetCustomTools(request_data)
    tools = toolsInstance.get_tools()
    # tools = [sport_tool]


    history_reddis = RedisChatMessageHistory(
        senderId, url=f"redis://{REDIS_SERVER}", ttl=60*60*3)

    messages = history_reddis.messages
    if len(messages) >= 3:
        redis_client = redis.StrictRedis.from_url(
            f"redis://{REDIS_SERVER}")
        length = len(messages)

        redis_client.ltrim(history_reddis.key, -length, -length+1)
        messages = history_reddis.messages
        
    agent = create_tool_calling_agent(llm, tools, prompt_agent)
    agent_executor = AgentExecutor(tools=tools, 
                            handle_parsing_errors=True,
                            max_iterations=5,
                            early_stopping_method='generate',
                            agent=agent,
                            return_intermediate_steps=True,
                            callbacks = [tool_handler],
                            verbose=False
                            )



    config = {"configurable": {"session_id": senderId}}
    agent_with_chat_history = RunnableWithMessageHistory(agent_executor,
                                                            lambda session_id: history_reddis,
                                                            input_messages_key="query",
                                                            history_messages_key="chat_history",
                                                            verbose=True,                                                        
                                                            )

    for chunk in agent_with_chat_history.stream({'query': request_data.query}, config=config):
        pass
        # print("First chunk is",chunk)

