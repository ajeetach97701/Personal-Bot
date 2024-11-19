import datetime
from Libs.libs import *
from Agent.agent import generate_response
# buffer convo save
user_conversations = {}
from threading import Thread

class GenerateResponse:
    def __init__(self, **requestData: QueryRequest):
        for key, value in requestData.items():
            setattr(self, key, value)

        # self.history=RedisChatMessageHistory(self.sender, url=f"redis://{self.redis_server}",ttl=60*60*8)

    def generate(self):
        if self.streaming == False:
            return generate_response(self)
        generate_response(self)
    
    def generate_thread(self):
        def start_generation(self):  
            # Creating a thread with generate function as a target  
            thread = Thread(target=generate_response(self), kwargs={"request_data": self})  
            # Starting the thread  
            thread.start()
        return start_generation(self)








