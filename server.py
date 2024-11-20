from Libs.libs import *
from models.vars import DELETE_HISTORY_QUERYS
from Agent.agent import generate_response
from Agent.generate_response import GenerateResponse
from vector_store_update import *
from fastapi.responses import StreamingResponse  
from models.model import tool_handler, tool_queue
app = FastAPI()

REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'

load_dotenv(find_dotenv())

import asyncio



@app.get('/test')
def test_app():
    return {"message": "this application is up and running"}
    

async def response_generator(data:dict):  
    generate_response_instance = GenerateResponse(**data)
    generate_response_instance.generate__()      
    while True:  
        value = tool_queue.get()  
        print("the value is:",value)
        if value == None or tool_queue.empty():
            print("The value is none")
            tool_queue.task_done()  
            break
        yield value 
        tool_queue.task_done()  
        await asyncio.sleep(0.01)

from fastapi import FastAPI
app = FastAPI()
@app.get('/response')
async def get_response(query: str, senderId: str):
    data = {"query": query, "senderId": senderId, }
    return StreamingResponse(response_generator(data=data), media_type='text/event-stream')




@app.get('/update_vector_store')
def update_vs(vector_store: VectorDB, store_name: StoreName, store_key: str):
    if store_key == os.getenv('DROP_STORE_KEY'):
        if vector_store not in [VectorDB.CHROMA]:
            return "Invalid vector store type. And only Chroma works for now. No Milvus not supported"

        update_functions = {
            StoreName.personal_vs: update_personal_store,}
        name = []
        # print("the am is",store_name.value)
        
        # drop all the collection if all is selected
        if store_name == StoreName.all_store:
            for store in update_functions:
                pass
            #     if vector_store == VectorDB.MILVUS:
            #         name.append(store.value)
            #         print(store.value)
            #         drop_collection(store.value)
            #     print(store, " ",  update_functions[store](vector_store))
            #     update_functions[store](vector_store)
            # return f"All collections updated. {name}"

        if store_name in update_functions:
            # if vector_store == VectorDB.MILVUS:
            #     print(store_name.value)
            #     print(store_name, "from here")
            #     print()
            #     drop_collection(store_name.value)
            if vector_store == VectorDB.CHROMA:
                return update_functions[store_name](vector_store)
        else:
            return "Error: Invalid store name."
    else:
        return "Wrong Store key"

