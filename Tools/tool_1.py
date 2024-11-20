import pprint
from Libs.libs import *

# vector_store=Milvus(embedding_function=embeddings,connection_args={"host":host,"port":port},collection_name='wadapatra_wada_karyalaya_kmc')
from langchain.tools import tool
from models.model import get_embeddings
embeddings = get_embeddings(name = "openai")
embedding_function = get_embeddings(name = "openai")
embeddings = get_embeddings("openai")
api_key = os.getenv('OPENAI_API_KEY')
import asyncio
from models.model import get_llm, tool_handler
embedding_function = get_embeddings(name = "openai")

collection_name  =os.getenv("PERSONAL_STORE_NAME")



def retrieval_tool(self):
    def retrieval(query: str):
        """A tool that answers the query related to sports"""
        
        
        query = self.query
        vector_store = Chroma(embedding_function=embedding_function, persist_directory=f"./Chroma/{collection_name}_Chroma")
        context = vector_store.similarity_search(query=query,k=2)
        llm = ChatOpenAI(api_key=api_key, model='gpt-4o-mini')
        print("tool entered")
        prompt = get_prompts('prompt_for_all_tools')

        chain = RunnableMap({
            'query': lambda x: x['query'],
            "context": lambda x: context,
            "name":lambda x:name

        }) | prompt | llm | string_parser
        response = chain.invoke({"query":query})
        print("From tool response is:",response)
        print()
        print()
        print()
        return response
    return retrieval
