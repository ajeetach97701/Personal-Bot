import datetime
from Libs.libs import *
from Agent.agent import generate_response
# buffer convo save
user_conversations = {}

api_key = os.getenv('OPENAI_API_KEY')



from threading import Thread

class GenerateResponse:

    def __init__(self, **requestData: QueryRequest):
        for key, value in requestData.items():
            setattr(self, key, value)

      

    def generate__(self):      
        generate_response(self)
